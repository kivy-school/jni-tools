from typing import Any, ClassVar, overload
from android.graphics.Outline import Outline
from android.view.View import View

class ViewOutlineProvider:
    BACKGROUND: ClassVar["ViewOutlineProvider"]
    BOUNDS: ClassVar["ViewOutlineProvider"]
    PADDED_BOUNDS: ClassVar["ViewOutlineProvider"]
    def __init__(self) -> None: ...
    def getOutline(self, p0: View, p1: Outline) -> None: ...
