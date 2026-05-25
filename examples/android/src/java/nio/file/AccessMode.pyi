from typing import Any, ClassVar, overload

class AccessMode:
    READ: ClassVar["AccessMode"]
    WRITE: ClassVar["AccessMode"]
    EXECUTE: ClassVar["AccessMode"]
    @staticmethod
    def values() -> list["AccessMode"]: ...
    @staticmethod
    def valueOf(arg0: str) -> "AccessMode": ...
