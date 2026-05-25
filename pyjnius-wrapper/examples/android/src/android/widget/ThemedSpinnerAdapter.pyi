from typing import Any, ClassVar, overload

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Theme:
    """Forward declaration for ``android.content.res.Resources.Theme``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.content.res.Resources.Theme')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/content/res/Resources/Theme
    """
    ...

class ThemedSpinnerAdapter:
    def setDropDownViewTheme(self, arg0: Theme) -> None: ...
    def getDropDownViewTheme(self) -> Theme: ...
