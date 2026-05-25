from typing import Any, ClassVar, overload
from java.io.File import File
from java.io.InputStream import InputStream
from java.util.Enumeration import Enumeration
from java.util.jar.JarEntry import JarEntry
from java.util.jar.Manifest import Manifest
from java.util.stream.Stream import Stream
from java.util.zip.ZipEntry import ZipEntry

class JarFile:
    MANIFEST_NAME: ClassVar[str]
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
    def __init__(self, p0: File, p1: bool) -> None: ...
    @overload
    def __init__(self, p0: File) -> None: ...
    @overload
    def __init__(self, p0: str, p1: bool) -> None: ...
    @overload
    def __init__(self, p0: str) -> None: ...
    @overload
    def __init__(self, p0: File, p1: bool, p2: int) -> None: ...
    @overload
    def __init__(self, p0: File, p1: bool, p2: int, p3: Any) -> None: ...
    def getInputStream(self, p0: ZipEntry) -> InputStream: ...
    def getManifest(self) -> Manifest: ...
    def getEntry(self, p0: str) -> ZipEntry: ...
    def isMultiRelease(self) -> bool: ...
    def getJarEntry(self, p0: str) -> JarEntry: ...
    @staticmethod
    def baseVersion() -> Any: ...
    def getVersion(self) -> Any: ...
    def versionedStream(self) -> Stream: ...
    @staticmethod
    def runtimeVersion() -> Any: ...
    def stream(self) -> Stream: ...
    def entries(self) -> Enumeration: ...
