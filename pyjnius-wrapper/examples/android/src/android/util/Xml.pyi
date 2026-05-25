from typing import Any, ClassVar, overload
from android.util.AttributeSet import AttributeSet
from java.io.InputStream import InputStream
from java.io.Reader import Reader
from org.xml.sax.ContentHandler import ContentHandler
from org.xmlpull.v1.XmlPullParser import XmlPullParser
from org.xmlpull.v1.XmlSerializer import XmlSerializer

class Xml:
    FEATURE_RELAXED: ClassVar[str]
    @overload
    @staticmethod
    def parse(arg0: str, arg1: ContentHandler) -> None: ...
    @overload
    @staticmethod
    def parse(arg0: Reader, arg1: ContentHandler) -> None: ...
    @overload
    @staticmethod
    def parse(arg0: InputStream, arg1: "Encoding", arg2: ContentHandler) -> None: ...
    @staticmethod
    def newPullParser() -> XmlPullParser: ...
    @staticmethod
    def newSerializer() -> XmlSerializer: ...
    @staticmethod
    def findEncodingByName(arg0: str) -> "Encoding": ...
    @staticmethod
    def asAttributeSet(arg0: XmlPullParser) -> AttributeSet: ...

    class Encoding:
        US_ASCII: ClassVar["Encoding"]
        UTF_8: ClassVar["Encoding"]
        UTF_16: ClassVar["Encoding"]
        ISO_8859_1: ClassVar["Encoding"]
        @staticmethod
        def values() -> list["Encoding"]: ...
        @staticmethod
        def valueOf(arg0: str) -> "Encoding": ...
