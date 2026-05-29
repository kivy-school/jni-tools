from typing import Any, ClassVar, overload
from java.nio.file.Path import Path

class PathMatcher:
    def matches(self, p0: Path) -> bool: ...
