from typing import Any, ClassVar, overload

class LutProperties:
    ONE_DIMENSION: ClassVar[int]
    SAMPLING_KEY_CIE_Y: ClassVar[int]
    SAMPLING_KEY_MAX_RGB: ClassVar[int]
    SAMPLING_KEY_RGB: ClassVar[int]
    THREE_DIMENSION: ClassVar[int]
    def getSamplingKeys(self) -> Any: ...
    def getSize(self) -> int: ...
    def getDimension(self) -> int: ...
