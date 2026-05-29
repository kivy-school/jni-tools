from typing import Any, ClassVar, overload

class LinkPermission:
    @overload
    def __init__(self, p0: str) -> None: ...
    @overload
    def __init__(self, p0: str, p1: str) -> None: ...
