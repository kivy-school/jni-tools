from typing import Any, ClassVar, overload
from java.nio.IntBuffer import IntBuffer

class GL10Ext:
    @overload
    def glQueryMatrixxOES(self, p0: Any, p1: int, p2: Any, p3: int) -> int: ...
    @overload
    def glQueryMatrixxOES(self, p0: IntBuffer, p1: IntBuffer) -> int: ...
