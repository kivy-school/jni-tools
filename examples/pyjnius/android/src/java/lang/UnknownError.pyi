from typing import Any, ClassVar, overload

class UnknownError:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, arg0: str) -> None: ...
