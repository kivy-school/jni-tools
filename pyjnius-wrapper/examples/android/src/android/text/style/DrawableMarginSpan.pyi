from typing import Any, ClassVar, overload
from android.graphics.Canvas import Canvas
from android.graphics.Paint import Paint
from android.graphics.drawable.Drawable import Drawable
from android.text.Layout import Layout

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

class DrawableMarginSpan:
    @overload
    def __init__(self, arg0: Drawable) -> None: ...
    @overload
    def __init__(self, arg0: Drawable, arg1: int) -> None: ...
    def getLeadingMargin(self, arg0: bool) -> int: ...
    def drawLeadingMargin(self, arg0: Canvas, arg1: Paint, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: str, arg8: int, arg9: int, arg10: bool, arg11: Layout) -> None: ...
    def chooseHeight(self, arg0: str, arg1: int, arg2: int, arg3: int, arg4: int, arg5: FontMetricsInt) -> None: ...
    def toString(self) -> str: ...
    def getDrawable(self) -> Drawable: ...
    def getPadding(self) -> int: ...
