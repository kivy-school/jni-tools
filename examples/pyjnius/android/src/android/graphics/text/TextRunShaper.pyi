from typing import Any, ClassVar, overload
from android.graphics.Paint import Paint
from android.graphics.text.PositionedGlyphs import PositionedGlyphs

class TextRunShaper:
    @overload
    @staticmethod
    def shapeTextRun(p0: Any, p1: int, p2: int, p3: int, p4: int, p5: float, p6: float, p7: bool, p8: Paint) -> PositionedGlyphs: ...
    @overload
    @staticmethod
    def shapeTextRun(p0: str, p1: int, p2: int, p3: int, p4: int, p5: float, p6: float, p7: bool, p8: Paint) -> PositionedGlyphs: ...
