from typing import Any, ClassVar, overload

class CameraProfile:
    QUALITY_HIGH: ClassVar[int]
    QUALITY_LOW: ClassVar[int]
    QUALITY_MEDIUM: ClassVar[int]
    def __init__(self) -> None: ...
    @overload
    @staticmethod
    def getJpegEncodingQualityParameter(arg0: int) -> int: ...
    @overload
    @staticmethod
    def getJpegEncodingQualityParameter(arg0: int, arg1: int) -> int: ...
