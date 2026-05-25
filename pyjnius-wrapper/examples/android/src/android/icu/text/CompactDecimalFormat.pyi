from typing import Any, ClassVar, overload
from android.icu.util.CurrencyAmount import CurrencyAmount
from android.icu.util.ULocale import ULocale
from java.text.ParsePosition import ParsePosition
from java.util.Locale import Locale

class CompactDecimalFormat:
    @overload
    @staticmethod
    def getInstance(arg0: ULocale, arg1: "CompactStyle") -> "CompactDecimalFormat": ...
    @overload
    @staticmethod
    def getInstance(arg0: Locale, arg1: "CompactStyle") -> "CompactDecimalFormat": ...
    def parse(self, arg0: str, arg1: ParsePosition) -> float: ...
    def parseCurrency(self, arg0: str, arg1: ParsePosition) -> CurrencyAmount: ...

    class CompactStyle:
        SHORT: ClassVar["CompactStyle"]
        LONG: ClassVar["CompactStyle"]
        @staticmethod
        def values() -> list["CompactStyle"]: ...
        @staticmethod
        def valueOf(arg0: str) -> "CompactStyle": ...
