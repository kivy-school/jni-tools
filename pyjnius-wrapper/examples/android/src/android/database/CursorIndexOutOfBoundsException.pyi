from typing import Any, ClassVar, overload

class CursorIndexOutOfBoundsException:
    @overload
    def __init__(self, arg0: int, arg1: int) -> None: ...
    @overload
    def __init__(self, arg0: str) -> None: ...
