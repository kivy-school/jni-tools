from typing import Any, ClassVar, overload
from android.content.Context import Context
from android.graphics.Path import Path
from android.util.AttributeSet import AttributeSet

class PathMotion:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, arg0: Context, arg1: AttributeSet) -> None: ...
    def getPath(self, arg0: float, arg1: float, arg2: float, arg3: float) -> Path: ...
