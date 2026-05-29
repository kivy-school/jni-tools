from typing import Any, ClassVar, overload

class PortUnreachableException:
    @overload
    def __init__(self, p0: str) -> None: ...
    @overload
    def __init__(self) -> None: ...
