"""End-to-end test: jni-wrap pyjnius backend + Apache commons-csv on macOS desktop.

Uses the committed generated package at test-suite/packages/commons_csv_pyjnius/.
"""
from __future__ import annotations

import os
import sys
from pathlib import Path

from conftest import (
    CSV_EXPECTED_HEADERS,
    CSV_EXPECTED_ROW_COUNT,
)


HERE = Path(__file__).parent.resolve()
_PYJNIUS_PKG_SRC = HERE.parent / "packages" / "commons_csv_pyjnius" / "src"


def _ensure_on_syspath() -> None:
    src = str(_PYJNIUS_PKG_SRC)
    if src not in sys.path:
        sys.path.insert(0, src)


def test_pyjnius_wrapper_parses_commons_csv(
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

    _ensure_on_syspath()

    from commons_csv_pyjnius.org.apache.commons.csv.CSVFormat import CSVFormat  # type: ignore
    from commons_csv_pyjnius.org.apache.commons.csv.CSVParser import CSVParser  # type: ignore

    # Read in Python — pyjnius auto-converts Python str to java.lang.String
    # for the CSVParser.parse(String, CSVFormat) overload.
    content = csv_sample_path.read_text(encoding="utf-8")
    fmt = CSVFormat.DEFAULT
    parser = CSVParser.parse(content, fmt)
    try:
        record_list = parser.getRecords()  # java.util.List<CSVRecord>
        size = record_list.size()
        records = [record_list.get(i) for i in range(size)]
        headers = [str(records[0].get(j)) for j in range(records[0].size())]
        data_rows = records[1:]
    finally:
        parser.close()

    print(f"[pyjnius] headers={headers} rows={len(data_rows)}", flush=True)
    assert sorted(headers) == sorted(CSV_EXPECTED_HEADERS)
    assert len(data_rows) == CSV_EXPECTED_ROW_COUNT
