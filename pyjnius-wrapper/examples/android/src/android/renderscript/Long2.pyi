from typing import Any, ClassVar, overload

class Long2:
    x: int
    y: int
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, arg0: int, arg1: int) -> None: ...
