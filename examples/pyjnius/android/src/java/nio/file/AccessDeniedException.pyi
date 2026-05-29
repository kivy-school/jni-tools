from typing import Any, ClassVar, overload

class AccessDeniedException:
    @overload
    def __init__(self, p0: str) -> None: ...
    @overload
    def __init__(self, p0: str, p1: str, p2: str) -> None: ...
