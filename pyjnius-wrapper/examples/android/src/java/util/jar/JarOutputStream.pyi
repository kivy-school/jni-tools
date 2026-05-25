from typing import Any, ClassVar, overload
from java.io.OutputStream import OutputStream
from java.util.jar.Manifest import Manifest
from java.util.zip.ZipEntry import ZipEntry

class JarOutputStream:
    CENATT: ClassVar[int]
    CENATX: ClassVar[int]
    CENCOM: ClassVar[int]
    CENCRC: ClassVar[int]
    CENDSK: ClassVar[int]
    CENEXT: ClassVar[int]
    CENFLG: ClassVar[int]
    CENHDR: ClassVar[int]
    CENHOW: ClassVar[int]
    CENLEN: ClassVar[int]
    CENNAM: ClassVar[int]
    CENOFF: ClassVar[int]
    CENSIG: ClassVar[int]
    CENSIZ: ClassVar[int]
    CENTIM: ClassVar[int]
    CENVEM: ClassVar[int]
    CENVER: ClassVar[int]
    ENDCOM: ClassVar[int]
    ENDHDR: ClassVar[int]
    ENDOFF: ClassVar[int]
    ENDSIG: ClassVar[int]
    ENDSIZ: ClassVar[int]
    ENDSUB: ClassVar[int]
    ENDTOT: ClassVar[int]
    EXTCRC: ClassVar[int]
    EXTHDR: ClassVar[int]
    EXTLEN: ClassVar[int]
    EXTSIG: ClassVar[int]
    EXTSIZ: ClassVar[int]
    LOCCRC: ClassVar[int]
    LOCEXT: ClassVar[int]
    LOCFLG: ClassVar[int]
    LOCHDR: ClassVar[int]
    LOCHOW: ClassVar[int]
    LOCLEN: ClassVar[int]
    LOCNAM: ClassVar[int]
    LOCSIG: ClassVar[int]
    LOCSIZ: ClassVar[int]
    LOCTIM: ClassVar[int]
    LOCVER: ClassVar[int]
    @overload
    def __init__(self, arg0: OutputStream, arg1: Manifest) -> None: ...
    @overload
    def __init__(self, arg0: OutputStream) -> None: ...
    def putNextEntry(self, arg0: ZipEntry) -> None: ...
