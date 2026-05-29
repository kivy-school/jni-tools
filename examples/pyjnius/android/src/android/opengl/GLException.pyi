from typing import Any, ClassVar, overload

class GLException:
    @overload
    def __init__(self, p0: int) -> None: ...
    @overload
    def __init__(self, p0: int, p1: str) -> None: ...
