from typing import Any, ClassVar, overload
from android.content.Context import Context
from android.util.AttributeSet import AttributeSet

class AccelerateDecelerateInterpolator:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, p0: Context, p1: AttributeSet) -> None: ...
    def getInterpolation(self, p0: float) -> float: ...
