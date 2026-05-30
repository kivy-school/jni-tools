"""Hatch build hook — compiles the Swift jni-wrap binary into bin/jni-wrap.
hatchling's shared-scripts then installs it directly to .venv/bin/jni-wrap.

In CI the binary is pre-built (universal2 on macOS, x86_64 on Linux) and
placed into bin/jni-wrap before `uv build --wheel` is called.
Set JNI_TOOLS_SKIP_SWIFT_BUILD=1 to skip the Swift build step (CI uses this).
"""
from __future__ import annotations

import os
import platform
import shutil
import subprocess
import sys
from pathlib import Path

from hatchling.builders.hooks.plugin.interface import BuildHookInterface


SWIFT_PKG = Path(__file__).parent / "jni-wrapper" / "JniWrap"
BIN_DIR   = Path(__file__).parent / "bin"


class JniWrapBuildHook(BuildHookInterface):
    PLUGIN_NAME = "jni-wrap-swift"

    def initialize(self, version: str, build_data: dict) -> None:
        system = platform.system()
        if system not in ("Darwin", "Linux"):
            return

        dest = BIN_DIR / "jni-wrap"

        if os.environ.get("JNI_TOOLS_SKIP_SWIFT_BUILD"):
            # Binary was pre-built by CI — just verify it exists.
            if not dest.exists():
                sys.exit(f"JNI_TOOLS_SKIP_SWIFT_BUILD set but binary not found: {dest}")
        else:
            self._build_native(dest)

        build_data["tag"] = self._wheel_tag(system, dest)

        # Bundle any dylibs/so files that were copied to bin/ alongside jni-wrap.
        # The binary has @loader_path in its rpath, so dylibs in the same
        # directory as the installed binary will be found automatically.
        proj_version = self.metadata.version
        dist = "jni_tools"
        force: dict[str, str] = build_data.setdefault("force_include", {})
        for lib in BIN_DIR.glob("*.dylib"):
            force[str(lib)] = f"{dist}-{proj_version}.data/scripts/{lib.name}"
        for lib in BIN_DIR.glob("*.so"):
            force[str(lib)] = f"{dist}-{proj_version}.data/scripts/{lib.name}"

    def _build_native(self, dest: Path) -> None:
        subprocess.run(
            ["swift", "build", "--configuration", "release",
             "--package-path", str(SWIFT_PKG)],
            check=True,
        )
        release_dir = SWIFT_PKG / ".build" / "release"
        src = release_dir / "jni-wrap"
        if not src.exists():
            sys.exit(f"Swift build succeeded but binary not found: {src}")
        BIN_DIR.mkdir(exist_ok=True)
        shutil.copy2(src, dest)
        dest.chmod(0o755)
        # Create stub dylibs for each dynamic library the binary links via @rpath.
        # jni-wrap statically embeds ALL SwiftJava symbols (SPM compiles the
        # JavaLangReflect/JavaNet/etc. static products which pull in SwiftJava
        # sources). The stubs satisfy dyld's load requirement without registering
        # the same ObjC classes a second time — preventing the duplicate-class
        # warnings and potential casting failures.
        for lib in release_dir.glob("*.dylib"):
            self._make_stub_dylib(BIN_DIR / lib.name)
        for lib in release_dir.glob("*.so"):
            self._make_stub_so(BIN_DIR / lib.name)

    @staticmethod
    def _make_stub_dylib(target: Path, archs: list[str] | None = None) -> None:
        """Compile a minimal stub dylib that satisfies dyld without symbols."""
        import tempfile
        with tempfile.NamedTemporaryFile(suffix=".c", mode="w", delete=False) as f:
            f.write('__attribute__((visibility("default"))) void __jni_wrap_stub(void){}\n')
            src = Path(f.name)
        arch_flags: list[str] = []
        for a in (archs or []):
            arch_flags += ["-arch", a]
        try:
            subprocess.run(
                ["clang", "-dynamiclib",
                 "-compatibility_version", "0.0.0",
                 "-current_version", "0.0.0",
                 *arch_flags, "-o", str(target), str(src)],
                check=True, capture_output=True,
            )
        finally:
            src.unlink(missing_ok=True)

    @staticmethod
    def _make_stub_so(target: Path) -> None:
        """Compile a minimal stub shared object that satisfies the dynamic linker."""
        import tempfile
        with tempfile.NamedTemporaryFile(suffix=".c", mode="w", delete=False) as f:
            f.write('void __jni_wrap_stub(void){}\n')
            src = Path(f.name)
        try:
            subprocess.run(
                ["gcc", "-shared", "-fPIC", "-o", str(target), str(src)],
                check=True, capture_output=True,
            )
        finally:
            src.unlink(missing_ok=True)

    @staticmethod
    def _wheel_tag(system: str, binary: Path) -> str:
        if system == "Darwin":
            # Detect universal2 by checking if binary contains both arches.
            r = subprocess.run(
                ["lipo", "-info", str(binary)], capture_output=True, text=True
            )
            if "arm64" in r.stdout and "x86_64" in r.stdout:
                return "py3-none-macosx_13_0_universal2"
            # Native dev build — use current arch.
            import sysconfig
            plat = sysconfig.get_platform().replace("-", "_").replace(".", "_")
            return f"py3-none-{plat}"
        # Linux — built on x86_64 runner.
        return "py3-none-linux_x86_64"
