from typing import Any, ClassVar, overload
from java.io.File import File
from java.io.InputStream import InputStream
from java.util.Enumeration import Enumeration
from java.util.jar.JarEntry import JarEntry
from java.util.jar.Manifest import Manifest
from java.util.stream.Stream import Stream
from java.util.zip.ZipEntry import ZipEntry

class JarFile:
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
    MANIFEST_NAME: ClassVar[str]
    @overload
    def __init__(self, arg0: str) -> None: ...
    @overload
    def __init__(self, arg0: str, arg1: bool) -> None: ...
    @overload
    def __init__(self, arg0: File) -> None: ...
    @overload
    def __init__(self, arg0: File, arg1: bool) -> None: ...
    @overload
    def __init__(self, arg0: File, arg1: bool, arg2: int) -> None: ...
    def getManifest(self) -> Manifest: ...
    def getJarEntry(self, arg0: str) -> JarEntry: ...
    def getEntry(self, arg0: str) -> ZipEntry: ...
    def entries(self) -> Enumeration: ...
    def stream(self) -> Stream: ...
    def getInputStream(self, arg0: ZipEntry) -> InputStream: ...
