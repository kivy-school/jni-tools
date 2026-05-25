from typing import Any, ClassVar, overload

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class SignDisplay:
    """Forward declaration for ``android.icu.number.NumberFormatter.SignDisplay``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.icu.number.NumberFormatter.SignDisplay')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/icu/number/NumberFormatter/SignDisplay
    """
    ...

class ScientificNotation:
    def withMinExponentDigits(self, arg0: int) -> "ScientificNotation": ...
    def withExponentSignDisplay(self, arg0: SignDisplay) -> "ScientificNotation": ...
