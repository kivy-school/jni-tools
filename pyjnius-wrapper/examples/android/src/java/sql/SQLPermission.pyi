from typing import Any, ClassVar, overload

class SQLPermission:
    @overload
    def __init__(self, arg0: str) -> None: ...
    @overload
    def __init__(self, arg0: str, arg1: str) -> None: ...
