from typing import Any, ClassVar, overload
from android.graphics.Canvas import Canvas
from android.graphics.Paint import Paint
from android.text.TextPaint import TextPaint

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class FontMetricsInt:
    """Forward declaration for ``android.graphics.Paint.FontMetricsInt``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.graphics.Paint.FontMetricsInt')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/graphics/Paint/FontMetricsInt
    """
    ...

class ReplacementSpan:
    def __init__(self) -> None: ...
    def getSize(self, arg0: Paint, arg1: str, arg2: int, arg3: int, arg4: FontMetricsInt) -> int: ...
    def draw(self, arg0: Canvas, arg1: str, arg2: int, arg3: int, arg4: float, arg5: int, arg6: int, arg7: int, arg8: Paint) -> None: ...
    def getContentDescription(self) -> str: ...
    def setContentDescription(self, arg0: str) -> None: ...
    def updateMeasureState(self, arg0: TextPaint) -> None: ...
    def updateDrawState(self, arg0: TextPaint) -> None: ...
