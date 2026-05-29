from typing import Any, ClassVar, overload
from java.lang.ClassLoader import ClassLoader

class PathClassLoader:
    @overload
    def __init__(self, p0: str, p1: ClassLoader) -> None: ...
    @overload
    def __init__(self, p0: str, p1: str, p2: ClassLoader) -> None: ...
