from typing import Any, ClassVar, overload

class ParcelFormatException:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, p0: str) -> None: ...
