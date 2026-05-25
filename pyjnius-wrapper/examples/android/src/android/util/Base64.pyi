from typing import Any, ClassVar, overload

class Base64:
    CRLF: ClassVar[int]
    DEFAULT: ClassVar[int]
    NO_CLOSE: ClassVar[int]
    NO_PADDING: ClassVar[int]
    NO_WRAP: ClassVar[int]
    URL_SAFE: ClassVar[int]
    @overload
    @staticmethod
    def decode(arg0: str, arg1: int) -> list[int]: ...
    @overload
    @staticmethod
    def decode(arg0: list[int], arg1: int) -> list[int]: ...
    @overload
    @staticmethod
    def decode(arg0: list[int], arg1: int, arg2: int, arg3: int) -> list[int]: ...
    @overload
    @staticmethod
    def encodeToString(arg0: list[int], arg1: int) -> str: ...
    @overload
    @staticmethod
    def encodeToString(arg0: list[int], arg1: int, arg2: int, arg3: int) -> str: ...
    @overload
    @staticmethod
    def encode(arg0: list[int], arg1: int) -> list[int]: ...
    @overload
    @staticmethod
    def encode(arg0: list[int], arg1: int, arg2: int, arg3: int) -> list[int]: ...
