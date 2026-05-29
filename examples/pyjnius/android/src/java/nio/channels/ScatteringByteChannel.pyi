from typing import Any, ClassVar, overload

class ScatteringByteChannel:
    @overload
    def read(self, p0: Any, p1: int, p2: int) -> int: ...
    @overload
    def read(self, p0: Any) -> int: ...
