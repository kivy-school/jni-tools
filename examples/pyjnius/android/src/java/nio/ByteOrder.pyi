from typing import Any, ClassVar, overload

class ByteOrder:
    LITTLE_ENDIAN: ClassVar["ByteOrder"]
    BIG_ENDIAN: ClassVar["ByteOrder"]
    LITTLE_ENDIAN: ClassVar["ByteOrder"]
    BIG_ENDIAN: ClassVar["ByteOrder"]
    @staticmethod
    def values() -> Any: ...
    @staticmethod
    def valueOf(p0: str) -> "ByteOrder": ...
    @staticmethod
    def nativeOrder() -> "ByteOrder": ...
