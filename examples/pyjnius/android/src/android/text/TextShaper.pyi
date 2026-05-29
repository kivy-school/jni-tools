from typing import Any, ClassVar, overload
from android.graphics.text.PositionedGlyphs import PositionedGlyphs
from android.text.TextDirectionHeuristic import TextDirectionHeuristic
from android.text.TextPaint import TextPaint

class TextShaper:
    @staticmethod
    def shapeText(p0: str, p1: int, p2: int, p3: TextDirectionHeuristic, p4: TextPaint, p5: Any) -> None: ...

    class GlyphsConsumer:
        def accept(self, p0: int, p1: int, p2: PositionedGlyphs, p3: TextPaint) -> None: ...
