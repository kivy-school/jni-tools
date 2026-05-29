from typing import Any, ClassVar, overload

class CursorIndexOutOfBoundsException:
    @overload
    def __init__(self, p0: int, p1: int) -> None: ...
    @overload
    def __init__(self, p0: str) -> None: ...
