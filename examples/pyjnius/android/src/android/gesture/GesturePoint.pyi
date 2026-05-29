from typing import Any, ClassVar, overload

class GesturePoint:
    timestamp: int
    x: float
    y: float
    def __init__(self, p0: float, p1: float, p2: int) -> None: ...
    def clone(self) -> Any: ...
