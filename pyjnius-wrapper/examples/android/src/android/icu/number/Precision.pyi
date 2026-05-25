from typing import Any, ClassVar, overload
from android.icu.number.CurrencyPrecision import CurrencyPrecision
from android.icu.number.FractionPrecision import FractionPrecision
from java.math.BigDecimal import BigDecimal

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class CurrencyUsage:
    """Forward declaration for ``android.icu.util.Currency.CurrencyUsage``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.icu.util.Currency.CurrencyUsage')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/icu/util/Currency/CurrencyUsage
    """
    ...
class TrailingZeroDisplay:
    """Forward declaration for ``android.icu.number.NumberFormatter.TrailingZeroDisplay``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.icu.number.NumberFormatter.TrailingZeroDisplay')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/icu/number/NumberFormatter/TrailingZeroDisplay
    """
    ...

class Precision:
    @staticmethod
    def unlimited() -> "Precision": ...
    @staticmethod
    def integer() -> FractionPrecision: ...
    @staticmethod
    def fixedFraction(arg0: int) -> FractionPrecision: ...
    @staticmethod
    def minFraction(arg0: int) -> FractionPrecision: ...
    @staticmethod
    def maxFraction(arg0: int) -> FractionPrecision: ...
    @staticmethod
    def minMaxFraction(arg0: int, arg1: int) -> FractionPrecision: ...
    @staticmethod
    def fixedSignificantDigits(arg0: int) -> "Precision": ...
    @staticmethod
    def minSignificantDigits(arg0: int) -> "Precision": ...
    @staticmethod
    def maxSignificantDigits(arg0: int) -> "Precision": ...
    @staticmethod
    def minMaxSignificantDigits(arg0: int, arg1: int) -> "Precision": ...
    @staticmethod
    def increment(arg0: BigDecimal) -> "Precision": ...
    @staticmethod
    def currency(arg0: CurrencyUsage) -> CurrencyPrecision: ...
    def trailingZeroDisplay(self, arg0: TrailingZeroDisplay) -> "Precision": ...
