from typing import Any, ClassVar, overload

class GesturePoint:
    timestamp: int
    x: float
    y: float
    def __init__(self, arg0: float, arg1: float, arg2: int) -> None: ...
    def clone(self) -> Any: ...
