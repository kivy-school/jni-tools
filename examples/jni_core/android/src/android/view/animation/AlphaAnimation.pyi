from typing import Any, ClassVar, overload
from android.content.Context import Context
from android.util.AttributeSet import AttributeSet

class AlphaAnimation:
    ABSOLUTE: ClassVar[int]
    INFINITE: ClassVar[int]
    RELATIVE_TO_PARENT: ClassVar[int]
    RELATIVE_TO_SELF: ClassVar[int]
    RESTART: ClassVar[int]
    REVERSE: ClassVar[int]
    START_ON_FIRST_FRAME: ClassVar[int]
    ZORDER_BOTTOM: ClassVar[int]
    ZORDER_NORMAL: ClassVar[int]
    ZORDER_TOP: ClassVar[int]
    @overload
    def __init__(self, p0: float, p1: float) -> None: ...
    @overload
    def __init__(self, p0: Context, p1: AttributeSet) -> None: ...
    def willChangeTransformationMatrix(self) -> bool: ...
    def willChangeBounds(self) -> bool: ...
