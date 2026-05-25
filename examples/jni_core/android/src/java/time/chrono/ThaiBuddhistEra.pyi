from typing import Any, ClassVar, overload
from java.time.format.TextStyle import TextStyle
from java.util.Locale import Locale

class ThaiBuddhistEra:
    BEFORE_BE: ClassVar["ThaiBuddhistEra"]
    BE: ClassVar["ThaiBuddhistEra"]
    BEFORE_BE: ClassVar["ThaiBuddhistEra"]
    BE: ClassVar["ThaiBuddhistEra"]
    def getDisplayName(self, p0: TextStyle, p1: Locale) -> str: ...
    @staticmethod
    def values() -> Any: ...
    @staticmethod
    def valueOf(p0: str) -> "ThaiBuddhistEra": ...
    def getValue(self) -> int: ...
    @staticmethod
    def of(p0: int) -> "ThaiBuddhistEra": ...
