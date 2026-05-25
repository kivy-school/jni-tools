from typing import Any, ClassVar, overload
from java.lang.ClassLoader import ClassLoader
from java.nio.ByteBuffer import ByteBuffer

class InMemoryDexClassLoader:
    @overload
    def __init__(self, arg0: list[ByteBuffer], arg1: str, arg2: ClassLoader) -> None: ...
    @overload
    def __init__(self, arg0: list[ByteBuffer], arg1: ClassLoader) -> None: ...
    @overload
    def __init__(self, arg0: ByteBuffer, arg1: ClassLoader) -> None: ...
