from typing import Any, ClassVar, overload
from java.nio.ByteBuffer import ByteBuffer

class GatheringByteChannel:
    @overload
    def write(self, arg0: list[ByteBuffer], arg1: int, arg2: int) -> int: ...
    @overload
    def write(self, arg0: list[ByteBuffer]) -> int: ...
