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
    def decode(p0: str, p1: int) -> Any: ...
    @overload
    @staticmethod
    def decode(p0: Any, p1: int, p2: int, p3: int) -> Any: ...
    @overload
    @staticmethod
    def decode(p0: Any, p1: int) -> Any: ...
    @overload
    @staticmethod
    def encode(p0: Any, p1: int, p2: int, p3: int) -> Any: ...
    @overload
    @staticmethod
    def encode(p0: Any, p1: int) -> Any: ...
    @overload
    @staticmethod
    def encodeToString(p0: Any, p1: int) -> str: ...
    @overload
    @staticmethod
    def encodeToString(p0: Any, p1: int, p2: int, p3: int) -> str: ...
