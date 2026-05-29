from typing import Any, ClassVar, overload

class SoundEffectConstants:
    CLICK: ClassVar[int]
    NAVIGATION_DOWN: ClassVar[int]
    NAVIGATION_LEFT: ClassVar[int]
    NAVIGATION_REPEAT_DOWN: ClassVar[int]
    NAVIGATION_REPEAT_LEFT: ClassVar[int]
    NAVIGATION_REPEAT_RIGHT: ClassVar[int]
    NAVIGATION_REPEAT_UP: ClassVar[int]
    NAVIGATION_RIGHT: ClassVar[int]
    NAVIGATION_UP: ClassVar[int]
    @staticmethod
    def getConstantForFocusDirection(p0: int, p1: bool) -> int: ...
    @staticmethod
    def getContantForFocusDirection(p0: int) -> int: ...
