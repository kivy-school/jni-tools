from typing import Any, ClassVar, overload
from android.graphics.Rect import Rect

class Gravity:
    AXIS_CLIP: ClassVar[int]
    AXIS_PULL_AFTER: ClassVar[int]
    AXIS_PULL_BEFORE: ClassVar[int]
    AXIS_SPECIFIED: ClassVar[int]
    AXIS_X_SHIFT: ClassVar[int]
    AXIS_Y_SHIFT: ClassVar[int]
    BOTTOM: ClassVar[int]
    CENTER: ClassVar[int]
    CENTER_HORIZONTAL: ClassVar[int]
    CENTER_VERTICAL: ClassVar[int]
    CLIP_HORIZONTAL: ClassVar[int]
    CLIP_VERTICAL: ClassVar[int]
    DISPLAY_CLIP_HORIZONTAL: ClassVar[int]
    DISPLAY_CLIP_VERTICAL: ClassVar[int]
    END: ClassVar[int]
    FILL: ClassVar[int]
    FILL_HORIZONTAL: ClassVar[int]
    FILL_VERTICAL: ClassVar[int]
    HORIZONTAL_GRAVITY_MASK: ClassVar[int]
    LEFT: ClassVar[int]
    NO_GRAVITY: ClassVar[int]
    RELATIVE_HORIZONTAL_GRAVITY_MASK: ClassVar[int]
    RELATIVE_LAYOUT_DIRECTION: ClassVar[int]
    RIGHT: ClassVar[int]
    START: ClassVar[int]
    TOP: ClassVar[int]
    VERTICAL_GRAVITY_MASK: ClassVar[int]
    def __init__(self) -> None: ...
    @overload
    @staticmethod
    def applyDisplay(p0: int, p1: Rect, p2: Rect) -> None: ...
    @overload
    @staticmethod
    def applyDisplay(p0: int, p1: Rect, p2: Rect, p3: int) -> None: ...
    @staticmethod
    def getAbsoluteGravity(p0: int, p1: int) -> int: ...
    @staticmethod
    def isHorizontal(p0: int) -> bool: ...
    @staticmethod
    def isVertical(p0: int) -> bool: ...
    @overload
    @staticmethod
    def apply(p0: int, p1: int, p2: int, p3: Rect, p4: int, p5: int, p6: Rect, p7: int) -> None: ...
    @overload
    @staticmethod
    def apply(p0: int, p1: int, p2: int, p3: Rect, p4: Rect) -> None: ...
    @overload
    @staticmethod
    def apply(p0: int, p1: int, p2: int, p3: Rect, p4: Rect, p5: int) -> None: ...
    @overload
    @staticmethod
    def apply(p0: int, p1: int, p2: int, p3: Rect, p4: int, p5: int, p6: Rect) -> None: ...
