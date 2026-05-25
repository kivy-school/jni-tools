from typing import Any, ClassVar, overload
from java.nio.charset.Charset import Charset

class URLEncoder:
    @overload
    @staticmethod
    def encode(p0: str) -> str: ...
    @overload
    @staticmethod
    def encode(p0: str, p1: Charset) -> str: ...
    @overload
    @staticmethod
    def encode(p0: str, p1: str) -> str: ...
