from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel

class HardwareBuffer:
    BLOB: ClassVar[int]
    CREATOR: ClassVar[Any]
    DS_24UI8: ClassVar[int]
    DS_FP32UI8: ClassVar[int]
    D_16: ClassVar[int]
    D_24: ClassVar[int]
    D_FP32: ClassVar[int]
    RGBA_10101010: ClassVar[int]
    RGBA_1010102: ClassVar[int]
    RGBA_8888: ClassVar[int]
    RGBA_FP16: ClassVar[int]
    RGBX_8888: ClassVar[int]
    RGB_565: ClassVar[int]
    RGB_888: ClassVar[int]
    RG_1616: ClassVar[int]
    R_16: ClassVar[int]
    R_8: ClassVar[int]
    S_UI8: ClassVar[int]
    USAGE_COMPOSER_OVERLAY: ClassVar[int]
    USAGE_CPU_READ_OFTEN: ClassVar[int]
    USAGE_CPU_READ_RARELY: ClassVar[int]
    USAGE_CPU_WRITE_OFTEN: ClassVar[int]
    USAGE_CPU_WRITE_RARELY: ClassVar[int]
    USAGE_FRONT_BUFFER: ClassVar[int]
    USAGE_GPU_COLOR_OUTPUT: ClassVar[int]
    USAGE_GPU_CUBE_MAP: ClassVar[int]
    USAGE_GPU_DATA_BUFFER: ClassVar[int]
    USAGE_GPU_MIPMAP_COMPLETE: ClassVar[int]
    USAGE_GPU_SAMPLED_IMAGE: ClassVar[int]
    USAGE_PROTECTED_CONTENT: ClassVar[int]
    USAGE_SENSOR_DIRECT_DATA: ClassVar[int]
    USAGE_VIDEO_ENCODE: ClassVar[int]
    YCBCR_420_888: ClassVar[int]
    YCBCR_P010: ClassVar[int]
    YCBCR_P210: ClassVar[int]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    def close(self) -> None: ...
    @staticmethod
    def isSupported(p0: int, p1: int, p2: int, p3: int, p4: int) -> bool: ...
    def getId(self) -> int: ...
    @staticmethod
    def create(p0: int, p1: int, p2: int, p3: int, p4: int) -> "HardwareBuffer": ...
    def getFormat(self) -> int: ...
    def isClosed(self) -> bool: ...
    def getLayers(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...
    def describeContents(self) -> int: ...
    def getUsage(self) -> int: ...
    def getHeight(self) -> int: ...
    def getWidth(self) -> int: ...
