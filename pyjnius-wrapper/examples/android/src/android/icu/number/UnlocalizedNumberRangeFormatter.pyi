from typing import Any, ClassVar, overload
from android.icu.number.LocalizedNumberRangeFormatter import LocalizedNumberRangeFormatter
from android.icu.util.ULocale import ULocale
from java.util.Locale import Locale

class UnlocalizedNumberRangeFormatter:
    @overload
    def locale(self, arg0: Locale) -> LocalizedNumberRangeFormatter: ...
    @overload
    def locale(self, arg0: ULocale) -> LocalizedNumberRangeFormatter: ...
