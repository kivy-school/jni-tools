from typing import Any, ClassVar, overload

class DialerKeyListener:
    CHARACTERS: ClassVar[Any]
    META_ALT_LOCKED: ClassVar[int]
    META_ALT_ON: ClassVar[int]
    META_CAP_LOCKED: ClassVar[int]
    META_SHIFT_ON: ClassVar[int]
    META_SYM_LOCKED: ClassVar[int]
    META_SYM_ON: ClassVar[int]
    def __init__(self) -> None: ...
    def getInputType(self) -> int: ...
    @staticmethod
    def getInstance() -> "DialerKeyListener": ...
