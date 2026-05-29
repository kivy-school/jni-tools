from typing import Any, ClassVar, overload
from java.nio.file.attribute.FileAttribute import FileAttribute

class PosixFilePermissions:
    @staticmethod
    def toString(p0: set) -> str: ...
    @staticmethod
    def fromString(p0: str) -> set: ...
    @staticmethod
    def asFileAttribute(p0: set) -> FileAttribute: ...
