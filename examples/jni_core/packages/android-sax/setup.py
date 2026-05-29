"""Build script for the generated android-jni-core Cython package.

Compiles every .pyx under src/ into a parallel set of CPython extension
modules linked to the jni_core runtime. Designed for both desktop testing
(JDK on host) and cibuildwheel Android targets (NDK + the jni.h shipped
inside the NDK sysroot).
"""
from __future__ import annotations

import os
import platform
import sys
from pathlib import Path

from setuptools import Extension, setup
from setuptools.command.build_py import build_py as _build_py

_ANDROID = (
    sys.platform == "android"
    or bool(os.environ.get("ANDROID_NDK_HOME"))
    or bool(os.environ.get("CIBW_ARCHS_ANDROID"))
    or "android" in os.environ.get("CC", "").lower()
)

if _ANDROID:
    try:
        from Cython.Build import cythonize
    except ImportError as exc:
        raise SystemExit(
            "Cython>=3.0 is required to build android-jni-core. "
            "Add it to [build-system] requires."
        ) from exc


HERE = Path(__file__).parent.resolve()
SRC = HERE / "src"

# Ensure CWD is the package directory; python-build may invoke setup.py from
# a different working directory when the package path is passed as argument.
os.chdir(HERE)


def _jni_include_dirs() -> list[str]:
    """Locate jni.h.

    Priority:
      1. ``JNI_INCLUDE_DIR`` env var (set by p4a / cibuildwheel for NDK builds).
      2. ``CC`` env var — cibuildwheel Android sets this to the NDK clang;
         derive sysroot as ``$(dirname $CC)/../sysroot``.
      3. ``JAVA_HOME`` env var + per-platform subdir.
      4. ``/usr/libexec/java_home`` (macOS auto-detect).
    """
    override = os.environ.get("JNI_INCLUDE_DIR")
    if override:
        # Caller supplies a colon-separated list.
        parts = override.split(os.pathsep) if os.pathsep in override else [override]
        return [p for p in parts if p]

    # cibuildwheel Android sets CC to the NDK clang binary, from which we
    # can derive the sysroot that contains jni.h without any extra config.
    cc_parts = os.environ.get("CC", "").split()
    cc = cc_parts[0] if cc_parts else ""
    if cc:
        cc_path = Path(cc)
        # .../bin/<triple>-clangXX -> parent = bin/ -> parent = toolchain root
        sysroot = cc_path.parent.parent / "sysroot"
        jni_h = sysroot / "usr" / "include" / "jni.h"
        if jni_h.exists():
            return [str(sysroot / "usr" / "include")]

    java_home = os.environ.get("JAVA_HOME")
    if not java_home and sys.platform == "darwin":
        from subprocess import run

        res = run(
            ["/usr/libexec/java_home"], capture_output=True, text=True, check=False
        )
        if res.returncode == 0:
            java_home = res.stdout.strip()
    if not java_home:
        raise SystemExit(
            "Cannot find jni.h: set JAVA_HOME, or JNI_INCLUDE_DIR for "
            "Android NDK cross builds."
        )
    base = Path(java_home) / "include"
    if not base.exists():
        raise SystemExit(f"JDK include dir not found: {base}")
    plat_map = {"darwin": "darwin", "linux": "linux", "win32": "win32"}
    plat_sub = plat_map.get(sys.platform, sys.platform)
    return [str(base), str(base / plat_sub)]


def _jni_core_include_dirs() -> list[str]:
    """Locate jni_core .pxd/.pxi Cython headers.

    Priority:
      1. ``vendor/jni_core/`` bundled alongside setup.py — preferred for
         cross-compile environments where jni_core can't be pip-installed
         for the target.
      2. Installed ``jni_core`` package (development / host builds).
    """
    vendor = HERE / "vendor"
    if (vendor / "jni_core" / "_core.pxd").exists():
        # vendor/ acts as the include root so that
        # `include "jni_core/conversions.pxi"` and
        # `from jni_core._core cimport ...` both resolve.
        # vendor/jni_core/ is also added so that C-level #include
        # "_jni_dispatch.h" (from _dispatch.pxd extern) is found.
        return [str(vendor), str(vendor / "jni_core")]

    try:
        import jni_core  # type: ignore
    except ImportError as exc:
        raise SystemExit(
            "jni_core headers not found. Either run from the repo (vendor/ "
            "is present) or install jni_core: pip install jni_core"
        ) from exc
    pkg_dir = Path(jni_core.__file__).parent
    return [str(pkg_dir.parent), str(pkg_dir)]


def _link_args() -> tuple[list[str], list[str]]:
    """libjvm linkage (host-side only). On Android the JVM is the host
    process, so we never link libjvm and instead resolve JNIEnv at runtime
    via JNI_GetCreatedJavaVMs / AttachCurrentThread (jni_core handles this).
    """
    cc = os.environ.get("CC", "")
    if (
        os.environ.get("ANDROID_NDK_HOME")
        or os.environ.get("CIBW_ARCHS_ANDROID")
        or "android" in cc.lower()
    ):
        return [], []
    java_home = os.environ.get("JAVA_HOME") or ""
    if not java_home and sys.platform == "darwin":
        from subprocess import run

        res = run(
            ["/usr/libexec/java_home"], capture_output=True, text=True, check=False
        )
        if res.returncode == 0:
            java_home = res.stdout.strip()
    if not java_home:
        return [], []
    jh = Path(java_home)
    libs: list[str] = []
    extra: list[str] = []
    if sys.platform == "darwin":
        candidates = [jh / "lib" / "server", jh / "jre" / "lib" / "server"]
    elif sys.platform.startswith("linux"):
        arch = platform.machine()
        candidates = [
            jh / "lib" / "server",
            jh / "lib" / arch / "server",
            jh / "jre" / "lib" / arch / "server",
        ]
    else:
        return libs, extra
    for cand in candidates:
        if (cand / ("libjvm.dylib" if sys.platform == "darwin" else "libjvm.so")).exists():
            libs.append("jvm")
            extra.append(f"-L{cand}")
            extra.append(f"-Wl,-rpath,{cand}")
            break
    return libs, extra


def _collect_pyx() -> list[Extension]:
    libraries, extra_link_args = _link_args()
    include_dirs = _jni_core_include_dirs() + _jni_include_dirs()
    ext_modules: list[Extension] = []
    for pyx in SRC.rglob("*.pyx"):
        rel = pyx.relative_to(SRC).with_suffix("")
        module_name = ".".join(rel.parts)
        ext_modules.append(
            Extension(
                name=module_name,
                sources=[str(pyx.relative_to(HERE))],
                include_dirs=include_dirs,
                libraries=libraries,
                extra_link_args=extra_link_args,
                language="c",
            )
        )
    return ext_modules


if _ANDROID:
    ext_modules = cythonize(
        _collect_pyx(),
        language_level=3,
        include_path=_jni_core_include_dirs(),
        nthreads=os.cpu_count() or 1,
        compiler_directives={
            "boundscheck": False,
            "wraparound": False,
            "initializedcheck": False,
            "cdivision": True,
        },
    )
    for _ext in ext_modules:
        _ext.sources = [
            os.path.relpath(s, HERE) if os.path.isabs(s) else s
            for s in _ext.sources
        ]
else:
    ext_modules = []


class _FilteredBuildPy(_build_py):
    """Keep only target-appropriate typing/cimport artifacts in wheels."""

    def run(self) -> None:
        super().run()
        root = Path(self.build_lib)
        if not root.exists():
            return
        pattern = "*.pyi" if _ANDROID else "*.pxd"
        for path in root.rglob(pattern):
            path.unlink()

setup(
    ext_modules=ext_modules,
    cmdclass={"build_py": _FilteredBuildPy},
)
