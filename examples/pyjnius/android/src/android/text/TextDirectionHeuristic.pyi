from typing import Any, ClassVar, overload

class TextDirectionHeuristic:
    @overload
    def isRtl(self, p0: Any, p1: int, p2: int) -> bool: ...
    @overload
    def isRtl(self, p0: str, p1: int, p2: int) -> bool: ...
