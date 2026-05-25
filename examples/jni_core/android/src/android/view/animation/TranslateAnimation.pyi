from typing import Any, ClassVar, overload
from android.content.Context import Context
from android.util.AttributeSet import AttributeSet

class TranslateAnimation:
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
    def __init__(self, p0: int, p1: float, p2: int, p3: float, p4: int, p5: float, p6: int, p7: float) -> None: ...
    @overload
    def __init__(self, p0: float, p1: float, p2: float, p3: float) -> None: ...
    @overload
    def __init__(self, p0: Context, p1: AttributeSet) -> None: ...
    def initialize(self, p0: int, p1: int, p2: int, p3: int) -> None: ...
