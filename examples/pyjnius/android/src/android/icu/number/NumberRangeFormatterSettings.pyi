from typing import Any, ClassVar, overload
from android.icu.number.UnlocalizedNumberFormatter import UnlocalizedNumberFormatter

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class RangeCollapse:
    """Forward declaration for ``android.icu.number.NumberRangeFormatter.RangeCollapse``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.icu.number.NumberRangeFormatter.RangeCollapse')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/icu/number/NumberRangeFormatter/RangeCollapse
    """
    ...
class RangeIdentityFallback:
    """Forward declaration for ``android.icu.number.NumberRangeFormatter.RangeIdentityFallback``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.icu.number.NumberRangeFormatter.RangeIdentityFallback')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/icu/number/NumberRangeFormatter/RangeIdentityFallback
    """
    ...

class NumberRangeFormatterSettings:
    def numberFormatterBoth(self, arg0: UnlocalizedNumberFormatter) -> "NumberRangeFormatterSettings": ...
    def numberFormatterFirst(self, arg0: UnlocalizedNumberFormatter) -> "NumberRangeFormatterSettings": ...
    def numberFormatterSecond(self, arg0: UnlocalizedNumberFormatter) -> "NumberRangeFormatterSettings": ...
    def collapse(self, arg0: RangeCollapse) -> "NumberRangeFormatterSettings": ...
    def identityFallback(self, arg0: RangeIdentityFallback) -> "NumberRangeFormatterSettings": ...
    def hashCode(self) -> int: ...
    def equals(self, arg0: Any) -> bool: ...
