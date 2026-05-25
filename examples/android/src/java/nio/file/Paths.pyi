from typing import Any, ClassVar, overload
from java.net.URI import URI
from java.nio.file.Path import Path

class Paths:
    @overload
    @staticmethod
    def get(arg0: str, *arg1: str) -> Path: ...
    @overload
    @staticmethod
    def get(arg0: URI) -> Path: ...
