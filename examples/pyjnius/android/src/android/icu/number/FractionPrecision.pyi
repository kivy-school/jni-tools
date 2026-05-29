from typing import Any, ClassVar, overload
from android.icu.number.Precision import Precision

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class RoundingPriority:
    """Forward declaration for ``android.icu.number.NumberFormatter.RoundingPriority``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.icu.number.NumberFormatter.RoundingPriority')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/icu/number/NumberFormatter/RoundingPriority
    """
    ...

class FractionPrecision:
    def withSignificantDigits(self, arg0: int, arg1: int, arg2: RoundingPriority) -> Precision: ...
    def withMinDigits(self, arg0: int) -> Precision: ...
    def withMaxDigits(self, arg0: int) -> Precision: ...
