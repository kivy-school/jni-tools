from typing import Any, ClassVar, overload

class Byte2:
    x: int
    y: int
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, p0: int, p1: int) -> None: ...
