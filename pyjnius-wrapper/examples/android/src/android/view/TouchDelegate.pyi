from typing import Any, ClassVar, overload
from android.graphics.Rect import Rect
from android.view.MotionEvent import MotionEvent
from android.view.View import View

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class TouchDelegateInfo:
    """Forward declaration for ``android.view.accessibility.AccessibilityNodeInfo.TouchDelegateInfo``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.view.accessibility.AccessibilityNodeInfo.TouchDelegateInfo')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/view/accessibility/AccessibilityNodeInfo/TouchDelegateInfo
    """
    ...

class TouchDelegate:
    ABOVE: ClassVar[int]
    BELOW: ClassVar[int]
    TO_LEFT: ClassVar[int]
    TO_RIGHT: ClassVar[int]
    def __init__(self, arg0: Rect, arg1: View) -> None: ...
    def onTouchEvent(self, arg0: MotionEvent) -> bool: ...
    def onTouchExplorationHoverEvent(self, arg0: MotionEvent) -> bool: ...
    def getTouchDelegateInfo(self) -> TouchDelegateInfo: ...
