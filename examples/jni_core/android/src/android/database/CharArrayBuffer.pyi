from typing import Any, ClassVar, overload

class CharArrayBuffer:
    data: Any
    sizeCopied: int
    @overload
    def __init__(self, p0: Any) -> None: ...
    @overload
    def __init__(self, p0: int) -> None: ...
