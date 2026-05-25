from typing import Any, ClassVar, overload
from android.graphics.Paint import Paint
from android.graphics.text.PositionedGlyphs import PositionedGlyphs

class TextRunShaper:
    @overload
    @staticmethod
    def shapeTextRun(arg0: list[str], arg1: int, arg2: int, arg3: int, arg4: int, arg5: float, arg6: float, arg7: bool, arg8: Paint) -> PositionedGlyphs: ...
    @overload
    @staticmethod
    def shapeTextRun(arg0: str, arg1: int, arg2: int, arg3: int, arg4: int, arg5: float, arg6: float, arg7: bool, arg8: Paint) -> PositionedGlyphs: ...
