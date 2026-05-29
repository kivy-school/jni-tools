from typing import Any, ClassVar, overload

class Short3:
    x: int
    y: int
    z: int
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, p0: int, p1: int, p2: int) -> None: ...
