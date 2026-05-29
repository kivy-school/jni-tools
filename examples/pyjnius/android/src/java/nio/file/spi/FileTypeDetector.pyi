from typing import Any, ClassVar, overload
from java.nio.file.Path import Path

class FileTypeDetector:
    def probeContentType(self, p0: Path) -> str: ...
