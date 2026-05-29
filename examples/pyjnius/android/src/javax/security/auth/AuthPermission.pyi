from typing import Any, ClassVar, overload

class AuthPermission:
    @overload
    def __init__(self, p0: str) -> None: ...
    @overload
    def __init__(self, p0: str, p1: str) -> None: ...
