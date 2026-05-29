from typing import Any, ClassVar, overload
from org.xml.sax.Parser import Parser

class ParserFactory:
    @overload
    @staticmethod
    def makeParser() -> Parser: ...
    @overload
    @staticmethod
    def makeParser(p0: str) -> Parser: ...
