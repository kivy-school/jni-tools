from typing import Any, ClassVar, overload
from java.io.File import File

class FilenameFilter:
    def accept(self, p0: File, p1: str) -> bool: ...
