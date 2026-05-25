from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Creator:
    """Forward declaration for ``android.os.Parcelable.Creator``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.os.Parcelable.Creator')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/os/Parcelable/Creator
    """
    ...

class HardwareBuffer:
    BLOB: ClassVar[int]
    CREATOR: ClassVar[Creator]
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
    @staticmethod
    def create(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> "HardwareBuffer": ...
    @staticmethod
    def isSupported(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> bool: ...
    def finalize(self) -> None: ...
    def getWidth(self) -> int: ...
    def getHeight(self) -> int: ...
    def getFormat(self) -> int: ...
    def getLayers(self) -> int: ...
    def getUsage(self) -> int: ...
    def getId(self) -> int: ...
    def close(self) -> None: ...
    def isClosed(self) -> bool: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, arg0: Parcel, arg1: int) -> None: ...
