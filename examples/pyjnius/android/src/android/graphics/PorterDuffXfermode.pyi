from typing import Any, ClassVar, overload

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Mode:
    """Forward declaration for ``android.graphics.PorterDuff.Mode``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.graphics.PorterDuff.Mode')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/graphics/PorterDuff/Mode
    """
    ...

class PorterDuffXfermode:
    def __init__(self, arg0: Mode) -> None: ...
