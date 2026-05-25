from typing import Any, ClassVar, overload
from android.icu.number.LocalizedNumberFormatter import LocalizedNumberFormatter
from android.icu.util.ULocale import ULocale
from java.util.Locale import Locale

class UnlocalizedNumberFormatter:
    @overload
    def locale(self, arg0: Locale) -> LocalizedNumberFormatter: ...
    @overload
    def locale(self, arg0: ULocale) -> LocalizedNumberFormatter: ...
