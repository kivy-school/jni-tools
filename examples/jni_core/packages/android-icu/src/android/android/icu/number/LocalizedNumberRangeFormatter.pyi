from typing import Any, ClassVar, overload
from android.icu.number.FormattedNumberRange import FormattedNumberRange

class LocalizedNumberRangeFormatter:
    @overload
    def formatRange(self, p0: float, p1: float) -> FormattedNumberRange: ...
    @overload
    def formatRange(self, p0: int, p1: int) -> FormattedNumberRange: ...
    @overload
    def formatRange(self, p0: float, p1: float) -> FormattedNumberRange: ...
