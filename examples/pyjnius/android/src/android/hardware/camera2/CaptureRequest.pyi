from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel
from android.view.Surface import Surface

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

class CaptureRequest:
    BLACK_LEVEL_LOCK: ClassVar["Key"]
    COLOR_CORRECTION_ABERRATION_MODE: ClassVar["Key"]
    COLOR_CORRECTION_GAINS: ClassVar["Key"]
    COLOR_CORRECTION_MODE: ClassVar["Key"]
    COLOR_CORRECTION_TRANSFORM: ClassVar["Key"]
    CONTROL_AE_ANTIBANDING_MODE: ClassVar["Key"]
    CONTROL_AE_EXPOSURE_COMPENSATION: ClassVar["Key"]
    CONTROL_AE_LOCK: ClassVar["Key"]
    CONTROL_AE_MODE: ClassVar["Key"]
    CONTROL_AE_PRECAPTURE_TRIGGER: ClassVar["Key"]
    CONTROL_AE_REGIONS: ClassVar["Key"]
    CONTROL_AE_TARGET_FPS_RANGE: ClassVar["Key"]
    CONTROL_AF_MODE: ClassVar["Key"]
    CONTROL_AF_REGIONS: ClassVar["Key"]
    CONTROL_AF_TRIGGER: ClassVar["Key"]
    CONTROL_AUTOFRAMING: ClassVar["Key"]
    CONTROL_AWB_LOCK: ClassVar["Key"]
    CONTROL_AWB_MODE: ClassVar["Key"]
    CONTROL_AWB_REGIONS: ClassVar["Key"]
    CONTROL_CAPTURE_INTENT: ClassVar["Key"]
    CONTROL_EFFECT_MODE: ClassVar["Key"]
    CONTROL_ENABLE_ZSL: ClassVar["Key"]
    CONTROL_EXTENDED_SCENE_MODE: ClassVar["Key"]
    CONTROL_MODE: ClassVar["Key"]
    CONTROL_POST_RAW_SENSITIVITY_BOOST: ClassVar["Key"]
    CONTROL_SCENE_MODE: ClassVar["Key"]
    CONTROL_SETTINGS_OVERRIDE: ClassVar["Key"]
    CONTROL_VIDEO_STABILIZATION_MODE: ClassVar["Key"]
    CONTROL_ZOOM_RATIO: ClassVar["Key"]
    CREATOR: ClassVar[Creator]
    DISTORTION_CORRECTION_MODE: ClassVar["Key"]
    EDGE_MODE: ClassVar["Key"]
    EXTENSION_STRENGTH: ClassVar["Key"]
    FLASH_MODE: ClassVar["Key"]
    FLASH_STRENGTH_LEVEL: ClassVar["Key"]
    HOT_PIXEL_MODE: ClassVar["Key"]
    JPEG_GPS_LOCATION: ClassVar["Key"]
    JPEG_ORIENTATION: ClassVar["Key"]
    JPEG_QUALITY: ClassVar["Key"]
    JPEG_THUMBNAIL_QUALITY: ClassVar["Key"]
    JPEG_THUMBNAIL_SIZE: ClassVar["Key"]
    LENS_APERTURE: ClassVar["Key"]
    LENS_FILTER_DENSITY: ClassVar["Key"]
    LENS_FOCAL_LENGTH: ClassVar["Key"]
    LENS_FOCUS_DISTANCE: ClassVar["Key"]
    LENS_OPTICAL_STABILIZATION_MODE: ClassVar["Key"]
    NOISE_REDUCTION_MODE: ClassVar["Key"]
    REPROCESS_EFFECTIVE_EXPOSURE_FACTOR: ClassVar["Key"]
    SCALER_CROP_REGION: ClassVar["Key"]
    SCALER_ROTATE_AND_CROP: ClassVar["Key"]
    SENSOR_EXPOSURE_TIME: ClassVar["Key"]
    SENSOR_FRAME_DURATION: ClassVar["Key"]
    SENSOR_PIXEL_MODE: ClassVar["Key"]
    SENSOR_SENSITIVITY: ClassVar["Key"]
    SENSOR_TEST_PATTERN_DATA: ClassVar["Key"]
    SENSOR_TEST_PATTERN_MODE: ClassVar["Key"]
    SHADING_MODE: ClassVar["Key"]
    STATISTICS_FACE_DETECT_MODE: ClassVar["Key"]
    STATISTICS_HOT_PIXEL_MAP_MODE: ClassVar["Key"]
    STATISTICS_LENS_SHADING_MAP_MODE: ClassVar["Key"]
    STATISTICS_OIS_DATA_MODE: ClassVar["Key"]
    TONEMAP_CURVE: ClassVar["Key"]
    TONEMAP_GAMMA: ClassVar["Key"]
    TONEMAP_MODE: ClassVar["Key"]
    TONEMAP_PRESET_CURVE: ClassVar["Key"]
    def get(self, arg0: "Key") -> Any: ...
    def getKeys(self) -> list: ...
    def getTag(self) -> Any: ...
    def isReprocess(self) -> bool: ...
    def equals(self, arg0: Any) -> bool: ...
    def hashCode(self) -> int: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, arg0: Parcel, arg1: int) -> None: ...
    def finalize(self) -> None: ...

    class Builder:
        def addTarget(self, arg0: Surface) -> None: ...
        def removeTarget(self, arg0: Surface) -> None: ...
        def set(self, arg0: "Key", arg1: Any) -> None: ...
        def get(self, arg0: "Key") -> Any: ...
        def setPhysicalCameraKey(self, arg0: "Key", arg1: Any, arg2: str) -> "Builder": ...
        def getPhysicalCameraKey(self, arg0: "Key", arg1: str) -> Any: ...
        def setTag(self, arg0: Any) -> None: ...
        def build(self) -> "CaptureRequest": ...

    class Key:
        def __init__(self, arg0: str, arg1: type) -> None: ...
        def getName(self) -> str: ...
        def hashCode(self) -> int: ...
        def equals(self, arg0: Any) -> bool: ...
        def toString(self) -> str: ...
