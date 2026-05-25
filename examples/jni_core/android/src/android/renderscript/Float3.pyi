from typing import Any, ClassVar, overload

class Float3:
    x: float
    y: float
    z: float
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, p0: float, p1: float, p2: float) -> None: ...
