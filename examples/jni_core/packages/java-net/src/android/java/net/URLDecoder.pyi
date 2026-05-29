from typing import Any, ClassVar, overload
from java.nio.charset.Charset import Charset

class URLDecoder:
    @overload
    @staticmethod
    def decode(p0: str, p1: Charset) -> str: ...
    @overload
    @staticmethod
    def decode(p0: str, p1: str) -> str: ...
    @overload
    @staticmethod
    def decode(p0: str) -> str: ...
