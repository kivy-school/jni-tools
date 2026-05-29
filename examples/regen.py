#!/usr/bin/env python3
"""Regenerate both jni_core and pyjnius example sources from android.jar.

Usage (from jni-tools/examples/ or anywhere):

    python3 regen.py                          # use default android-36.jar
    python3 regen.py --jar /path/to/android.jar
    python3 regen.py --cython-only
    python3 regen.py --pyjnius-only

The script:
  1. Locates the built jni-wrap binary (builds it if missing).
  2. Runs ``jni-wrap cython`` → writes to jni_core/android/src/ and then runs
     split.py to sync into jni_core/packages/.
  3. Runs ``jni-wrap pyjnius`` → writes to pyjnius/android/src/.
"""
from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).parent.resolve()          # examples/
REPO = HERE.parent                               # jni-tools/
SWIFT_PKG = REPO / "jni-wrapper" / "JniWrap"

JNI_CORE_DIR = HERE / "jni_core"
PYJNIUS_DIR  = HERE / "pyjnius"

CYTHON_MONOLITH_SRC = JNI_CORE_DIR / "android" / "src"
PYJNIUS_ANDROID_SRC = PYJNIUS_DIR / "android" / "src"

_DEFAULT_JAR_CANDIDATES = [
    Path.home() / ".kivyschool" / "android-sdk" / "platforms" / "android-36" / "android.jar",
    Path.home() / ".kivyschool" / "android-sdk" / "platforms" / "android-35" / "android.jar",
    Path.home() / "Library" / "Android" / "sdk" / "platforms" / "android-35" / "android.jar",
]


def _find_jar() -> Path:
    for p in _DEFAULT_JAR_CANDIDATES:
        if p.exists():
            return p
    sys.exit(
        "Cannot find android.jar. Pass --jar or install the Android SDK to one of:\n"
        + "\n".join(f"  {p}" for p in _DEFAULT_JAR_CANDIDATES)
    )


def _jni_wrap_bin() -> Path:
    debug = SWIFT_PKG / ".build" / "debug" / "jni-wrap"
    release = SWIFT_PKG / ".build" / "release" / "jni-wrap"
    if release.exists():
        return release
    if debug.exists():
        return debug
    print("[build] jni-wrap binary not found — running swift build …")
    subprocess.run(["swift", "build", "--package-path", str(SWIFT_PKG)], check=True)
    if not debug.exists():
        sys.exit(f"swift build succeeded but binary not found at {debug}")
    return debug


def regen_cython(jni_wrap: Path, jar: Path) -> None:
    """Regenerate jni_core/android/src/ then resync packages/ via split.py."""
    print(f"\n{'='*60}")
    print(f"[cython] Generating from {jar.name} …")
    print(f"{'='*60}")

    tmp = Path(tempfile.mkdtemp(prefix="jni-wrap-cython-"))
    try:
        cmd = [
            str(jni_wrap), "cython",
            "--keep-package-prefix",
            str(jar),
            str(tmp),
        ]
        print(f"[cython] {' '.join(cmd)}")
        subprocess.run(cmd, check=True)

        # Wipe and replace the monolith src tree.
        if CYTHON_MONOLITH_SRC.exists():
            shutil.rmtree(CYTHON_MONOLITH_SRC)
        CYTHON_MONOLITH_SRC.mkdir(parents=True)

        for ns_dir in sorted(tmp.iterdir()):
            if ns_dir.is_dir():
                shutil.copytree(ns_dir, CYTHON_MONOLITH_SRC / ns_dir.name)
            else:
                shutil.copy2(ns_dir, CYTHON_MONOLITH_SRC / ns_dir.name)

        print(f"[cython] Written to {CYTHON_MONOLITH_SRC}")

    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    # Resync packages/ via split.py.
    print("\n[cython] Syncing packages/ via split.py …")
    subprocess.run(
        [sys.executable, str(JNI_CORE_DIR / "split.py"), "--src", str(CYTHON_MONOLITH_SRC)],
        check=True,
    )
    print("[cython] Done.")


def regen_pyjnius(jni_wrap: Path, jar: Path) -> None:
    """Regenerate pyjnius/android/src/ in-place."""
    print(f"\n{'='*60}")
    print(f"[pyjnius] Generating from {jar.name} …")
    print(f"{'='*60}")

    tmp = Path(tempfile.mkdtemp(prefix="jni-wrap-pyjnius-"))
    try:
        cmd = [
            str(jni_wrap), "pyjnius",
            "--keep-package-prefix",
            str(jar),
            str(tmp),
        ]
        print(f"[pyjnius] {' '.join(cmd)}")
        subprocess.run(cmd, check=True)

        # Wipe and replace the src tree.
        if PYJNIUS_ANDROID_SRC.exists():
            shutil.rmtree(PYJNIUS_ANDROID_SRC)
        PYJNIUS_ANDROID_SRC.mkdir(parents=True)

        for item in sorted(tmp.iterdir()):
            if item.is_dir():
                shutil.copytree(item, PYJNIUS_ANDROID_SRC / item.name)
            else:
                shutil.copy2(item, PYJNIUS_ANDROID_SRC / item.name)

        print(f"[pyjnius] Written to {PYJNIUS_ANDROID_SRC}")

    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    print("[pyjnius] Done.")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--jar", help="Path to android.jar (auto-detected if omitted)")
    ap.add_argument("--cython-only", action="store_true", help="Only regen jni_core")
    ap.add_argument("--pyjnius-only", action="store_true", help="Only regen pyjnius")
    args = ap.parse_args()

    jar = Path(args.jar).resolve() if args.jar else _find_jar()
    if not jar.exists():
        sys.exit(f"JAR not found: {jar}")

    print(f"[regen] android.jar: {jar}")
    jni_wrap = _jni_wrap_bin()
    print(f"[regen] jni-wrap:    {jni_wrap}")

    if args.pyjnius_only:
        regen_pyjnius(jni_wrap, jar)
    elif args.cython_only:
        regen_cython(jni_wrap, jar)
    else:
        regen_cython(jni_wrap, jar)
        regen_pyjnius(jni_wrap, jar)

    print("\n[regen] All done.")


if __name__ == "__main__":
    main()
