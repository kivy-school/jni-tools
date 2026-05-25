from typing import Any, ClassVar, overload
from android.content.Context import Context
from android.view.MenuItem import MenuItem
from android.view.View import View

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class OnClickListener:
    """Forward declaration for ``android.view.View.OnClickListener``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.view.View.OnClickListener')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/view/View/OnClickListener
    """
    ...

class MediaRouteActionProvider:
    def __init__(self, arg0: Context) -> None: ...
    def setRouteTypes(self, arg0: int) -> None: ...
    def setExtendedSettingsClickListener(self, arg0: OnClickListener) -> None: ...
    @overload
    def onCreateActionView(self) -> View: ...
    @overload
    def onCreateActionView(self, arg0: MenuItem) -> View: ...
    def onPerformDefaultAction(self) -> bool: ...
    def overridesItemVisibility(self) -> bool: ...
    def isVisible(self) -> bool: ...
