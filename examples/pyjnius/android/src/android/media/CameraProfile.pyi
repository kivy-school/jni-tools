from typing import Any, ClassVar, overload

class CameraProfile:
    QUALITY_HIGH: ClassVar[int]
    QUALITY_LOW: ClassVar[int]
    QUALITY_MEDIUM: ClassVar[int]
    def __init__(self) -> None: ...
    @overload
    @staticmethod
    def getJpegEncodingQualityParameter(p0: int) -> int: ...
    @overload
    @staticmethod
    def getJpegEncodingQualityParameter(p0: int, p1: int) -> int: ...
