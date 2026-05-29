from typing import Any, ClassVar, overload
from java.util.Locale import Locale

class DateKeyListener:
    CHARACTERS: ClassVar[Any]
    META_ALT_LOCKED: ClassVar[int]
    META_ALT_ON: ClassVar[int]
    META_CAP_LOCKED: ClassVar[int]
    META_SHIFT_ON: ClassVar[int]
    META_SYM_LOCKED: ClassVar[int]
    META_SYM_ON: ClassVar[int]
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, p0: Locale) -> None: ...
    @overload
    @staticmethod
    def getInstance() -> "DateKeyListener": ...
    @overload
    @staticmethod
    def getInstance(p0: Locale) -> "DateKeyListener": ...
    def getInputType(self) -> int: ...
