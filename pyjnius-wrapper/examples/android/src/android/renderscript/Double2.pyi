from typing import Any, ClassVar, overload

class Double2:
    x: float
    y: float
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, arg0: float, arg1: float) -> None: ...
