from typing import Any, ClassVar, overload
from java.nio.file.attribute.FileAttribute import FileAttribute

class PosixFilePermissions:
    @staticmethod
    def toString(arg0: set) -> str: ...
    @staticmethod
    def fromString(arg0: str) -> set: ...
    @staticmethod
    def asFileAttribute(arg0: set) -> FileAttribute: ...
