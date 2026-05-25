from typing import Any, ClassVar, overload
from android.graphics.text.PositionedGlyphs import PositionedGlyphs
from android.text.TextDirectionHeuristic import TextDirectionHeuristic
from android.text.TextPaint import TextPaint

class TextShaper:
    @staticmethod
    def shapeText(arg0: str, arg1: int, arg2: int, arg3: TextDirectionHeuristic, arg4: TextPaint, arg5: "GlyphsConsumer") -> None: ...

    class GlyphsConsumer:
        def accept(self, arg0: int, arg1: int, arg2: PositionedGlyphs, arg3: TextPaint) -> None: ...
