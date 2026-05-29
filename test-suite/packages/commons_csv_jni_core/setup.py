"""Build script for the commons_csv_jni_core Cython wrapper (macOS desktop)."""
from __future__ import annotations

import os
import sys
from pathlib import Path

from setuptools import Extension, setup
from Cython.Build import cythonize


HERE = Path(__file__).parent.resolve()
SRC = HERE / "src"


def _jni_include_dirs() -> list[str]:
    java_home = os.environ.get("JAVA_HOME") or ""
    if not java_home and sys.platform == "darwin":
        from subprocess import run
        r = run(["/usr/libexec/java_home"], capture_output=True, text=True, check=False)
        if r.returncode == 0:
            java_home = r.stdout.strip()
    if not java_home:
        raise SystemExit("Cannot find jni.h: set JAVA_HOME")
    base = Path(java_home) / "include"
    plat = {"darwin": "darwin", "linux": "linux", "win32": "win32"}.get(sys.platform, sys.platform)
    return [str(base), str(base / plat)]


def _jni_core_include_dirs() -> list[str]:
    import jni_core
    pkg_dir = Path(jni_core.__file__).parent
    return [str(pkg_dir.parent), str(pkg_dir)]


def _link_args() -> tuple[list[str], list[str]]:
    java_home = os.environ.get("JAVA_HOME") or ""
    if not java_home and sys.platform == "darwin":
        from subprocess import run
        r = run(["/usr/libexec/java_home"], capture_output=True, text=True, check=False)
        if r.returncode == 0:
            java_home = r.stdout.strip()
    if not java_home:
        return [], []
    jh = Path(java_home)
    candidates = [jh / "lib" / "server", jh / "jre" / "lib" / "server"]
    for cand in candidates:
        suffix = "libjvm.dylib" if sys.platform == "darwin" else "libjvm.so"
        if (cand / suffix).exists():
            return ["jvm"], [f"-L{cand}", f"-Wl,-rpath,{cand}"]
    return [], []


def _collect_pyx() -> list[Extension]:
    libs, link_args = _link_args()
    incs = _jni_core_include_dirs() + _jni_include_dirs()
    exts = []
    for pyx in SRC.rglob("*.pyx"):
        rel = pyx.relative_to(SRC).with_suffix("")
        name = ".".join(rel.parts)
        exts.append(Extension(
            name=name,
            sources=[str(pyx.relative_to(HERE))],
            include_dirs=incs,
            libraries=libs,
            extra_link_args=link_args,
            language="c",
        ))
    return exts


setup(
    name="commons_csv_jni_core",
    version="1.11.0",
    package_dir={"": "src"},
    packages=[],
    ext_modules=cythonize(
        _collect_pyx(),
        language_level=3,
        include_path=_jni_core_include_dirs(),
        compiler_directives={
            "boundscheck": False,
            "wraparound": False,
            "initializedcheck": False,
            "cdivision": True,
        },
    ),
    zip_safe=False,
)
