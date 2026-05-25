from typing import Any, ClassVar, overload

class RowIdLifetime:
    ROWID_UNSUPPORTED: ClassVar["RowIdLifetime"]
    ROWID_VALID_OTHER: ClassVar["RowIdLifetime"]
    ROWID_VALID_SESSION: ClassVar["RowIdLifetime"]
    ROWID_VALID_TRANSACTION: ClassVar["RowIdLifetime"]
    ROWID_VALID_FOREVER: ClassVar["RowIdLifetime"]
    @staticmethod
    def values() -> list["RowIdLifetime"]: ...
    @staticmethod
    def valueOf(arg0: str) -> "RowIdLifetime": ...
