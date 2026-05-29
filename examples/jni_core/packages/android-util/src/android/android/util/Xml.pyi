from typing import Any, ClassVar, overload
from android.util.AttributeSet import AttributeSet
from java.io.InputStream import InputStream
from java.io.Reader import Reader
from org.xml.sax.ContentHandler import ContentHandler
from org.xmlpull.v1.XmlPullParser import XmlPullParser
from org.xmlpull.v1.XmlSerializer import XmlSerializer

class Xml:
    FEATURE_RELAXED: ClassVar[str]
    @staticmethod
    def newPullParser() -> XmlPullParser: ...
    @staticmethod
    def newSerializer() -> XmlSerializer: ...
    @staticmethod
    def findEncodingByName(p0: str) -> Any: ...
    @staticmethod
    def asAttributeSet(p0: XmlPullParser) -> AttributeSet: ...
    @overload
    @staticmethod
    def parse(p0: InputStream, p1: Any, p2: ContentHandler) -> None: ...
    @overload
    @staticmethod
    def parse(p0: str, p1: ContentHandler) -> None: ...
    @overload
    @staticmethod
    def parse(p0: Reader, p1: ContentHandler) -> None: ...

    class Encoding:
        US_ASCII: ClassVar["Encoding"]
        UTF_8: ClassVar["Encoding"]
        UTF_16: ClassVar["Encoding"]
        ISO_8859_1: ClassVar["Encoding"]
        US_ASCII: ClassVar[Any]
        UTF_8: ClassVar[Any]
        UTF_16: ClassVar[Any]
        ISO_8859_1: ClassVar[Any]
        @staticmethod
        def values() -> Any: ...
        @staticmethod
        def valueOf(p0: str) -> Any: ...
