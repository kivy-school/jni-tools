from typing import Any, ClassVar, overload

class GLException:
    @overload
    def __init__(self, arg0: int) -> None: ...
    @overload
    def __init__(self, arg0: int, arg1: str) -> None: ...
