"""End-to-end test: jni-wrap cython backend (jni_core runtime) + Apache commons-csv on macOS desktop.

Uses the committed generated package at test-suite/packages/commons_csv_jni_core/.
Compiles Cython extensions once per session, then exercises the real generated API.
"""
from __future__ import annotations

import os
import subprocess
import sys
import sysconfig
from pathlib import Path

import pytest

from conftest import (
    CSV_EXPECTED_HEADERS,
    CSV_EXPECTED_ROW_COUNT,
)


HERE = Path(__file__).parent.resolve()
_JNI_CORE_PKG_DIR = HERE.parent / "packages" / "commons_csv_jni_core"


@pytest.fixture(scope="session")
def jni_core_pkg_install(tmp_path_factory, java_home):
    """Compile and install the committed jni_core package into a session-scoped prefix."""
    install_prefix = tmp_path_factory.mktemp("jni_core_install")
    env = os.environ.copy()
    env["JAVA_HOME"] = java_home
    res = subprocess.run(
        [
            sys.executable, "-m", "pip", "install",
            "--no-build-isolation",
            "--prefix", str(install_prefix),
            str(_JNI_CORE_PKG_DIR),
        ],
        env=env,
        capture_output=True,
        text=True,
    )
    if res.returncode != 0:
        raise RuntimeError(
            f"pip install failed (exit {res.returncode}):\n"
            f"stdout:\n{res.stdout}\nstderr:\n{res.stderr}"
        )
    purelib = Path(sysconfig.get_path("purelib", vars={"base": str(install_prefix), "platbase": str(install_prefix)}))
    platlib = Path(sysconfig.get_path("platlib", vars={"base": str(install_prefix), "platbase": str(install_prefix)}))
    for p in {str(purelib), str(platlib)}:
        if p not in sys.path:
            sys.path.insert(0, p)
    return install_prefix


def test_jni_core_wrapper_parses_commons_csv(
    jni_core_pkg_install,
    commons_csv_jar: Path,
    commons_io_jar: Path,
    commons_codec_jar: Path,
    csv_sample_path: Path,
    java_home: str,
) -> None:
    os.environ["JAVA_HOME"] = java_home

    import jnius_config
    if not jnius_config.vm_running:
        jnius_config.set_classpath(
            str(commons_csv_jar), str(commons_io_jar), str(commons_codec_jar)
        )
    from jnius import autoclass  # noqa: F401  — forces JVM start with classpath
    autoclass("java.lang.String")

    from commons_csv_jni_core.org.apache.commons.csv.CSVFormat import CSVFormat  # type: ignore
    from commons_csv_jni_core.org.apache.commons.csv.CSVParser import CSVParser  # type: ignore
    from commons_csv_jni_core.org.apache.commons.csv.CSVRecord import CSVRecord  # type: ignore
    from commons_csv_jni_core.java.util.Iterator import Iterator  # type: ignore

    content = csv_sample_path.read_text(encoding="utf-8")
    fmt = CSVFormat.DEFAULT()
    # parse_4 = overload (String, CSVFormat) — picked by index from the generated overload list
    parser = CSVParser.parse_4(content, fmt)
    try:
        it = Iterator.from_java_object(parser.iterator())
        records = []
        while it.hasNext():
            records.append(CSVRecord.from_java_object(it.next()))
    finally:
        parser.close()

    headers = [records[0].get(j) for j in range(records[0].size())]
    data_rows = records[1:]

    print(f"[jni_core] headers={headers} rows={len(data_rows)}", flush=True)
    assert sorted(headers) == sorted(CSV_EXPECTED_HEADERS)
    assert len(data_rows) == CSV_EXPECTED_ROW_COUNT

