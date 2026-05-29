from typing import Any, ClassVar, overload
from android.icu.text.Replaceable import Replaceable

class UnicodeFilter:
    ETHER: ClassVar[str]
    U_MATCH: ClassVar[int]
    U_MISMATCH: ClassVar[int]
    U_PARTIAL_MATCH: ClassVar[int]
    def matches(self, p0: Replaceable, p1: Any, p2: int, p3: bool) -> int: ...
    def contains(self, p0: int) -> bool: ...
