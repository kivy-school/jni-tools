from typing import Any, ClassVar, overload
from java.beans.PropertyChangeListener import PropertyChangeListener
from java.io.File import File
from java.io.InputStream import InputStream
from java.io.OutputStream import OutputStream
from java.util.SortedMap import SortedMap
from java.util.jar.JarFile import JarFile
from java.util.jar.JarInputStream import JarInputStream
from java.util.jar.JarOutputStream import JarOutputStream

class Pack200:
    @staticmethod
    def newPacker() -> "Packer": ...
    @staticmethod
    def newUnpacker() -> "Unpacker": ...

    class Packer:
        CLASS_ATTRIBUTE_PFX: ClassVar[str]
        CODE_ATTRIBUTE_PFX: ClassVar[str]
        DEFLATE_HINT: ClassVar[str]
        EFFORT: ClassVar[str]
        ERROR: ClassVar[str]
        FALSE: ClassVar[str]
        FIELD_ATTRIBUTE_PFX: ClassVar[str]
        KEEP: ClassVar[str]
        KEEP_FILE_ORDER: ClassVar[str]
        LATEST: ClassVar[str]
        METHOD_ATTRIBUTE_PFX: ClassVar[str]
        MODIFICATION_TIME: ClassVar[str]
        PASS: ClassVar[str]
        PASS_FILE_PFX: ClassVar[str]
        PROGRESS: ClassVar[str]
        SEGMENT_LIMIT: ClassVar[str]
        STRIP: ClassVar[str]
        TRUE: ClassVar[str]
        UNKNOWN_ATTRIBUTE: ClassVar[str]
        def properties(self) -> SortedMap: ...
        @overload
        def pack(self, arg0: JarFile, arg1: OutputStream) -> None: ...
        @overload
        def pack(self, arg0: JarInputStream, arg1: OutputStream) -> None: ...
        def addPropertyChangeListener(self, arg0: PropertyChangeListener) -> None: ...
        def removePropertyChangeListener(self, arg0: PropertyChangeListener) -> None: ...

    class Unpacker:
        DEFLATE_HINT: ClassVar[str]
        FALSE: ClassVar[str]
        KEEP: ClassVar[str]
        PROGRESS: ClassVar[str]
        TRUE: ClassVar[str]
        def properties(self) -> SortedMap: ...
        @overload
        def unpack(self, arg0: InputStream, arg1: JarOutputStream) -> None: ...
        @overload
        def unpack(self, arg0: File, arg1: JarOutputStream) -> None: ...
        def addPropertyChangeListener(self, arg0: PropertyChangeListener) -> None: ...
        def removePropertyChangeListener(self, arg0: PropertyChangeListener) -> None: ...
