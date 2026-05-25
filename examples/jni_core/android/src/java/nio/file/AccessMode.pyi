from typing import Any, ClassVar, overload

class AccessMode:
    READ: ClassVar["AccessMode"]
    WRITE: ClassVar["AccessMode"]
    EXECUTE: ClassVar["AccessMode"]
    READ: ClassVar["AccessMode"]
    WRITE: ClassVar["AccessMode"]
    EXECUTE: ClassVar["AccessMode"]
    @staticmethod
    def values() -> Any: ...
    @staticmethod
    def valueOf(p0: str) -> "AccessMode": ...
