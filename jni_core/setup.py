"""Build script for jni_core.

Resolves jni.h from $JAVA_HOME and compiles the Cython extension. The
package is otherwise declared in pyproject.toml; this file exists only
because we need to compute include_dirs at build time.
"""
from __future__ import annotations

import os
import platform
import sys
from pathlib import Path

from setuptools import Extension, setup

try:
    from Cython.Build import cythonize
except ImportError as exc:  # pragma: no cover - build-time only
    raise SystemExit(
        "Cython>=3.0 is required to build jni_core. Install build deps first."
    ) from exc


def _java_include_dirs() -> list[str]:
    java_home = os.environ.get("JAVA_HOME")
    if not java_home:
        if sys.platform == "darwin":
            # /usr/libexec/java_home is the macOS convention.
            from subprocess import run

            res = run(
                ["/usr/libexec/java_home"], capture_output=True, text=True, check=False
            )
            if res.returncode == 0:
                java_home = res.stdout.strip()
    if not java_home:
        raise SystemExit(
            "JAVA_HOME is not set and could not be auto-detected; "
            "set it to a JDK install before building jni_core."
        )
    base = Path(java_home) / "include"
    if not base.exists():
        raise SystemExit(f"JDK include dir not found: {base}")
    plat_map = {"darwin": "darwin", "linux": "linux", "win32": "win32"}
    plat_sub = plat_map.get(sys.platform, sys.platform)
    return [str(base), str(base / plat_sub)]


def _link_args() -> tuple[list[str], list[str]]:
    """Return (libraries, extra_link_args) needed to link against libjvm.

    Tests need to dlopen libjvm; we link weakly via runtime-search paths so
    the extension imports cleanly even without a JVM (caller may attach an
    existing JVM provided by p4a/pyjnius at runtime).
    """
    java_home = os.environ.get("JAVA_HOME") or ""
    if not java_home and sys.platform == "darwin":
        from subprocess import run

        res = run(
            ["/usr/libexec/java_home"], capture_output=True, text=True, check=False
        )
        if res.returncode == 0:
            java_home = res.stdout.strip()

    libs: list[str] = []
    extra: list[str] = []
    if not java_home:
        return libs, extra
    jh = Path(java_home)
    if sys.platform == "darwin":
        candidates = [jh / "lib" / "server", jh / "jre" / "lib" / "server"]
    elif sys.platform.startswith("linux"):
        arch = platform.machine()
        candidates = [
            jh / "lib" / "server",
            jh / "lib" / arch / "server",
            jh / "jre" / "lib" / arch / "server",
        ]
    else:  # win32 / android: caller arranges linking
        return libs, extra
    for cand in candidates:
        if (cand / ("libjvm.dylib" if sys.platform == "darwin" else "libjvm.so")).exists():
            libs.append("jvm")
            extra.append(f"-L{cand}")
            extra.append(f"-Wl,-rpath,{cand}")
            break
    return libs, extra


libraries, extra_link_args = _link_args()

_PKG_DIR = str(Path(__file__).parent / "src" / "jni_core")

ext_modules = cythonize(
    [
        Extension(
            name="jni_core._core",
            sources=["src/jni_core/_core.pyx"],
            include_dirs=_java_include_dirs() + [_PKG_DIR],
            libraries=libraries,
            extra_link_args=extra_link_args,
            language="c",
        ),
    ],
    language_level=3,
    include_path=[str(Path(__file__).parent / "src")],
)

setup(ext_modules=ext_modules)
