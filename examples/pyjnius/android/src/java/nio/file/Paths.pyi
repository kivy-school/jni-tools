from typing import Any, ClassVar, overload
from java.net.URI import URI
from java.nio.file.Path import Path

class Paths:
    @overload
    @staticmethod
    def get(p0: str, p1: Any) -> Path: ...
    @overload
    @staticmethod
    def get(p0: URI) -> Path: ...
