from typing import Any, ClassVar, overload
from android.icu.number.FormattedNumberRange import FormattedNumberRange

class LocalizedNumberRangeFormatter:
    @overload
    def formatRange(self, arg0: int, arg1: int) -> FormattedNumberRange: ...
    @overload
    def formatRange(self, arg0: float, arg1: float) -> FormattedNumberRange: ...
    @overload
    def formatRange(self, arg0: float, arg1: float) -> FormattedNumberRange: ...
