from typing import Any, ClassVar, overload
from android.icu.util.CurrencyAmount import CurrencyAmount
from android.icu.util.ULocale import ULocale
from java.text.ParsePosition import ParsePosition
from java.util.Locale import Locale

class CompactDecimalFormat:
    MINIMUM_GROUPING_DIGITS_AUTO: ClassVar[int]
    MINIMUM_GROUPING_DIGITS_MIN2: ClassVar[int]
    PAD_AFTER_PREFIX: ClassVar[int]
    PAD_AFTER_SUFFIX: ClassVar[int]
    PAD_BEFORE_PREFIX: ClassVar[int]
    PAD_BEFORE_SUFFIX: ClassVar[int]
    ACCOUNTINGCURRENCYSTYLE: ClassVar[int]
    CASHCURRENCYSTYLE: ClassVar[int]
    CURRENCYSTYLE: ClassVar[int]
    FRACTION_FIELD: ClassVar[int]
    INTEGERSTYLE: ClassVar[int]
    INTEGER_FIELD: ClassVar[int]
    ISOCURRENCYSTYLE: ClassVar[int]
    NUMBERSTYLE: ClassVar[int]
    PERCENTSTYLE: ClassVar[int]
    PLURALCURRENCYSTYLE: ClassVar[int]
    SCIENTIFICSTYLE: ClassVar[int]
    STANDARDCURRENCYSTYLE: ClassVar[int]
    def parseCurrency(self, p0: str, p1: ParsePosition) -> CurrencyAmount: ...
    @overload
    @staticmethod
    def getInstance(p0: ULocale, p1: Any) -> "CompactDecimalFormat": ...
    @overload
    @staticmethod
    def getInstance(p0: Locale, p1: Any) -> "CompactDecimalFormat": ...
    def parse(self, p0: str, p1: ParsePosition) -> float: ...

    class CompactStyle:
        SHORT: ClassVar["CompactStyle"]
        LONG: ClassVar["CompactStyle"]
        SHORT: ClassVar[Any]
        LONG: ClassVar[Any]
        @staticmethod
        def values() -> Any: ...
        @staticmethod
        def valueOf(p0: str) -> Any: ...
