from typing import Any, ClassVar, overload

class ByteOrder:
    BIG_ENDIAN: ClassVar["ByteOrder"]
    LITTLE_ENDIAN: ClassVar["ByteOrder"]
    @staticmethod
    def nativeOrder() -> "ByteOrder": ...
    def toString(self) -> str: ...
