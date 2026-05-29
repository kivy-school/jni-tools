from typing import Any, ClassVar, overload
from java.lang.ClassLoader import ClassLoader
from java.nio.ByteBuffer import ByteBuffer

class InMemoryDexClassLoader:
    @overload
    def __init__(self, p0: ByteBuffer, p1: ClassLoader) -> None: ...
    @overload
    def __init__(self, p0: Any, p1: ClassLoader) -> None: ...
    @overload
    def __init__(self, p0: Any, p1: str, p2: ClassLoader) -> None: ...
