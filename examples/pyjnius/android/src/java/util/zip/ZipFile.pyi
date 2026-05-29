from typing import Any, ClassVar, overload
from java.io.File import File
from java.io.InputStream import InputStream
from java.nio.charset.Charset import Charset
from java.util.Enumeration import Enumeration
from java.util.stream.Stream import Stream
from java.util.zip.ZipEntry import ZipEntry

class ZipFile:
    OPEN_READ: ClassVar[int]
    OPEN_DELETE: ClassVar[int]
    LOCSIG: ClassVar[int]
    EXTSIG: ClassVar[int]
    CENSIG: ClassVar[int]
    ENDSIG: ClassVar[int]
    LOCHDR: ClassVar[int]
    EXTHDR: ClassVar[int]
    CENHDR: ClassVar[int]
    ENDHDR: ClassVar[int]
    LOCVER: ClassVar[int]
    LOCFLG: ClassVar[int]
    LOCHOW: ClassVar[int]
    LOCTIM: ClassVar[int]
    LOCCRC: ClassVar[int]
    LOCSIZ: ClassVar[int]
    LOCLEN: ClassVar[int]
    LOCNAM: ClassVar[int]
    LOCEXT: ClassVar[int]
    EXTCRC: ClassVar[int]
    EXTSIZ: ClassVar[int]
    EXTLEN: ClassVar[int]
    CENVEM: ClassVar[int]
    CENVER: ClassVar[int]
    CENFLG: ClassVar[int]
    CENHOW: ClassVar[int]
    CENTIM: ClassVar[int]
    CENCRC: ClassVar[int]
    CENSIZ: ClassVar[int]
    CENLEN: ClassVar[int]
    CENNAM: ClassVar[int]
    CENEXT: ClassVar[int]
    CENCOM: ClassVar[int]
    CENDSK: ClassVar[int]
    CENATT: ClassVar[int]
    CENATX: ClassVar[int]
    CENOFF: ClassVar[int]
    ENDSUB: ClassVar[int]
    ENDTOT: ClassVar[int]
    ENDSIZ: ClassVar[int]
    ENDOFF: ClassVar[int]
    ENDCOM: ClassVar[int]
    @overload
    def __init__(self, p0: str, p1: Charset) -> None: ...
    @overload
    def __init__(self, p0: File, p1: Charset) -> None: ...
    @overload
    def __init__(self, p0: str) -> None: ...
    @overload
    def __init__(self, p0: File, p1: int) -> None: ...
    @overload
    def __init__(self, p0: File) -> None: ...
    @overload
    def __init__(self, p0: File, p1: int, p2: Charset) -> None: ...
    def getName(self) -> str: ...
    def size(self) -> int: ...
    def toString(self) -> str: ...
    def stream(self) -> Stream: ...
    def close(self) -> None: ...
    def entries(self) -> Enumeration: ...
    def getInputStream(self, p0: ZipEntry) -> InputStream: ...
    def getComment(self) -> str: ...
    def getEntry(self, p0: str) -> ZipEntry: ...
