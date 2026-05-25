from typing import Any, ClassVar, overload
from java.nio.IntBuffer import IntBuffer

class GL10Ext:
    @overload
    def glQueryMatrixxOES(self, arg0: list[int], arg1: int, arg2: list[int], arg3: int) -> int: ...
    @overload
    def glQueryMatrixxOES(self, arg0: IntBuffer, arg1: IntBuffer) -> int: ...
