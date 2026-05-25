from typing import Any, ClassVar, overload
from java.lang.Throwable import Throwable

class CameraAccessException:
    CAMERA_DISABLED: ClassVar[int]
    CAMERA_DISCONNECTED: ClassVar[int]
    CAMERA_ERROR: ClassVar[int]
    CAMERA_IN_USE: ClassVar[int]
    MAX_CAMERAS_IN_USE: ClassVar[int]
    @overload
    def __init__(self, p0: int) -> None: ...
    @overload
    def __init__(self, p0: int, p1: Throwable) -> None: ...
    @overload
    def __init__(self, p0: int, p1: str, p2: Throwable) -> None: ...
    @overload
    def __init__(self, p0: int, p1: str) -> None: ...
    def getReason(self) -> int: ...
