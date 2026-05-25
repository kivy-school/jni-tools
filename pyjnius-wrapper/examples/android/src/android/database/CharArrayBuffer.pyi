from typing import Any, ClassVar, overload

class CharArrayBuffer:
    data: list[str]
    sizeCopied: int
    @overload
    def __init__(self, arg0: int) -> None: ...
    @overload
    def __init__(self, arg0: list[str]) -> None: ...
