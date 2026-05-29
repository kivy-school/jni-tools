from typing import Any, ClassVar, overload
from java.io.OutputStream import OutputStream
from java.nio.charset.Charset import Charset
from java.util.zip.ZipEntry import ZipEntry

class ZipOutputStream:
    STORED: ClassVar[int]
    DEFLATED: ClassVar[int]
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
    def __init__(self, p0: OutputStream, p1: Charset) -> None: ...
    @overload
    def __init__(self, p0: OutputStream) -> None: ...
    def write(self, p0: Any, p1: int, p2: int) -> None: ...
    def close(self) -> None: ...
    def putNextEntry(self, p0: ZipEntry) -> None: ...
    def finish(self) -> None: ...
    def setLevel(self, p0: int) -> None: ...
    def setMethod(self, p0: int) -> None: ...
    def setComment(self, p0: str) -> None: ...
    def closeEntry(self) -> None: ...
