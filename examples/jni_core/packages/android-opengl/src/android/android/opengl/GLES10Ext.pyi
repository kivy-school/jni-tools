from typing import Any, ClassVar, overload
from java.nio.IntBuffer import IntBuffer

class GLES10Ext:
    def __init__(self) -> None: ...
    @overload
    @staticmethod
    def glQueryMatrixxOES(p0: Any, p1: int, p2: Any, p3: int) -> int: ...
    @overload
    @staticmethod
    def glQueryMatrixxOES(p0: IntBuffer, p1: IntBuffer) -> int: ...
