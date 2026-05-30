from typing import Any, ClassVar, overload
from android.icu.number.Precision import Precision

class FractionPrecision:
    def withMaxDigits(self, p0: int) -> Precision: ...
    def withMinDigits(self, p0: int) -> Precision: ...
    def withSignificantDigits(self, p0: int, p1: int, p2: Any) -> Precision: ...

from typing import Any, ClassVar, overload
from java.math.BigDecimal import BigDecimal

class Scale:
    @staticmethod
    def none() -> "Scale": ...
    @staticmethod
    def byBigDecimal(p0: BigDecimal) -> "Scale": ...
    @staticmethod
    def byDouble(p0: float) -> "Scale": ...
    @staticmethod
    def byDoubleAndPowerOfTen(p0: float, p1: int) -> "Scale": ...
    @staticmethod
    def powerOfTen(p0: int) -> "Scale": ...

from typing import Any, ClassVar, overload
from android.icu.number.CurrencyPrecision import CurrencyPrecision
from android.icu.number.FractionPrecision import FractionPrecision
from java.math.BigDecimal import BigDecimal

class Precision:
    @staticmethod
    def currency(p0: Any) -> CurrencyPrecision: ...
    @staticmethod
    def integer() -> FractionPrecision: ...
    @staticmethod
    def maxSignificantDigits(p0: int) -> "Precision": ...
    @staticmethod
    def minSignificantDigits(p0: int) -> "Precision": ...
    @staticmethod
    def fixedFraction(p0: int) -> FractionPrecision: ...
    @staticmethod
    def fixedSignificantDigits(p0: int) -> "Precision": ...
    @staticmethod
    def minMaxSignificantDigits(p0: int, p1: int) -> "Precision": ...
    @staticmethod
    def maxFraction(p0: int) -> FractionPrecision: ...
    @staticmethod
    def minFraction(p0: int) -> FractionPrecision: ...
    @staticmethod
    def minMaxFraction(p0: int, p1: int) -> FractionPrecision: ...
    def trailingZeroDisplay(self, p0: Any) -> "Precision": ...
    @staticmethod
    def unlimited() -> "Precision": ...
    @staticmethod
    def increment(p0: BigDecimal) -> "Precision": ...

from typing import Any, ClassVar, overload
from android.icu.text.ConstrainedFieldPosition import ConstrainedFieldPosition
from android.icu.util.MeasureUnit import MeasureUnit
from java.lang.Appendable import Appendable
from java.math.BigDecimal import BigDecimal
from java.text.AttributedCharacterIterator import AttributedCharacterIterator

class FormattedNumber:
    def getNounClass(self) -> Any: ...
    def getOutputUnit(self) -> MeasureUnit: ...
    def nextPosition(self, p0: ConstrainedFieldPosition) -> bool: ...
    def toCharacterIterator(self) -> AttributedCharacterIterator: ...
    def toBigDecimal(self) -> BigDecimal: ...
    def length(self) -> int: ...
    def toString(self) -> str: ...
    def charAt(self, p0: int) -> str: ...
    def subSequence(self, p0: int, p1: int) -> str: ...
    def appendTo(self, p0: Appendable) -> Appendable: ...

from typing import Any, ClassVar, overload

class IntegerWidth:
    @staticmethod
    def zeroFillTo(p0: int) -> "IntegerWidth": ...
    def truncateAt(self, p0: int) -> "IntegerWidth": ...

from typing import Any, ClassVar, overload
from android.icu.number.UnlocalizedNumberFormatter import UnlocalizedNumberFormatter

class NumberRangeFormatterSettings:
    def identityFallback(self, p0: Any) -> "NumberRangeFormatterSettings": ...
    def collapse(self, p0: Any) -> "NumberRangeFormatterSettings": ...
    def numberFormatterBoth(self, p0: UnlocalizedNumberFormatter) -> "NumberRangeFormatterSettings": ...
    def numberFormatterFirst(self, p0: UnlocalizedNumberFormatter) -> "NumberRangeFormatterSettings": ...
    def numberFormatterSecond(self, p0: UnlocalizedNumberFormatter) -> "NumberRangeFormatterSettings": ...
    def equals(self, p0: Any) -> bool: ...
    def hashCode(self) -> int: ...

from typing import Any, ClassVar, overload
from android.icu.number.LocalizedNumberRangeFormatter import LocalizedNumberRangeFormatter
from android.icu.util.ULocale import ULocale
from java.util.Locale import Locale

class UnlocalizedNumberRangeFormatter:
    @overload
    def locale(self, p0: ULocale) -> LocalizedNumberRangeFormatter: ...
    @overload
    def locale(self, p0: Locale) -> LocalizedNumberRangeFormatter: ...

from typing import Any, ClassVar, overload
from android.icu.number.Precision import Precision
from android.icu.util.Currency import Currency

class CurrencyPrecision:
    def withCurrency(self, p0: Currency) -> Precision: ...

from typing import Any, ClassVar, overload
from android.icu.number.LocalizedNumberFormatter import LocalizedNumberFormatter
from android.icu.number.UnlocalizedNumberFormatter import UnlocalizedNumberFormatter
from android.icu.util.ULocale import ULocale
from java.util.Locale import Locale

class NumberFormatter:
    @staticmethod
    def with_() -> UnlocalizedNumberFormatter: ...
    @overload
    @staticmethod
    def withLocale(p0: Locale) -> LocalizedNumberFormatter: ...
    @overload
    @staticmethod
    def withLocale(p0: ULocale) -> LocalizedNumberFormatter: ...

    class UnitWidth:
        FORMAL: ClassVar["UnitWidth"]
        FULL_NAME: ClassVar["UnitWidth"]
        HIDDEN: ClassVar["UnitWidth"]
        ISO_CODE: ClassVar["UnitWidth"]
        NARROW: ClassVar["UnitWidth"]
        SHORT: ClassVar["UnitWidth"]
        VARIANT: ClassVar["UnitWidth"]
        FORMAL: ClassVar[Any]
        FULL_NAME: ClassVar[Any]
        HIDDEN: ClassVar[Any]
        ISO_CODE: ClassVar[Any]
        NARROW: ClassVar[Any]
        SHORT: ClassVar[Any]
        VARIANT: ClassVar[Any]
        @staticmethod
        def values() -> Any: ...
        @staticmethod
        def valueOf(p0: str) -> Any: ...

    class TrailingZeroDisplay:
        AUTO: ClassVar["TrailingZeroDisplay"]
        HIDE_IF_WHOLE: ClassVar["TrailingZeroDisplay"]
        AUTO: ClassVar[Any]
        HIDE_IF_WHOLE: ClassVar[Any]
        @staticmethod
        def values() -> Any: ...
        @staticmethod
        def valueOf(p0: str) -> Any: ...

    class SignDisplay:
        ACCOUNTING: ClassVar["SignDisplay"]
        ACCOUNTING_ALWAYS: ClassVar["SignDisplay"]
        ACCOUNTING_EXCEPT_ZERO: ClassVar["SignDisplay"]
        ACCOUNTING_NEGATIVE: ClassVar["SignDisplay"]
        ALWAYS: ClassVar["SignDisplay"]
        AUTO: ClassVar["SignDisplay"]
        EXCEPT_ZERO: ClassVar["SignDisplay"]
        NEGATIVE: ClassVar["SignDisplay"]
        NEVER: ClassVar["SignDisplay"]
        ACCOUNTING: ClassVar[Any]
        ACCOUNTING_ALWAYS: ClassVar[Any]
        ACCOUNTING_EXCEPT_ZERO: ClassVar[Any]
        ACCOUNTING_NEGATIVE: ClassVar[Any]
        ALWAYS: ClassVar[Any]
        AUTO: ClassVar[Any]
        EXCEPT_ZERO: ClassVar[Any]
        NEGATIVE: ClassVar[Any]
        NEVER: ClassVar[Any]
        @staticmethod
        def values() -> Any: ...
        @staticmethod
        def valueOf(p0: str) -> Any: ...

    class RoundingPriority:
        RELAXED: ClassVar["RoundingPriority"]
        STRICT: ClassVar["RoundingPriority"]
        RELAXED: ClassVar[Any]
        STRICT: ClassVar[Any]
        @staticmethod
        def values() -> Any: ...
        @staticmethod
        def valueOf(p0: str) -> Any: ...

    class GroupingStrategy:
        AUTO: ClassVar["GroupingStrategy"]
        MIN2: ClassVar["GroupingStrategy"]
        OFF: ClassVar["GroupingStrategy"]
        ON_ALIGNED: ClassVar["GroupingStrategy"]
        THOUSANDS: ClassVar["GroupingStrategy"]
        AUTO: ClassVar[Any]
        MIN2: ClassVar[Any]
        OFF: ClassVar[Any]
        ON_ALIGNED: ClassVar[Any]
        THOUSANDS: ClassVar[Any]
        @staticmethod
        def values() -> Any: ...
        @staticmethod
        def valueOf(p0: str) -> Any: ...

    class DecimalSeparatorDisplay:
        ALWAYS: ClassVar["DecimalSeparatorDisplay"]
        AUTO: ClassVar["DecimalSeparatorDisplay"]
        ALWAYS: ClassVar[Any]
        AUTO: ClassVar[Any]
        @staticmethod
        def values() -> Any: ...
        @staticmethod
        def valueOf(p0: str) -> Any: ...

from typing import Any, ClassVar, overload
from android.icu.text.ConstrainedFieldPosition import ConstrainedFieldPosition
from java.lang.Appendable import Appendable
from java.math.BigDecimal import BigDecimal
from java.text.AttributedCharacterIterator import AttributedCharacterIterator

class FormattedNumberRange:
    def getFirstBigDecimal(self) -> BigDecimal: ...
    def getIdentityResult(self) -> Any: ...
    def getSecondBigDecimal(self) -> BigDecimal: ...
    def nextPosition(self, p0: ConstrainedFieldPosition) -> bool: ...
    def toCharacterIterator(self) -> AttributedCharacterIterator: ...
    def equals(self, p0: Any) -> bool: ...
    def length(self) -> int: ...
    def toString(self) -> str: ...
    def hashCode(self) -> int: ...
    def charAt(self, p0: int) -> str: ...
    def subSequence(self, p0: int, p1: int) -> str: ...
    def appendTo(self, p0: Appendable) -> Appendable: ...

from typing import Any, ClassVar, overload
from android.icu.number.LocalizedNumberRangeFormatter import LocalizedNumberRangeFormatter
from android.icu.number.UnlocalizedNumberRangeFormatter import UnlocalizedNumberRangeFormatter
from android.icu.util.ULocale import ULocale
from java.util.Locale import Locale

class NumberRangeFormatter:
    @staticmethod
    def with_() -> UnlocalizedNumberRangeFormatter: ...
    @overload
    @staticmethod
    def withLocale(p0: Locale) -> LocalizedNumberRangeFormatter: ...
    @overload
    @staticmethod
    def withLocale(p0: ULocale) -> LocalizedNumberRangeFormatter: ...

    class RangeIdentityResult:
        EQUAL_AFTER_ROUNDING: ClassVar["RangeIdentityResult"]
        EQUAL_BEFORE_ROUNDING: ClassVar["RangeIdentityResult"]
        NOT_EQUAL: ClassVar["RangeIdentityResult"]
        EQUAL_AFTER_ROUNDING: ClassVar[Any]
        EQUAL_BEFORE_ROUNDING: ClassVar[Any]
        NOT_EQUAL: ClassVar[Any]
        @staticmethod
        def values() -> Any: ...
        @staticmethod
        def valueOf(p0: str) -> Any: ...

    class RangeIdentityFallback:
        APPROXIMATELY: ClassVar["RangeIdentityFallback"]
        APPROXIMATELY_OR_SINGLE_VALUE: ClassVar["RangeIdentityFallback"]
        RANGE: ClassVar["RangeIdentityFallback"]
        SINGLE_VALUE: ClassVar["RangeIdentityFallback"]
        APPROXIMATELY: ClassVar[Any]
        APPROXIMATELY_OR_SINGLE_VALUE: ClassVar[Any]
        RANGE: ClassVar[Any]
        SINGLE_VALUE: ClassVar[Any]
        @staticmethod
        def values() -> Any: ...
        @staticmethod
        def valueOf(p0: str) -> Any: ...

    class RangeCollapse:
        ALL: ClassVar["RangeCollapse"]
        AUTO: ClassVar["RangeCollapse"]
        NONE: ClassVar["RangeCollapse"]
        UNIT: ClassVar["RangeCollapse"]
        ALL: ClassVar[Any]
        AUTO: ClassVar[Any]
        NONE: ClassVar[Any]
        UNIT: ClassVar[Any]
        @staticmethod
        def values() -> Any: ...
        @staticmethod
        def valueOf(p0: str) -> Any: ...

from typing import Any, ClassVar, overload
from android.icu.number.CompactNotation import CompactNotation
from android.icu.number.ScientificNotation import ScientificNotation
from android.icu.number.SimpleNotation import SimpleNotation

class Notation:
    @staticmethod
    def simple() -> SimpleNotation: ...
    @staticmethod
    def compactShort() -> CompactNotation: ...
    @staticmethod
    def engineering() -> ScientificNotation: ...
    @staticmethod
    def scientific() -> ScientificNotation: ...
    @staticmethod
    def compactLong() -> CompactNotation: ...

from typing import Any, ClassVar, overload
from android.icu.number.FormattedNumber import FormattedNumber
from android.icu.number.UnlocalizedNumberFormatter import UnlocalizedNumberFormatter
from android.icu.util.Measure import Measure
from java.text.Format import Format

class LocalizedNumberFormatter:
    def withoutLocale(self) -> UnlocalizedNumberFormatter: ...
    @overload
    def format(self, p0: float) -> FormattedNumber: ...
    @overload
    def format(self, p0: int) -> FormattedNumber: ...
    @overload
    def format(self, p0: Measure) -> FormattedNumber: ...
    @overload
    def format(self, p0: float) -> FormattedNumber: ...
    def toFormat(self) -> Format: ...

from typing import Any, ClassVar, overload
from android.icu.number.FormattedNumberRange import FormattedNumberRange
from android.icu.number.UnlocalizedNumberRangeFormatter import UnlocalizedNumberRangeFormatter

class LocalizedNumberRangeFormatter:
    @overload
    def formatRange(self, p0: int, p1: int) -> FormattedNumberRange: ...
    @overload
    def formatRange(self, p0: float, p1: float) -> FormattedNumberRange: ...
    @overload
    def formatRange(self, p0: float, p1: float) -> FormattedNumberRange: ...
    def withoutLocale(self) -> UnlocalizedNumberRangeFormatter: ...

from typing import Any, ClassVar, overload

class ScientificNotation:
    def withExponentSignDisplay(self, p0: Any) -> "ScientificNotation": ...
    def withMinExponentDigits(self, p0: int) -> "ScientificNotation": ...

from typing import Any, ClassVar, overload

class CompactNotation:
    ...

from typing import Any, ClassVar, overload
from android.icu.number.IntegerWidth import IntegerWidth
from android.icu.number.Notation import Notation
from android.icu.number.Precision import Precision
from android.icu.number.Scale import Scale
from android.icu.text.DecimalFormatSymbols import DecimalFormatSymbols
from android.icu.text.DisplayOptions import DisplayOptions
from android.icu.text.NumberingSystem import NumberingSystem
from android.icu.util.MeasureUnit import MeasureUnit
from java.math.RoundingMode import RoundingMode

class NumberFormatterSettings:
    def usage(self, p0: str) -> "NumberFormatterSettings": ...
    def displayOptions(self, p0: DisplayOptions) -> "NumberFormatterSettings": ...
    def decimal(self, p0: Any) -> "NumberFormatterSettings": ...
    def grouping(self, p0: Any) -> "NumberFormatterSettings": ...
    def integerWidth(self, p0: IntegerWidth) -> "NumberFormatterSettings": ...
    def notation(self, p0: Notation) -> "NumberFormatterSettings": ...
    def perUnit(self, p0: MeasureUnit) -> "NumberFormatterSettings": ...
    def unitWidth(self, p0: Any) -> "NumberFormatterSettings": ...
    def equals(self, p0: Any) -> bool: ...
    def hashCode(self) -> int: ...
    def scale(self, p0: Scale) -> "NumberFormatterSettings": ...
    def precision(self, p0: Precision) -> "NumberFormatterSettings": ...
    def sign(self, p0: Any) -> "NumberFormatterSettings": ...
    def unit(self, p0: MeasureUnit) -> "NumberFormatterSettings": ...
    @overload
    def symbols(self, p0: NumberingSystem) -> "NumberFormatterSettings": ...
    @overload
    def symbols(self, p0: DecimalFormatSymbols) -> "NumberFormatterSettings": ...
    def roundingMode(self, p0: RoundingMode) -> "NumberFormatterSettings": ...

from typing import Any, ClassVar, overload
from android.icu.number.LocalizedNumberFormatter import LocalizedNumberFormatter
from android.icu.util.ULocale import ULocale
from java.util.Locale import Locale

class UnlocalizedNumberFormatter:
    @overload
    def locale(self, p0: ULocale) -> LocalizedNumberFormatter: ...
    @overload
    def locale(self, p0: Locale) -> LocalizedNumberFormatter: ...

from typing import Any, ClassVar, overload

class SimpleNotation:
    ...

