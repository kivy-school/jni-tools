from typing import Any, ClassVar, overload

class Float4:
    w: float
    x: float
    y: float
    z: float
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, arg0: float, arg1: float, arg2: float, arg3: float) -> None: ...
