from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel

class AudioFormat:
    CHANNEL_CONFIGURATION_DEFAULT: ClassVar[int]
    CHANNEL_CONFIGURATION_INVALID: ClassVar[int]
    CHANNEL_CONFIGURATION_MONO: ClassVar[int]
    CHANNEL_CONFIGURATION_STEREO: ClassVar[int]
    CHANNEL_INVALID: ClassVar[int]
    CHANNEL_IN_BACK: ClassVar[int]
    CHANNEL_IN_BACK_PROCESSED: ClassVar[int]
    CHANNEL_IN_DEFAULT: ClassVar[int]
    CHANNEL_IN_FRONT: ClassVar[int]
    CHANNEL_IN_FRONT_PROCESSED: ClassVar[int]
    CHANNEL_IN_LEFT: ClassVar[int]
    CHANNEL_IN_LEFT_PROCESSED: ClassVar[int]
    CHANNEL_IN_MONO: ClassVar[int]
    CHANNEL_IN_PRESSURE: ClassVar[int]
    CHANNEL_IN_RIGHT: ClassVar[int]
    CHANNEL_IN_RIGHT_PROCESSED: ClassVar[int]
    CHANNEL_IN_STEREO: ClassVar[int]
    CHANNEL_IN_VOICE_DNLINK: ClassVar[int]
    CHANNEL_IN_VOICE_UPLINK: ClassVar[int]
    CHANNEL_IN_X_AXIS: ClassVar[int]
    CHANNEL_IN_Y_AXIS: ClassVar[int]
    CHANNEL_IN_Z_AXIS: ClassVar[int]
    CHANNEL_OUT_5POINT1: ClassVar[int]
    CHANNEL_OUT_5POINT1POINT2: ClassVar[int]
    CHANNEL_OUT_5POINT1POINT4: ClassVar[int]
    CHANNEL_OUT_6POINT1: ClassVar[int]
    CHANNEL_OUT_7POINT1: ClassVar[int]
    CHANNEL_OUT_7POINT1POINT2: ClassVar[int]
    CHANNEL_OUT_7POINT1POINT4: ClassVar[int]
    CHANNEL_OUT_7POINT1_SURROUND: ClassVar[int]
    CHANNEL_OUT_9POINT1POINT4: ClassVar[int]
    CHANNEL_OUT_9POINT1POINT6: ClassVar[int]
    CHANNEL_OUT_BACK_CENTER: ClassVar[int]
    CHANNEL_OUT_BACK_LEFT: ClassVar[int]
    CHANNEL_OUT_BACK_RIGHT: ClassVar[int]
    CHANNEL_OUT_BOTTOM_FRONT_CENTER: ClassVar[int]
    CHANNEL_OUT_BOTTOM_FRONT_LEFT: ClassVar[int]
    CHANNEL_OUT_BOTTOM_FRONT_RIGHT: ClassVar[int]
    CHANNEL_OUT_DEFAULT: ClassVar[int]
    CHANNEL_OUT_FRONT_CENTER: ClassVar[int]
    CHANNEL_OUT_FRONT_LEFT: ClassVar[int]
    CHANNEL_OUT_FRONT_LEFT_OF_CENTER: ClassVar[int]
    CHANNEL_OUT_FRONT_RIGHT: ClassVar[int]
    CHANNEL_OUT_FRONT_RIGHT_OF_CENTER: ClassVar[int]
    CHANNEL_OUT_FRONT_WIDE_LEFT: ClassVar[int]
    CHANNEL_OUT_FRONT_WIDE_RIGHT: ClassVar[int]
    CHANNEL_OUT_LOW_FREQUENCY: ClassVar[int]
    CHANNEL_OUT_LOW_FREQUENCY_2: ClassVar[int]
    CHANNEL_OUT_MONO: ClassVar[int]
    CHANNEL_OUT_QUAD: ClassVar[int]
    CHANNEL_OUT_SIDE_LEFT: ClassVar[int]
    CHANNEL_OUT_SIDE_RIGHT: ClassVar[int]
    CHANNEL_OUT_STEREO: ClassVar[int]
    CHANNEL_OUT_SURROUND: ClassVar[int]
    CHANNEL_OUT_TOP_BACK_CENTER: ClassVar[int]
    CHANNEL_OUT_TOP_BACK_LEFT: ClassVar[int]
    CHANNEL_OUT_TOP_BACK_RIGHT: ClassVar[int]
    CHANNEL_OUT_TOP_CENTER: ClassVar[int]
    CHANNEL_OUT_TOP_FRONT_CENTER: ClassVar[int]
    CHANNEL_OUT_TOP_FRONT_LEFT: ClassVar[int]
    CHANNEL_OUT_TOP_FRONT_RIGHT: ClassVar[int]
    CHANNEL_OUT_TOP_SIDE_LEFT: ClassVar[int]
    CHANNEL_OUT_TOP_SIDE_RIGHT: ClassVar[int]
    CREATOR: ClassVar[Any]
    ENCODING_AAC_ELD: ClassVar[int]
    ENCODING_AAC_HE_V1: ClassVar[int]
    ENCODING_AAC_HE_V2: ClassVar[int]
    ENCODING_AAC_LC: ClassVar[int]
    ENCODING_AAC_XHE: ClassVar[int]
    ENCODING_AC3: ClassVar[int]
    ENCODING_AC4: ClassVar[int]
    ENCODING_DEFAULT: ClassVar[int]
    ENCODING_DOLBY_MAT: ClassVar[int]
    ENCODING_DOLBY_TRUEHD: ClassVar[int]
    ENCODING_DRA: ClassVar[int]
    ENCODING_DSD: ClassVar[int]
    ENCODING_DTS: ClassVar[int]
    ENCODING_DTS_HD: ClassVar[int]
    ENCODING_DTS_HD_MA: ClassVar[int]
    ENCODING_DTS_UHD: ClassVar[int]
    ENCODING_DTS_UHD_P1: ClassVar[int]
    ENCODING_DTS_UHD_P2: ClassVar[int]
    ENCODING_E_AC3: ClassVar[int]
    ENCODING_E_AC3_JOC: ClassVar[int]
    ENCODING_IEC61937: ClassVar[int]
    ENCODING_INVALID: ClassVar[int]
    ENCODING_MP3: ClassVar[int]
    ENCODING_MPEGH_BL_L3: ClassVar[int]
    ENCODING_MPEGH_BL_L4: ClassVar[int]
    ENCODING_MPEGH_LC_L3: ClassVar[int]
    ENCODING_MPEGH_LC_L4: ClassVar[int]
    ENCODING_OPUS: ClassVar[int]
    ENCODING_PCM_16BIT: ClassVar[int]
    ENCODING_PCM_24BIT_PACKED: ClassVar[int]
    ENCODING_PCM_32BIT: ClassVar[int]
    ENCODING_PCM_8BIT: ClassVar[int]
    ENCODING_PCM_FLOAT: ClassVar[int]
    SAMPLE_RATE_UNSPECIFIED: ClassVar[int]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    def getChannelMask(self) -> int: ...
    def getChannelIndexMask(self) -> int: ...
    def getFrameSizeInBytes(self) -> int: ...
    def getSampleRate(self) -> int: ...
    def getChannelCount(self) -> int: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...
    def getEncoding(self) -> int: ...
    def equals(self, p0: Any) -> bool: ...
    def toString(self) -> str: ...
    def hashCode(self) -> int: ...

    class Builder:
        @overload
        def __init__(self, p0: "AudioFormat") -> None: ...
        @overload
        def __init__(self) -> None: ...
        def setChannelMask(self, p0: int) -> Any: ...
        def setChannelIndexMask(self, p0: int) -> Any: ...
        def setSampleRate(self, p0: int) -> Any: ...
        def setEncoding(self, p0: int) -> Any: ...
        def build(self) -> "AudioFormat": ...
