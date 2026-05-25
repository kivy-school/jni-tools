from typing import Any, ClassVar, overload
from android.icu.number.LocalizedNumberFormatter import LocalizedNumberFormatter
from android.icu.util.ULocale import ULocale
from java.util.Locale import Locale

class UnlocalizedNumberFormatter:
    @overload
    def locale(self, p0: Locale) -> LocalizedNumberFormatter: ...
    @overload
    def locale(self, p0: ULocale) -> LocalizedNumberFormatter: ...
