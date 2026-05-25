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

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class GroupingStrategy:
    """Forward declaration for ``android.icu.number.NumberFormatter.GroupingStrategy``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.icu.number.NumberFormatter.GroupingStrategy')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/icu/number/NumberFormatter/GroupingStrategy
    """
    ...
class UnitWidth:
    """Forward declaration for ``android.icu.number.NumberFormatter.UnitWidth``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.icu.number.NumberFormatter.UnitWidth')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/icu/number/NumberFormatter/UnitWidth
    """
    ...
class SignDisplay:
    """Forward declaration for ``android.icu.number.NumberFormatter.SignDisplay``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.icu.number.NumberFormatter.SignDisplay')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/icu/number/NumberFormatter/SignDisplay
    """
    ...
class DecimalSeparatorDisplay:
    """Forward declaration for ``android.icu.number.NumberFormatter.DecimalSeparatorDisplay``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.icu.number.NumberFormatter.DecimalSeparatorDisplay')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/icu/number/NumberFormatter/DecimalSeparatorDisplay
    """
    ...

class NumberFormatterSettings:
    def notation(self, arg0: Notation) -> "NumberFormatterSettings": ...
    def unit(self, arg0: MeasureUnit) -> "NumberFormatterSettings": ...
    def perUnit(self, arg0: MeasureUnit) -> "NumberFormatterSettings": ...
    def precision(self, arg0: Precision) -> "NumberFormatterSettings": ...
    def roundingMode(self, arg0: RoundingMode) -> "NumberFormatterSettings": ...
    def grouping(self, arg0: GroupingStrategy) -> "NumberFormatterSettings": ...
    def integerWidth(self, arg0: IntegerWidth) -> "NumberFormatterSettings": ...
    @overload
    def symbols(self, arg0: DecimalFormatSymbols) -> "NumberFormatterSettings": ...
    @overload
    def symbols(self, arg0: NumberingSystem) -> "NumberFormatterSettings": ...
    def unitWidth(self, arg0: UnitWidth) -> "NumberFormatterSettings": ...
    def sign(self, arg0: SignDisplay) -> "NumberFormatterSettings": ...
    def decimal(self, arg0: DecimalSeparatorDisplay) -> "NumberFormatterSettings": ...
    def scale(self, arg0: Scale) -> "NumberFormatterSettings": ...
    def usage(self, arg0: str) -> "NumberFormatterSettings": ...
    def displayOptions(self, arg0: DisplayOptions) -> "NumberFormatterSettings": ...
    def hashCode(self) -> int: ...
    def equals(self, arg0: Any) -> bool: ...
