from typing import Any, ClassVar, overload
from java.io.File import File

class FileFilter:
    def accept(self, p0: File) -> bool: ...
