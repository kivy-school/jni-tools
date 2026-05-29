from typing import Any, ClassVar, overload
from android.media.EncoderProfiles import EncoderProfiles

class CamcorderProfile:
    QUALITY_1080P: ClassVar[int]
    QUALITY_2160P: ClassVar[int]
    QUALITY_2K: ClassVar[int]
    QUALITY_480P: ClassVar[int]
    QUALITY_4KDCI: ClassVar[int]
    QUALITY_720P: ClassVar[int]
    QUALITY_8KUHD: ClassVar[int]
    QUALITY_CIF: ClassVar[int]
    QUALITY_HIGH: ClassVar[int]
    QUALITY_HIGH_SPEED_1080P: ClassVar[int]
    QUALITY_HIGH_SPEED_2160P: ClassVar[int]
    QUALITY_HIGH_SPEED_480P: ClassVar[int]
    QUALITY_HIGH_SPEED_4KDCI: ClassVar[int]
    QUALITY_HIGH_SPEED_720P: ClassVar[int]
    QUALITY_HIGH_SPEED_CIF: ClassVar[int]
    QUALITY_HIGH_SPEED_HIGH: ClassVar[int]
    QUALITY_HIGH_SPEED_LOW: ClassVar[int]
    QUALITY_HIGH_SPEED_VGA: ClassVar[int]
    QUALITY_LOW: ClassVar[int]
    QUALITY_QCIF: ClassVar[int]
    QUALITY_QHD: ClassVar[int]
    QUALITY_QVGA: ClassVar[int]
    QUALITY_TIME_LAPSE_1080P: ClassVar[int]
    QUALITY_TIME_LAPSE_2160P: ClassVar[int]
    QUALITY_TIME_LAPSE_2K: ClassVar[int]
    QUALITY_TIME_LAPSE_480P: ClassVar[int]
    QUALITY_TIME_LAPSE_4KDCI: ClassVar[int]
    QUALITY_TIME_LAPSE_720P: ClassVar[int]
    QUALITY_TIME_LAPSE_8KUHD: ClassVar[int]
    QUALITY_TIME_LAPSE_CIF: ClassVar[int]
    QUALITY_TIME_LAPSE_HIGH: ClassVar[int]
    QUALITY_TIME_LAPSE_LOW: ClassVar[int]
    QUALITY_TIME_LAPSE_QCIF: ClassVar[int]
    QUALITY_TIME_LAPSE_QHD: ClassVar[int]
    QUALITY_TIME_LAPSE_QVGA: ClassVar[int]
    QUALITY_TIME_LAPSE_VGA: ClassVar[int]
    QUALITY_VGA: ClassVar[int]
    audioBitRate: int
    audioChannels: int
    audioCodec: int
    audioSampleRate: int
    duration: int
    fileFormat: int
    quality: int
    videoBitRate: int
    videoCodec: int
    videoFrameHeight: int
    videoFrameRate: int
    videoFrameWidth: int
    @staticmethod
    def getAll(p0: str, p1: int) -> EncoderProfiles: ...
    @overload
    @staticmethod
    def hasProfile(p0: int) -> bool: ...
    @overload
    @staticmethod
    def hasProfile(p0: int, p1: int) -> bool: ...
    @overload
    @staticmethod
    def get(p0: int) -> "CamcorderProfile": ...
    @overload
    @staticmethod
    def get(p0: int, p1: int) -> "CamcorderProfile": ...
