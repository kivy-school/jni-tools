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
    def getContantForFocusDirection(arg0: int) -> int: ...
    @staticmethod
    def getConstantForFocusDirection(arg0: int, arg1: bool) -> int: ...
