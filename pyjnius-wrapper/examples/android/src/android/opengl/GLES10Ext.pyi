from typing import Any, ClassVar, overload
from java.nio.IntBuffer import IntBuffer

class GLES10Ext:
    def __init__(self) -> None: ...
    @overload
    @staticmethod
    def glQueryMatrixxOES(arg0: list[int], arg1: int, arg2: list[int], arg3: int) -> int: ...
    @overload
    @staticmethod
    def glQueryMatrixxOES(arg0: IntBuffer, arg1: IntBuffer) -> int: ...
