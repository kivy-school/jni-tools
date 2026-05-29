from typing import Any, ClassVar, overload

class TextDirectionHeuristic:
    @overload
    def isRtl(self, arg0: list[str], arg1: int, arg2: int) -> bool: ...
    @overload
    def isRtl(self, arg0: str, arg1: int, arg2: int) -> bool: ...
