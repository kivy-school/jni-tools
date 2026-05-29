from typing import Any, ClassVar, overload
from java.lang.ClassLoader import ClassLoader
from java.net.URI import URI
from java.nio.file.FileSystem import FileSystem
from java.nio.file.Path import Path

class FileSystems:
    @staticmethod
    def getDefault() -> FileSystem: ...
    @staticmethod
    def getFileSystem(p0: URI) -> FileSystem: ...
    @overload
    @staticmethod
    def newFileSystem(p0: Path, p1: dict) -> FileSystem: ...
    @overload
    @staticmethod
    def newFileSystem(p0: Path) -> FileSystem: ...
    @overload
    @staticmethod
    def newFileSystem(p0: Path, p1: dict, p2: ClassLoader) -> FileSystem: ...
    @overload
    @staticmethod
    def newFileSystem(p0: Path, p1: ClassLoader) -> FileSystem: ...
    @overload
    @staticmethod
    def newFileSystem(p0: URI, p1: dict, p2: ClassLoader) -> FileSystem: ...
    @overload
    @staticmethod
    def newFileSystem(p0: URI, p1: dict) -> FileSystem: ...
