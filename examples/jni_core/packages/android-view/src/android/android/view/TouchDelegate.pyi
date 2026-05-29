from typing import Any, ClassVar, overload
from android.graphics.Rect import Rect
from android.view.MotionEvent import MotionEvent
from android.view.View import View

class TouchDelegate:
    ABOVE: ClassVar[int]
    BELOW: ClassVar[int]
    TO_LEFT: ClassVar[int]
    TO_RIGHT: ClassVar[int]
    def __init__(self, p0: Rect, p1: View) -> None: ...
    def getTouchDelegateInfo(self) -> Any: ...
    def onTouchEvent(self, p0: MotionEvent) -> bool: ...
    def onTouchExplorationHoverEvent(self, p0: MotionEvent) -> bool: ...
