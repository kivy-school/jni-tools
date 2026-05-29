from typing import Any, ClassVar, overload

class GatheringByteChannel:
    @overload
    def write(self, p0: Any, p1: int, p2: int) -> int: ...
    @overload
    def write(self, p0: Any) -> int: ...
