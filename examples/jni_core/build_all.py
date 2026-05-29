#!/usr/bin/env python3
from __future__ import annotations
"""Build wheels for all android.jar wrapper packages.

Run from jni-tools/examples/jni_core/:

    # Android compiled wheels (one arch at a time)
    python3 build_all.py --platform android --arch x86_64
    python3 build_all.py --platform android --arch arm64_v8a --skip-existing

    # Pure-python stub wheels (.pyi only, py3-none-any) for IDE / desktop
    python3 build_all.py --platform any
    python3 build_all.py --platform any --skip-existing

    python3 build_all.py --platform android --arch x86_64 --only android-bluetooth
"""

import argparse
import os
import subprocess
import sys
import tomllib
from pathlib import Path

HERE = Path(__file__).parent.resolve()
PACKAGES = HERE / "packages"
WHEELHOUSE = HERE / "wheelhouse"

_ANDROID_SDK_CANDIDATES = [
    Path.home() / ".kivyschool" / "android-sdk",
    Path.home() / "Library" / "Android" / "sdk",
    Path("/opt/android-sdk"),
]


def _resolve_android_home() -> str:
    if v := os.environ.get("ANDROID_HOME"):
        return v
    for candidate in _ANDROID_SDK_CANDIDATES:
        if candidate.is_dir():
            return str(candidate)
    raise SystemExit(
        "Cannot find Android SDK. Set ANDROID_HOME or install to one of:\n"
        + "\n".join(f"  {p}" for p in _ANDROID_SDK_CANDIDATES)
    )


def _dist_name(pkg_dir: Path) -> str:
    with open(pkg_dir / "pyproject.toml", "rb") as f:
        return tomllib.load(f)["project"]["name"].replace("-", "_")


def _has_wheel(pkg_dir: Path, arch: str) -> bool:
    name = _dist_name(pkg_dir)
    if arch == "any":
        return any(WHEELHOUSE.glob(f"{name}-*-none-any.whl"))
    return any(WHEELHOUSE.glob(f"{name}-*_{arch}.whl"))


def _build_android(pkg_dir: Path, arch: str) -> bool:
    WHEELHOUSE.mkdir(exist_ok=True)
    env = os.environ.copy()
    env.setdefault("ANDROID_HOME", _resolve_android_home())
    result = subprocess.run(
        [
            "cibuildwheel", "--platform", "android",
            "--archs", arch,
            "--output-dir", str(WHEELHOUSE),
            ".",
        ],
        cwd=pkg_dir,
        env=env,
    )
    return result.returncode == 0


def _build_any(pkg_dir: Path) -> bool:
    """Build a pure-python stub wheel — setup.py detects non-Android and skips Cython."""
    WHEELHOUSE.mkdir(exist_ok=True)
    result = subprocess.run(
        [sys.executable, "-m", "pip", "wheel", ".", "--no-deps", "-w", str(WHEELHOUSE)],
        cwd=pkg_dir,
    )
    return result.returncode == 0


def main() -> None:
    ap = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    ap.add_argument(
        "--platform",
        required=True,
        choices=["android", "any"],
        help="android: compiled via cibuildwheel; any: .pyi stub wheels for IDE/desktop",
    )
    ap.add_argument(
        "--arch",
        choices=["arm64_v8a", "x86_64"],
        help="Android target arch (required when --platform android)",
    )
    ap.add_argument(
        "--skip-existing",
        action="store_true",
        help="Skip packages that already have a matching .whl in wheelhouse/",
    )
    ap.add_argument(
        "--only",
        nargs="+",
        metavar="PKG",
        help="Only build these package dir names (e.g. android-bluetooth java)",
    )
    args = ap.parse_args()

    if args.platform == "android" and not args.arch:
        ap.error("--arch is required when --platform android")

    arch = args.arch if args.platform == "android" else "any"

    if args.only:
        pkg_dirs = [PACKAGES / n for n in args.only]
    else:
        pkg_dirs = sorted(p for p in PACKAGES.iterdir() if p.is_dir())

    pkg_dirs = [p for p in pkg_dirs if (p / "pyproject.toml").exists()]

    failed: list[str] = []
    for pkg_dir in pkg_dirs:
        name = pkg_dir.name
        # Shell/meta packages have no src/ — always a pure py3-none-any wheel.
        is_shell = not (pkg_dir / "src").exists()
        effective_arch = "any" if is_shell else arch
        if args.skip_existing and _has_wheel(pkg_dir, effective_arch):
            print(f"[skip]  {name}")
            continue
        print(f"[build] {name} …")
        if is_shell or args.platform == "any":
            ok = _build_any(pkg_dir)
        else:
            ok = _build_android(pkg_dir, arch)
        if ok:
            print(f"[ok]    {name}")
        else:
            print(f"[FAIL]  {name}", file=sys.stderr)
            failed.append(name)

    if failed:
        print(f"\nFailed ({len(failed)}): {', '.join(failed)}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
