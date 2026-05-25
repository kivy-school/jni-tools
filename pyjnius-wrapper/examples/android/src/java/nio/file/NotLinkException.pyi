from typing import Any, ClassVar, overload

class NotLinkException:
    @overload
    def __init__(self, arg0: str) -> None: ...
    @overload
    def __init__(self, arg0: str, arg1: str, arg2: str) -> None: ...
