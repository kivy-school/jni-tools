from typing import Any, ClassVar, overload

class PixelFormat:
    A_8: ClassVar[int]
    JPEG: ClassVar[int]
    LA_88: ClassVar[int]
    L_8: ClassVar[int]
    OPAQUE: ClassVar[int]
    RGBA_1010102: ClassVar[int]
    RGBA_4444: ClassVar[int]
    RGBA_5551: ClassVar[int]
    RGBA_8888: ClassVar[int]
    RGBA_F16: ClassVar[int]
    RGBX_8888: ClassVar[int]
    RGB_332: ClassVar[int]
    RGB_565: ClassVar[int]
    RGB_888: ClassVar[int]
    TRANSLUCENT: ClassVar[int]
    TRANSPARENT: ClassVar[int]
    UNKNOWN: ClassVar[int]
    YCbCr_420_SP: ClassVar[int]
    YCbCr_422_I: ClassVar[int]
    YCbCr_422_SP: ClassVar[int]
    bitsPerPixel: int
    bytesPerPixel: int
    def __init__(self) -> None: ...
    @staticmethod
    def getPixelFormatInfo(arg0: int, arg1: "PixelFormat") -> None: ...
    @staticmethod
    def formatHasAlpha(arg0: int) -> bool: ...
