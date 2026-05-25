from typing import Any, ClassVar, overload
from java.nio.charset.Charset import Charset

class URLEncoder:
    @overload
    @staticmethod
    def encode(arg0: str) -> str: ...
    @overload
    @staticmethod
    def encode(arg0: str, arg1: str) -> str: ...
    @overload
    @staticmethod
    def encode(arg0: str, arg1: Charset) -> str: ...
