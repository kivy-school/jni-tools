from typing import Any, ClassVar, overload
from java.lang.ClassLoader import ClassLoader
from java.net.URI import URI
from java.nio.file.FileSystem import FileSystem
from java.nio.file.Path import Path

class FileSystems:
    @staticmethod
    def getDefault() -> FileSystem: ...
    @staticmethod
    def getFileSystem(arg0: URI) -> FileSystem: ...
    @overload
    @staticmethod
    def newFileSystem(arg0: URI, arg1: dict) -> FileSystem: ...
    @overload
    @staticmethod
    def newFileSystem(arg0: URI, arg1: dict, arg2: ClassLoader) -> FileSystem: ...
    @overload
    @staticmethod
    def newFileSystem(arg0: Path, arg1: ClassLoader) -> FileSystem: ...
