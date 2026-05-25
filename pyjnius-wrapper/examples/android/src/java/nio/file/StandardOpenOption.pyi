from typing import Any, ClassVar, overload

class StandardOpenOption:
    READ: ClassVar["StandardOpenOption"]
    WRITE: ClassVar["StandardOpenOption"]
    APPEND: ClassVar["StandardOpenOption"]
    TRUNCATE_EXISTING: ClassVar["StandardOpenOption"]
    CREATE: ClassVar["StandardOpenOption"]
    CREATE_NEW: ClassVar["StandardOpenOption"]
    DELETE_ON_CLOSE: ClassVar["StandardOpenOption"]
    SPARSE: ClassVar["StandardOpenOption"]
    SYNC: ClassVar["StandardOpenOption"]
    DSYNC: ClassVar["StandardOpenOption"]
    @staticmethod
    def values() -> list["StandardOpenOption"]: ...
    @staticmethod
    def valueOf(arg0: str) -> "StandardOpenOption": ...
