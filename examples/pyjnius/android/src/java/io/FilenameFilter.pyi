from typing import Any, ClassVar, overload
from java.io.File import File

class FilenameFilter:
    def accept(self, arg0: File, arg1: str) -> bool: ...
