from typing import Any, ClassVar, overload
from android.content.Context import Context
from android.database.Cursor import Cursor
from android.view.View import View
from android.view.ViewGroup import ViewGroup

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

class ResourceCursorAdapter:
    @overload
    def __init__(self, arg0: Context, arg1: int, arg2: Cursor) -> None: ...
    @overload
    def __init__(self, arg0: Context, arg1: int, arg2: Cursor, arg3: bool) -> None: ...
    @overload
    def __init__(self, arg0: Context, arg1: int, arg2: Cursor, arg3: int) -> None: ...
    def setDropDownViewTheme(self, arg0: Theme) -> None: ...
    def newView(self, arg0: Context, arg1: Cursor, arg2: ViewGroup) -> View: ...
    def newDropDownView(self, arg0: Context, arg1: Cursor, arg2: ViewGroup) -> View: ...
    def setViewResource(self, arg0: int) -> None: ...
    def setDropDownViewResource(self, arg0: int) -> None: ...
