from typing import Any, ClassVar, overload
from java.lang.ClassLoader import ClassLoader

class PathClassLoader:
    @overload
    def __init__(self, arg0: str, arg1: ClassLoader) -> None: ...
    @overload
    def __init__(self, arg0: str, arg1: str, arg2: ClassLoader) -> None: ...
