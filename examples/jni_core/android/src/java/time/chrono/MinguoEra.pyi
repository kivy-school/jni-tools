from typing import Any, ClassVar, overload
from java.time.format.TextStyle import TextStyle
from java.util.Locale import Locale

class MinguoEra:
    BEFORE_ROC: ClassVar["MinguoEra"]
    ROC: ClassVar["MinguoEra"]
    BEFORE_ROC: ClassVar["MinguoEra"]
    ROC: ClassVar["MinguoEra"]
    def getDisplayName(self, p0: TextStyle, p1: Locale) -> str: ...
    @staticmethod
    def values() -> Any: ...
    @staticmethod
    def valueOf(p0: str) -> "MinguoEra": ...
    def getValue(self) -> int: ...
    @staticmethod
    def of(p0: int) -> "MinguoEra": ...
