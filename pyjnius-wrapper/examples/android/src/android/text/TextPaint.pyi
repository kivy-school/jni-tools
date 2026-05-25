from typing import Any, ClassVar, overload
from android.graphics.Paint import Paint

class TextPaint:
    baselineShift: int
    bgColor: int
    density: float
    drawableState: list[int]
    linkColor: int
    underlineColor: int
    underlineThickness: float
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, arg0: int) -> None: ...
    @overload
    def __init__(self, arg0: Paint) -> None: ...
    def set(self, arg0: "TextPaint") -> None: ...
    def getUnderlineThickness(self) -> float: ...
