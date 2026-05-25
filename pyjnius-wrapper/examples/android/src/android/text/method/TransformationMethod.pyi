from typing import Any, ClassVar, overload
from android.graphics.Rect import Rect
from android.view.View import View

class TransformationMethod:
    def getTransformation(self, arg0: str, arg1: View) -> str: ...
    def onFocusChanged(self, arg0: View, arg1: str, arg2: bool, arg3: int, arg4: Rect) -> None: ...
