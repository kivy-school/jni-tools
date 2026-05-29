from typing import Any, ClassVar, overload

class Double2:
    x: float
    y: float
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, p0: float, p1: float) -> None: ...
