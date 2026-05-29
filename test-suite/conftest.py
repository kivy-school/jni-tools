"""Session fixtures shared by both backend tests."""
from __future__ import annotations

import hashlib
import os
import shutil
import subprocess
import sys
import urllib.request
from pathlib import Path

import pytest


HERE = Path(__file__).parent.resolve()
REPO_ROOT = HERE.parent  # jni-tools/
JNI_WRAPPER_DIR = REPO_ROOT / "jni-wrapper" / "JniWrap"

COMMONS_CSV_VERSION = "1.11.0"
COMMONS_CSV_URL = (
    "https://repo1.maven.org/maven2/org/apache/commons/commons-csv/"
    f"{COMMONS_CSV_VERSION}/commons-csv-{COMMONS_CSV_VERSION}.jar"
)
# SHA-1 published by Maven Central next to the jar (.sha1 sidecar) —
# we re-fetch it at download time to detect upstream tampering.
COMMONS_CSV_SHA1 = "8f2dc805097da534612128b7cdf491a5a76752bf"

# commons-csv 1.11.0 references org.apache.commons.io.output.AppendableOutputStream,
# so the reflection JVM also needs commons-io on the classpath to load CSVFormat.
COMMONS_IO_VERSION = "2.16.1"
COMMONS_IO_URL = (
    "https://repo1.maven.org/maven2/commons-io/commons-io/"
    f"{COMMONS_IO_VERSION}/commons-io-{COMMONS_IO_VERSION}.jar"
)
COMMONS_IO_SHA1 = "377d592e740dc77124e0901291dbfaa6810a200e"

# commons-csv 1.11.0 also references commons-codec (e.g. Base64OutputStream).
COMMONS_CODEC_VERSION = "1.16.1"
COMMONS_CODEC_URL = (
    "https://repo1.maven.org/maven2/commons-codec/commons-codec/"
    f"{COMMONS_CODEC_VERSION}/commons-codec-{COMMONS_CODEC_VERSION}.jar"
)
COMMONS_CODEC_SHA1 = "47bd4d333fba53406f6c6c51884ddbca435c8862"

CSV_SAMPLE_TEXT = (
    "name,age,city\n"
    "Alice,30,NYC\n"
    "Bob,25,LA\n"
    "Charlie,35,Boston\n"
)
CSV_EXPECTED_HEADERS = ["name", "age", "city"]
CSV_EXPECTED_ROW_COUNT = 3  # data rows (excluding header)


def pytest_collection_modifyitems(config, items):
    """Skip everything on non-macOS hosts."""
    if sys.platform == "darwin":
        return
    skip_marker = pytest.mark.skip(reason="jni-tools test-suite is macOS-only for now")
    for item in items:
        item.add_marker(skip_marker)


def _sha1(path: Path) -> str:
    h = hashlib.sha1()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def _cached_jar(url: str, filename: str, expected_sha1: str) -> Path:
    cache_dir = Path.home() / ".cache" / "jni-tools-tests"
    cache_dir.mkdir(parents=True, exist_ok=True)
    dest = cache_dir / filename
    if dest.exists() and _sha1(dest) == expected_sha1:
        return dest
    urllib.request.urlretrieve(url, dest)
    got = _sha1(dest)
    if got != expected_sha1:
        dest.unlink(missing_ok=True)
        raise RuntimeError(
            f"{filename} SHA-1 mismatch: expected {expected_sha1}, got {got}"
        )
    return dest


@pytest.fixture(scope="session")
def commons_csv_jar() -> Path:
    """Download (once) and return path to the commons-csv jar."""
    return _cached_jar(
        COMMONS_CSV_URL, f"commons-csv-{COMMONS_CSV_VERSION}.jar", COMMONS_CSV_SHA1
    )


@pytest.fixture(scope="session")
def commons_io_jar() -> Path:
    """commons-io is a transitive dep of commons-csv at reflection time."""
    return _cached_jar(
        COMMONS_IO_URL, f"commons-io-{COMMONS_IO_VERSION}.jar", COMMONS_IO_SHA1
    )


@pytest.fixture(scope="session")
def commons_codec_jar() -> Path:
    """commons-codec is a transitive dep of commons-csv at reflection time."""
    return _cached_jar(
        COMMONS_CODEC_URL, f"commons-codec-{COMMONS_CODEC_VERSION}.jar", COMMONS_CODEC_SHA1
    )


@pytest.fixture(scope="session")
def csv_sample_path(tmp_path_factory) -> Path:
    p = tmp_path_factory.mktemp("csv") / "sample.csv"
    p.write_text(CSV_SAMPLE_TEXT, encoding="utf-8")
    return p


@pytest.fixture(scope="session")
def jni_wrap_bin() -> Path:
    """Build the Swift package once and return the path to the jni-wrap binary."""
    bin_path = JNI_WRAPPER_DIR / ".build" / "debug" / "jni-wrap"
    if not bin_path.exists():
        subprocess.run(
            ["swift", "build"],
            cwd=JNI_WRAPPER_DIR,
            check=True,
        )
    assert bin_path.exists(), f"swift build did not produce {bin_path}"
    return bin_path


@pytest.fixture(scope="session")
def java_home() -> str:
    jh = os.environ.get("JAVA_HOME")
    if jh and Path(jh).is_dir():
        return jh
    res = subprocess.run(
        ["/usr/libexec/java_home"], capture_output=True, text=True, check=False
    )
    if res.returncode == 0 and res.stdout.strip():
        return res.stdout.strip()
    pytest.skip("No JAVA_HOME on host")
    return ""  # unreachable


def run_jni_wrap(
    bin_path: Path,
    backend: str,
    jar: Path,
    out_dir: Path,
    *,
    keep_package_prefix: bool = True,
    classpath: list[Path] | None = None,
) -> None:
    """Invoke jni-wrap and ensure it succeeds, capturing output on failure."""
    out_dir.mkdir(parents=True, exist_ok=True)
    cmd = [str(bin_path), backend, str(jar), str(out_dir)]
    if keep_package_prefix:
        cmd.append("--keep-package-prefix")
    for cp in classpath or []:
        cmd.extend(["--classpath", str(cp)])
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        raise RuntimeError(
            f"jni-wrap {backend} failed (exit {res.returncode}):\n"
            f"stdout:\n{res.stdout}\nstderr:\n{res.stderr}"
        )


def clean_dir(p: Path) -> None:
    if p.exists():
        shutil.rmtree(p)
    p.mkdir(parents=True)
