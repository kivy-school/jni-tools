from typing import Any, ClassVar, overload
from java.nio.charset.Charset import Charset

class URLDecoder:
    def __init__(self) -> None: ...
    @overload
    @staticmethod
    def decode(arg0: str) -> str: ...
    @overload
    @staticmethod
    def decode(arg0: str, arg1: str) -> str: ...
    @overload
    @staticmethod
    def decode(arg0: str, arg1: Charset) -> str: ...
