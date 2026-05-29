from typing import Any, ClassVar, overload
from org.xml.sax.XMLReader import XMLReader

class XMLReaderFactory:
    @overload
    @staticmethod
    def createXMLReader() -> XMLReader: ...
    @overload
    @staticmethod
    def createXMLReader(arg0: str) -> XMLReader: ...
