from typing import Any, ClassVar, overload

class Int3:
    x: int
    y: int
    z: int
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, arg0: int, arg1: int, arg2: int) -> None: ...
