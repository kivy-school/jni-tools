from typing import Any, ClassVar, overload

class NegativeArraySizeException:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, arg0: str) -> None: ...
