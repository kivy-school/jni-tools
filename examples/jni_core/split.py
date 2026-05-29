#!/usr/bin/env python3
"""Split generated android.jar Cython sources into kivy-garden-style pip packages.

Run from jni-tools/examples/jni_core/:

    python3 split.py [OPTIONS]

The generator output (``android/src/``) contains five top-level Java
namespaces — ``android/``, ``dalvik/``, ``java/``, ``javax/``, ``org/`` —
each holding the .pyx/.pxd/.pyi for one class hierarchy of API 35.

This script reshapes that monolith into a set of PyPI distributions that
all install into the same PEP 420 implicit namespace ``android/``::

    Distribution name           Ships filesystem tree         Imports as
    --------------------------- ----------------------------- ----------------------
    android-java                src/android/java/             android.java.*
    android-javax               src/android/javax/            android.javax.*
    android-org                 src/android/org/              android.org.*
    android-dalvik              src/android/dalvik/           android.dalvik.*
    android-android             src/android/android/{Manifest,R}.{pyx,pxd,pyi}
                                                              android.android.{Manifest,R}
    android-android-<group>     src/android/android/<group>/  android.android.<group>.*

``android-android`` is a small **shell**: it ships only the top-level
``Manifest``/``R`` classes plus ``[project.optional-dependencies]`` extras
that pull in per-group dists.  Users write::

    dependencies = [
        "android-java",
        "android-org",
        "android-android[bluetooth, text]",
    ]

Options
-------
--src DIR        Root containing the generated namespace subdirs
                 (default: android/src).  Must have android/, java/, etc.
--gen            Run the Swift jni-wrap generator first, writing output
                 to a temp dir and using that as --src automatically.
--build          Run cibuildwheel on each package after the sync.
--android-sdk P  ANDROID_HOME for cibuildwheel (default: $ANDROID_HOME).
--jar PATH       Path to android.jar used by --gen
                 (default: ~/.kivyschool/android-sdk/platforms/android-35/android.jar).
"""
from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).parent.resolve()       # jni-tools/examples/jni_core/
MONOLITH = HERE / "android"                  # existing monolith package (shared assets)
PACKAGES = HERE / "packages"                 # per-distribution package dirs

VERSION = "35.0.0"
PY_REQUIRES = ">=3.11"

# Top-level Java namespaces that each become a single monolithic distribution.
SIMPLE_NS = ["javax", "org", "dalvik"]
# Namespaces split per-subdirectory into one dist each, fronted by a shell dist
# with optional-dependency extras.  Includes both ``java`` and ``android``.
SPLIT_NS = ["java", "android"]

# Generated .c lives in build/, never in the wheel src tree.
_SKIP_EXTS = {".c"}


# ---------------------------------------------------------------------------
# pyproject.toml templates
# ---------------------------------------------------------------------------

_PYPROJECT_SHELL_HEAD = """\
[build-system]
requires = ["setuptools>=68", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "{name}"
version = "{version}"
description = "{description}"
requires-python = "{py_requires}"
dependencies = [
{deps}]
"""

_PYPROJECT_HEAD = """\
[build-system]
requires = ["setuptools>=68", "wheel", "cython>=3.0"]
build-backend = "setuptools.build_meta"

[project]
name = "{name}"
version = "{version}"
description = "{description}"
requires-python = "{py_requires}"
dependencies = [
{deps}]
"""

_PYPROJECT_TAIL = """\

[tool.setuptools.packages.find]
where = ["src"]
namespaces = true

[tool.setuptools.package-data]
"*" = ["*.pxd", "*.pyi"]

[tool.setuptools.exclude-package-data]
"*" = [".DS_Store", "*.DS_Store", "*.c", "*.pyx", "*.pxi"]

[tool.cibuildwheel]
build = "cp313-android_*"

[tool.cibuildwheel.android]
archs = ["arm64_v8a", "x86_64"]
"""

# Shell/meta packages have no source — no cython, no packages.find, no cibuildwheel.
_PYPROJECT_SHELL_TAIL = """\

[tool.setuptools]
packages = []
"""


def _format_deps(deps: list[str]) -> str:
    if not deps:
        return ""
    return "".join(f'    "{d}",\n' for d in deps)


def _format_extras(extras: dict[str, list[str]]) -> str:
    if not extras:
        return ""
    lines = ["\n[project.optional-dependencies]\n"]
    for key in sorted(extras):
        values = extras[key]
        lines.append(f"{key} = [\n")
        for v in values:
            lines.append(f'    "{v}",\n')
        lines.append("]\n")
    return "".join(lines)


def _render_pyproject(
    *,
    name: str,
    description: str,
    deps: list[str],
    extras: dict[str, list[str]] | None = None,
) -> str:
    head = _PYPROJECT_HEAD.format(
        name=name,
        version=VERSION,
        description=description,
        py_requires=PY_REQUIRES,
        deps=_format_deps(deps),
    )
    extras_block = _format_extras(extras or {})
    return head + extras_block + _PYPROJECT_TAIL


def _render_shell_pyproject(
    *,
    name: str,
    description: str,
    extras: dict[str, list[str]],
) -> str:
    head = _PYPROJECT_SHELL_HEAD.format(
        name=name,
        version=VERSION,
        description=description,
        py_requires=PY_REQUIRES,
        deps="",
    )
    extras_block = _format_extras(extras)
    return head + extras_block + _PYPROJECT_SHELL_TAIL


# ---------------------------------------------------------------------------
# File sync helpers
# ---------------------------------------------------------------------------

def _is_namespace_init(rel: Path) -> bool:
    """``__init__.py`` files at the root of a synced ns must not ship.

    The Cython generator emits ``__init__.py`` at every level including
    the namespace root (``java/__init__.py``, ``android/__init__.py``).
    We strip the one at the very top of each sync tree so ``src/android/``
    and ``src/android/android/`` stay PEP 420 implicit namespace dirs.
    """
    return rel.parts == ("__init__.py",)


def _copy_tree(src: Path, dst: Path, *, top_only: bool = False) -> int:
    """Copy non-.c files from src to dst, mkdir-p as needed.

    ``top_only=True`` copies just the regular files at the root of src
    (no recursion into subdirs) — used to populate the android shell with
    Manifest/R but no group subtrees.
    """
    dst.mkdir(parents=True, exist_ok=True)
    copied = 0
    if top_only:
        for item in src.iterdir():
            if item.is_dir():
                continue
            if item.suffix in _SKIP_EXTS:
                continue
            if _is_namespace_init(Path(item.name)):
                continue
            shutil.copy2(item, dst / item.name)
            copied += 1
        return copied

    for item in src.rglob("*"):
        if item.is_dir():
            continue
        if item.suffix in _SKIP_EXTS:
            continue
        rel = item.relative_to(src)
        if _is_namespace_init(rel):
            continue
        dest = dst / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(item, dest)
        copied += 1
    return copied


def _copy_shared_assets(pkg_dir: Path) -> None:
    """Copy ``setup.py``, ``MANIFEST.in`` and ``vendor/jni_core/`` into pkg_dir.

    Both are shared across all packages; they live in the monolith and are
    re-copied on every run so updates to setup.py propagate to all dists.
    """
    for fname in ("setup.py", "MANIFEST.in"):
        src = MONOLITH / fname
        if src.exists():
            shutil.copy2(src, pkg_dir / fname)

    vendor_src = MONOLITH / "vendor" / "jni_core"
    vendor_dst = pkg_dir / "vendor" / "jni_core"
    if vendor_src.exists():
        if vendor_dst.exists():
            shutil.rmtree(vendor_dst)
        shutil.copytree(vendor_src, vendor_dst)


def _reset_src(pkg_dir: Path, ns_path: tuple[str, ...]) -> Path:
    """Wipe pkg_dir/src/<ns_path> and return the empty dir.

    Each split.py run starts from a clean tree so removed classes in the
    generator output don't linger as orphan .pyx files.
    """
    src_root = pkg_dir / "src"
    target = src_root.joinpath(*ns_path)
    if target.exists():
        shutil.rmtree(target)
    # If src/ itself contains no other content, blow it away too so the
    # PEP 420 namespace dirs are recreated fresh.
    if src_root.exists() and not any(src_root.iterdir()):
        shutil.rmtree(src_root)
    target.mkdir(parents=True, exist_ok=True)
    return target


# ---------------------------------------------------------------------------
# Discovery
# ---------------------------------------------------------------------------

def _discover_ns_groups(src_root: Path, ns: str) -> list[str]:
    """List subdirectories of ``<src>/<ns>/`` — one per group dist."""
    base = src_root / ns
    if not base.is_dir():
        return []
    return sorted(p.name for p in base.iterdir() if p.is_dir() and not p.name.startswith("."))


def _discover_ns_toplevel(src_root: Path, ns: str) -> list[str]:
    """List unique stems of top-level class files directly under ``<src>/<ns>/``.

    These are single classes like ``Manifest`` and ``R`` under ``android/``
    that live at the ``android.<ns>`` level, not inside a subdirectory group.
    """
    base = src_root / ns
    if not base.is_dir():
        return []
    stems = sorted({
        f.stem for f in base.iterdir()
        if f.is_file()
        and f.suffix in {".pyx", ".pxd", ".pyi"}
        and f.stem != "__init__"
    })
    return stems


# ---------------------------------------------------------------------------
# Per-distribution build
# ---------------------------------------------------------------------------

def _materialise_simple_ns(src_root: Path, ns: str) -> Path:
    """Generate ``packages/<ns>/`` for a top-level Java namespace.

    Distribution name ``android-<ns>``; ships ``src/android/<ns>/`` and
    imports as ``android.<ns>.*``.
    """
    pkg_dir = PACKAGES / ns
    pkg_dir.mkdir(parents=True, exist_ok=True)

    target = _reset_src(pkg_dir, ("android", ns))
    n = _copy_tree(src_root / ns, target)

    pyproject = _render_pyproject(
        name=f"android-{ns}",
        description=(
            f"Cython JNI wrappers for the {ns}.* namespace "
            f"(android.jar, API 35). Imports as android.{ns}.*."
        ),
        deps=["jni_core"],
    )
    (pkg_dir / "pyproject.toml").write_text(pyproject)
    _copy_shared_assets(pkg_dir)
    return pkg_dir, n


def _materialise_ns_toplevel(src_root: Path, ns: str, stem: str) -> tuple[Path, int]:
    """Generate ``packages/<ns>-<stem>/`` for a single top-level class in a split ns.

    Distribution name ``android-<ns>-<stem>`` (lower-cased); ships
    ``src/android/<ns>/<Stem>.{pyx,pxd,pyi}`` and imports as
    ``android.<ns>.<Stem>``.
    """
    key = stem.lower()
    pkg_dir = PACKAGES / f"{ns}-{key}"
    pkg_dir.mkdir(parents=True, exist_ok=True)

    target = _reset_src(pkg_dir, ("android", ns))
    src_dir = src_root / ns
    n = 0
    for f in src_dir.iterdir():
        if f.is_file() and f.stem == stem and f.suffix not in _SKIP_EXTS:
            shutil.copy2(f, target / f.name)
            n += 1

    pyproject = _render_pyproject(
        name=f"android-{ns}-{key}",
        description=(
            f"Cython JNI wrapper for {ns}.{stem} "
            f"(android.jar, API 35). Imports as android.{ns}.{stem}."
        ),
        deps=["jni_core", f"android-{ns} == {VERSION}"],
    )
    (pkg_dir / "pyproject.toml").write_text(pyproject)
    _copy_shared_assets(pkg_dir)
    return pkg_dir, n


def _materialise_ns_group(src_root: Path, ns: str, group: str) -> tuple[Path, int]:
    """Generate ``packages/<ns>-<group>/`` for one subgroup of a split namespace.

    Distribution name ``android-<ns>-<group>``; ships
    ``src/android/<ns>/<group>/`` and imports as ``android.<ns>.<group>.*``.
    """
    pkg_dir = PACKAGES / f"{ns}-{group}"
    pkg_dir.mkdir(parents=True, exist_ok=True)

    target = _reset_src(pkg_dir, ("android", ns, group))
    n = _copy_tree(src_root / ns / group, target)

    pyproject = _render_pyproject(
        name=f"android-{ns}-{group}",
        description=(
            f"Cython JNI wrappers for the {ns}.{group}.* subpackage "
            f"(android.jar, API 35). Imports as android.{ns}.{group}.*."
        ),
        deps=["jni_core", f"android-{ns} == {VERSION}"],
    )
    (pkg_dir / "pyproject.toml").write_text(pyproject)
    _copy_shared_assets(pkg_dir)
    return pkg_dir, n


def _materialise_ns_shell(
    ns: str, toplevel: list[str], groups: list[str]
) -> tuple[Path, int]:
    """Generate ``packages/<ns>/`` shell dist.

    Pure meta-package: no source. Provides
    ``[project.optional-dependencies]`` extras for every top-level class
    and every group plus ``[all]``.
    """
    pkg_dir = PACKAGES / ns
    pkg_dir.mkdir(parents=True, exist_ok=True)

    # Remove any stale source tree left over from a previous simple-ns run.
    src_tree = pkg_dir / "src"
    if src_tree.exists():
        shutil.rmtree(src_tree)

    extras: dict[str, list[str]] = {}
    for stem in toplevel:
        extras[stem.lower()] = [f"android-{ns}-{stem.lower()} == {VERSION}"]
    for group in groups:
        extras[group] = [f"android-{ns}-{group} == {VERSION}"]
    all_deps = (
        [f"android-{ns}-{s.lower()} == {VERSION}" for s in toplevel]
        + [f"android-{ns}-{g} == {VERSION}" for g in groups]
    )
    if all_deps:
        extras["all"] = all_deps

    pyproject = _render_shell_pyproject(
        name=f"android-{ns}",
        description=(
            f"Meta-package for the android.{ns}.* namespace "
            f"(android.jar, API 35). Use extras to pull in individual "
            f"dists: [{', '.join(list(extras)[:3])}, …, all]."
        ),
        extras=extras,
    )
    (pkg_dir / "pyproject.toml").write_text(pyproject)
    # No setup.py / vendor / MANIFEST.in — pure metadata, no compiled code.
    for leftover in ("setup.py", "MANIFEST.in", "vendor"):
        target = pkg_dir / leftover
        if target.is_file():
            target.unlink()
        elif target.is_dir():
            shutil.rmtree(target)
    return pkg_dir, 0


# ---------------------------------------------------------------------------
# Generator
# ---------------------------------------------------------------------------

def _run_generator(jar: str, out_dir: Path) -> None:
    """Invoke the Swift jni-wrap cython generator into ``out_dir``."""
    swift_pkg = HERE.parent.parent / "jni-wrapper" / "JniWrap"
    if not swift_pkg.exists():
        sys.exit(f"Swift package not found: {swift_pkg}")
    out_dir.mkdir(parents=True, exist_ok=True)
    cmd = [
        "swift", "run",
        "--package-path", str(swift_pkg),
        "jni-wrap", "cython",
        "--keep-package-prefix",
        jar,
        str(out_dir),
    ]
    print(f"[gen] running: {' '.join(cmd)}")
    subprocess.run(cmd, check=True)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    default_jar = str(
        Path("~/.kivyschool/android-sdk/platforms/android-35/android.jar").expanduser()
    )

    ap = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    ap.add_argument(
        "--src",
        default=str(MONOLITH / "src"),
        help="Root of generated namespace dirs (default: android/src)",
    )
    ap.add_argument(
        "--gen",
        action="store_true",
        help="Run the Swift generator before splitting",
    )
    ap.add_argument(
        "--jar",
        default=default_jar,
        help=f"android.jar path used by --gen (default: {default_jar})",
    )
    ap.add_argument(
        "--build",
        action="store_true",
        help="Run cibuildwheel on each package after splitting",
    )
    ap.add_argument(
        "--android-sdk",
        default=os.environ.get("ANDROID_HOME", ""),
        help="ANDROID_HOME for cibuildwheel (default: $ANDROID_HOME)",
    )
    args = ap.parse_args()

    if args.gen:
        tmp = Path(tempfile.mkdtemp(prefix="android-cy-"))
        print(f"[gen] output dir: {tmp}")
        _run_generator(args.jar, tmp)
        src_root = tmp
    else:
        src_root = Path(args.src).resolve()

    if not src_root.is_dir():
        sys.exit(f"--src not a directory: {src_root}")

    # Track all package dirs produced so --build can iterate them.
    produced: list[Path] = []

    # 1) Simple top-level namespaces (one dist per namespace).
    for ns in SIMPLE_NS:
        src_ns = src_root / ns
        if not src_ns.is_dir():
            print(f"[skip] {ns}: not found in {src_root}", file=sys.stderr)
            continue
        print(f"[{ns}] syncing → packages/{ns} …", end=" ", flush=True)
        pkg_dir, n = _materialise_simple_ns(src_root, ns)
        print(f"{n} files")
        produced.append(pkg_dir)

    # 2) Split namespaces: one dist per subgroup + a shell meta-package.
    for ns in SPLIT_NS:
        if not (src_root / ns).is_dir():
            print(f"[skip] {ns}: not found in {src_root}", file=sys.stderr)
            continue
        toplevel = _discover_ns_toplevel(src_root, ns)
        groups = _discover_ns_groups(src_root, ns)
        print(f"[{ns}] discovered {len(toplevel)} top-level classes, {len(groups)} groups")

        for stem in toplevel:
            print(f"[{ns}-{stem.lower()}] syncing …", end=" ", flush=True)
            pkg_dir, n = _materialise_ns_toplevel(src_root, ns, stem)
            print(f"{n} files")
            produced.append(pkg_dir)

        for group in groups:
            print(f"[{ns}-{group}] syncing …", end=" ", flush=True)
            pkg_dir, n = _materialise_ns_group(src_root, ns, group)
            print(f"{n} files")
            produced.append(pkg_dir)

        print(f"[{ns}] syncing shell (meta + extras) …", end=" ", flush=True)
        pkg_dir, _ = _materialise_ns_shell(ns, toplevel, groups)
        print(f"{len(toplevel) + len(groups)} extras")
        produced.append(pkg_dir)

    print(f"\n{len(produced)} packages ready under {PACKAGES}/")

    if not args.build:
        return

    env = os.environ.copy()
    if args.android_sdk:
        env["ANDROID_HOME"] = args.android_sdk

    failed: list[str] = []
    for pkg_dir in produced:
        wh = pkg_dir / "wheelhouse"
        wh.mkdir(exist_ok=True)
        print(f"\n{'=' * 60}")
        print(f"[{pkg_dir.name}] cibuildwheel …")
        print(f"{'=' * 60}")
        r = subprocess.run(
            ["cibuildwheel", "--platform", "android",
             "--output-dir", str(wh), str(pkg_dir)],
            env=env,
        )
        if r.returncode != 0:
            failed.append(pkg_dir.name)

    if failed:
        print(f"\nFailed: {', '.join(failed)}", file=sys.stderr)
        sys.exit(1)
    print("\nAll packages built successfully.")


if __name__ == "__main__":
    main()
