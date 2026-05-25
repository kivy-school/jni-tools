from typing import Any, ClassVar, overload

class ImageFormat:
    DEPTH16: ClassVar[int]
    DEPTH_JPEG: ClassVar[int]
    DEPTH_POINT_CLOUD: ClassVar[int]
    FLEX_RGBA_8888: ClassVar[int]
    FLEX_RGB_888: ClassVar[int]
    HEIC: ClassVar[int]
    JPEG: ClassVar[int]
    JPEG_R: ClassVar[int]
    NV16: ClassVar[int]
    NV21: ClassVar[int]
    PRIVATE: ClassVar[int]
    RAW10: ClassVar[int]
    RAW12: ClassVar[int]
    RAW_PRIVATE: ClassVar[int]
    RAW_SENSOR: ClassVar[int]
    RGB_565: ClassVar[int]
    UNKNOWN: ClassVar[int]
    Y8: ClassVar[int]
    YCBCR_P010: ClassVar[int]
    YUV_420_888: ClassVar[int]
    YUV_422_888: ClassVar[int]
    YUV_444_888: ClassVar[int]
    YUY2: ClassVar[int]
    YV12: ClassVar[int]
    def __init__(self) -> None: ...
    @staticmethod
    def getBitsPerPixel(p0: int) -> int: ...
