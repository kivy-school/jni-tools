from typing import Any, ClassVar, overload
from java.io.File import File

class FileFilter:
    def accept(self, arg0: File) -> bool: ...
