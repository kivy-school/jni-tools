from typing import Any, ClassVar, overload

class Attributes:
    @overload
    def __init__(self, p0: "Attributes") -> None: ...
    @overload
    def __init__(self, p0: int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def remove(self, p0: Any) -> Any: ...
    def size(self) -> int: ...
    def get(self, p0: Any) -> Any: ...
    def put(self, p0: Any, p1: Any) -> Any: ...
    def equals(self, p0: Any) -> bool: ...
    def values(self) -> list: ...
    def hashCode(self) -> int: ...
    def clone(self) -> Any: ...
    def clear(self) -> None: ...
    @overload
    def getValue(self, p0: str) -> str: ...
    @overload
    def getValue(self, p0: Any) -> str: ...
    def isEmpty(self) -> bool: ...
    def entrySet(self) -> set: ...
    def putAll(self, p0: dict) -> None: ...
    def containsKey(self, p0: Any) -> bool: ...
    def keySet(self) -> set: ...
    def containsValue(self, p0: Any) -> bool: ...
    def putValue(self, p0: str, p1: str) -> str: ...

    class Name:
        MANIFEST_VERSION: ClassVar[Any]
        SIGNATURE_VERSION: ClassVar[Any]
        CONTENT_TYPE: ClassVar[Any]
        CLASS_PATH: ClassVar[Any]
        MAIN_CLASS: ClassVar[Any]
        SEALED: ClassVar[Any]
        EXTENSION_LIST: ClassVar[Any]
        EXTENSION_NAME: ClassVar[Any]
        EXTENSION_INSTALLATION: ClassVar[Any]
        IMPLEMENTATION_TITLE: ClassVar[Any]
        IMPLEMENTATION_VERSION: ClassVar[Any]
        IMPLEMENTATION_VENDOR: ClassVar[Any]
        IMPLEMENTATION_VENDOR_ID: ClassVar[Any]
        IMPLEMENTATION_URL: ClassVar[Any]
        SPECIFICATION_TITLE: ClassVar[Any]
        SPECIFICATION_VERSION: ClassVar[Any]
        SPECIFICATION_VENDOR: ClassVar[Any]
        MULTI_RELEASE: ClassVar[Any]
        def __init__(self, p0: str) -> None: ...
        def equals(self, p0: Any) -> bool: ...
        def toString(self) -> str: ...
        def hashCode(self) -> int: ...

from typing import Any, ClassVar, overload

class JarException:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, p0: str) -> None: ...

from typing import Any, ClassVar, overload
from java.io.InputStream import InputStream
from java.io.OutputStream import OutputStream
from java.util.jar.Attributes import Attributes

class Manifest:
    @overload
    def __init__(self, p0: "Manifest") -> None: ...
    @overload
    def __init__(self, p0: InputStream) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def equals(self, p0: Any) -> bool: ...
    def hashCode(self) -> int: ...
    def clone(self) -> Any: ...
    def clear(self) -> None: ...
    def write(self, p0: OutputStream) -> None: ...
    def read(self, p0: InputStream) -> None: ...
    def getMainAttributes(self) -> Attributes: ...
    def getEntries(self) -> dict: ...
    def getAttributes(self, p0: str) -> Attributes: ...

from typing import Any, ClassVar, overload
from java.util.jar.Attributes import Attributes
from java.util.zip.ZipEntry import ZipEntry

class JarEntry:
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
    def __init__(self, p0: "JarEntry") -> None: ...
    @overload
    def __init__(self, p0: ZipEntry) -> None: ...
    @overload
    def __init__(self, p0: str) -> None: ...
    def getCertificates(self) -> Any: ...
    def getRealName(self) -> str: ...
    def getCodeSigners(self) -> Any: ...
    def getAttributes(self) -> Attributes: ...

from typing import Any, ClassVar, overload
from java.io.InputStream import InputStream
from java.util.jar.JarEntry import JarEntry
from java.util.jar.Manifest import Manifest
from java.util.zip.ZipEntry import ZipEntry

class JarInputStream:
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
    def __init__(self, p0: InputStream) -> None: ...
    @overload
    def __init__(self, p0: InputStream, p1: bool) -> None: ...
    def getNextEntry(self) -> ZipEntry: ...
    def read(self, p0: Any, p1: int, p2: int) -> int: ...
    def getNextJarEntry(self) -> JarEntry: ...
    def getManifest(self) -> Manifest: ...

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
    def __init__(self, p0: File, p1: bool, p2: int, p3: Any) -> None: ...
    @overload
    def __init__(self, p0: File) -> None: ...
    @overload
    def __init__(self, p0: File, p1: bool) -> None: ...
    @overload
    def __init__(self, p0: File, p1: bool, p2: int) -> None: ...
    @overload
    def __init__(self, p0: str) -> None: ...
    @overload
    def __init__(self, p0: str, p1: bool) -> None: ...
    def isMultiRelease(self) -> bool: ...
    def getJarEntry(self, p0: str) -> JarEntry: ...
    @staticmethod
    def baseVersion() -> Any: ...
    def getVersion(self) -> Any: ...
    def versionedStream(self) -> Stream: ...
    def stream(self) -> Stream: ...
    def entries(self) -> Enumeration: ...
    def getEntry(self, p0: str) -> ZipEntry: ...
    def getInputStream(self, p0: ZipEntry) -> InputStream: ...
    def getManifest(self) -> Manifest: ...
    @staticmethod
    def runtimeVersion() -> Any: ...

from typing import Any, ClassVar, overload
from java.io.OutputStream import OutputStream
from java.util.jar.Manifest import Manifest
from java.util.zip.ZipEntry import ZipEntry

class JarOutputStream:
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
    def __init__(self, p0: OutputStream, p1: Manifest) -> None: ...
    @overload
    def __init__(self, p0: OutputStream) -> None: ...
    def putNextEntry(self, p0: ZipEntry) -> None: ...

