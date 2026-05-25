from typing import Any, ClassVar, overload

class IDN:
    ALLOW_UNASSIGNED: ClassVar[int]
    USE_STD3_ASCII_RULES: ClassVar[int]
    @overload
    @staticmethod
    def toASCII(arg0: str, arg1: int) -> str: ...
    @overload
    @staticmethod
    def toASCII(arg0: str) -> str: ...
    @overload
    @staticmethod
    def toUnicode(arg0: str, arg1: int) -> str: ...
    @overload
    @staticmethod
    def toUnicode(arg0: str) -> str: ...
