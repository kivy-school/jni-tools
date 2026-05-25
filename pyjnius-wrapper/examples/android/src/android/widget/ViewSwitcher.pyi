from typing import Any, ClassVar, overload
from android.content.Context import Context
from android.util.AttributeSet import AttributeSet
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

class ViewSwitcher:
    @overload
    def __init__(self, arg0: Context) -> None: ...
    @overload
    def __init__(self, arg0: Context, arg1: AttributeSet) -> None: ...
    def addView(self, arg0: View, arg1: int, arg2: LayoutParams) -> None: ...
    def getAccessibilityClassName(self) -> str: ...
    def getNextView(self) -> View: ...
    def setFactory(self, arg0: "ViewFactory") -> None: ...
    def reset(self) -> None: ...

    class ViewFactory:
        def makeView(self) -> View: ...
