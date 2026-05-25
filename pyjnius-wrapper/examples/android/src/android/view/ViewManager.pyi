from typing import Any, ClassVar, overload
from android.view.View import View

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class LayoutParams:
    """Forward declaration for ``android.view.ViewGroup.LayoutParams``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.view.ViewGroup.LayoutParams')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/view/ViewGroup/LayoutParams
    """
    ...

class ViewManager:
    def addView(self, arg0: View, arg1: LayoutParams) -> None: ...
    def updateViewLayout(self, arg0: View, arg1: LayoutParams) -> None: ...
    def removeView(self, arg0: View) -> None: ...
