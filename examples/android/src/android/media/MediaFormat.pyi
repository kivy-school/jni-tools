from typing import Any, ClassVar, overload
from android.graphics.Rect import Rect
from java.nio.ByteBuffer import ByteBuffer

class MediaFormat:
    COLOR_RANGE_FULL: ClassVar[int]
    COLOR_RANGE_LIMITED: ClassVar[int]
    COLOR_STANDARD_BT2020: ClassVar[int]
    COLOR_STANDARD_BT601_NTSC: ClassVar[int]
    COLOR_STANDARD_BT601_PAL: ClassVar[int]
    COLOR_STANDARD_BT709: ClassVar[int]
    COLOR_TRANSFER_HLG: ClassVar[int]
    COLOR_TRANSFER_LINEAR: ClassVar[int]
    COLOR_TRANSFER_SDR_VIDEO: ClassVar[int]
    COLOR_TRANSFER_ST2084: ClassVar[int]
    KEY_AAC_DRC_ALBUM_MODE: ClassVar[str]
    KEY_AAC_DRC_ATTENUATION_FACTOR: ClassVar[str]
    KEY_AAC_DRC_BOOST_FACTOR: ClassVar[str]
    KEY_AAC_DRC_EFFECT_TYPE: ClassVar[str]
    KEY_AAC_DRC_HEAVY_COMPRESSION: ClassVar[str]
    KEY_AAC_DRC_OUTPUT_LOUDNESS: ClassVar[str]
    KEY_AAC_DRC_TARGET_REFERENCE_LEVEL: ClassVar[str]
    KEY_AAC_ENCODED_TARGET_LEVEL: ClassVar[str]
    KEY_AAC_MAX_OUTPUT_CHANNEL_COUNT: ClassVar[str]
    KEY_AAC_PROFILE: ClassVar[str]
    KEY_AAC_SBR_MODE: ClassVar[str]
    KEY_ALLOW_FRAME_DROP: ClassVar[str]
    KEY_AUDIO_SESSION_ID: ClassVar[str]
    KEY_BITRATE_MODE: ClassVar[str]
    KEY_BIT_RATE: ClassVar[str]
    KEY_BUFFER_BATCH_MAX_OUTPUT_SIZE: ClassVar[str]
    KEY_BUFFER_BATCH_THRESHOLD_OUTPUT_SIZE: ClassVar[str]
    KEY_CAPTION_SERVICE_NUMBER: ClassVar[str]
    KEY_CAPTURE_RATE: ClassVar[str]
    KEY_CHANNEL_COUNT: ClassVar[str]
    KEY_CHANNEL_MASK: ClassVar[str]
    KEY_CODECS_STRING: ClassVar[str]
    KEY_COLOR_FORMAT: ClassVar[str]
    KEY_COLOR_RANGE: ClassVar[str]
    KEY_COLOR_STANDARD: ClassVar[str]
    KEY_COLOR_TRANSFER: ClassVar[str]
    KEY_COLOR_TRANSFER_REQUEST: ClassVar[str]
    KEY_COMPLEXITY: ClassVar[str]
    KEY_CREATE_INPUT_SURFACE_SUSPENDED: ClassVar[str]
    KEY_CROP_BOTTOM: ClassVar[str]
    KEY_CROP_LEFT: ClassVar[str]
    KEY_CROP_RIGHT: ClassVar[str]
    KEY_CROP_TOP: ClassVar[str]
    KEY_DURATION: ClassVar[str]
    KEY_ENCODER_DELAY: ClassVar[str]
    KEY_ENCODER_PADDING: ClassVar[str]
    KEY_FLAC_COMPRESSION_LEVEL: ClassVar[str]
    KEY_FRAME_RATE: ClassVar[str]
    KEY_GRID_COLUMNS: ClassVar[str]
    KEY_GRID_ROWS: ClassVar[str]
    KEY_HAPTIC_CHANNEL_COUNT: ClassVar[str]
    KEY_HARDWARE_AV_SYNC_ID: ClassVar[str]
    KEY_HDR10_PLUS_INFO: ClassVar[str]
    KEY_HDR_STATIC_INFO: ClassVar[str]
    KEY_HEIGHT: ClassVar[str]
    KEY_IMPORTANCE: ClassVar[str]
    KEY_INTRA_REFRESH_PERIOD: ClassVar[str]
    KEY_IS_ADTS: ClassVar[str]
    KEY_IS_AUTOSELECT: ClassVar[str]
    KEY_IS_DEFAULT: ClassVar[str]
    KEY_IS_FORCED_SUBTITLE: ClassVar[str]
    KEY_I_FRAME_INTERVAL: ClassVar[str]
    KEY_LANGUAGE: ClassVar[str]
    KEY_LATENCY: ClassVar[str]
    KEY_LEVEL: ClassVar[str]
    KEY_LOW_LATENCY: ClassVar[str]
    KEY_MAX_B_FRAMES: ClassVar[str]
    KEY_MAX_FPS_TO_ENCODER: ClassVar[str]
    KEY_MAX_HEIGHT: ClassVar[str]
    KEY_MAX_INPUT_SIZE: ClassVar[str]
    KEY_MAX_OUTPUT_CHANNEL_COUNT: ClassVar[str]
    KEY_MAX_PTS_GAP_TO_ENCODER: ClassVar[str]
    KEY_MAX_WIDTH: ClassVar[str]
    KEY_MIME: ClassVar[str]
    KEY_MPEGH_COMPATIBLE_SETS: ClassVar[str]
    KEY_MPEGH_PROFILE_LEVEL_INDICATION: ClassVar[str]
    KEY_MPEGH_REFERENCE_CHANNEL_LAYOUT: ClassVar[str]
    KEY_OPERATING_RATE: ClassVar[str]
    KEY_OUTPUT_REORDER_DEPTH: ClassVar[str]
    KEY_PCM_ENCODING: ClassVar[str]
    KEY_PICTURE_TYPE: ClassVar[str]
    KEY_PIXEL_ASPECT_RATIO_HEIGHT: ClassVar[str]
    KEY_PIXEL_ASPECT_RATIO_WIDTH: ClassVar[str]
    KEY_PREPEND_HEADER_TO_SYNC_FRAMES: ClassVar[str]
    KEY_PRIORITY: ClassVar[str]
    KEY_PROFILE: ClassVar[str]
    KEY_PUSH_BLANK_BUFFERS_ON_STOP: ClassVar[str]
    KEY_QUALITY: ClassVar[str]
    KEY_REPEAT_PREVIOUS_FRAME_AFTER: ClassVar[str]
    KEY_ROTATION: ClassVar[str]
    KEY_SAMPLE_RATE: ClassVar[str]
    KEY_SLICE_HEIGHT: ClassVar[str]
    KEY_SLOW_MOTION_MARKERS: ClassVar[str]
    KEY_STRIDE: ClassVar[str]
    KEY_TEMPORAL_LAYERING: ClassVar[str]
    KEY_TILE_HEIGHT: ClassVar[str]
    KEY_TILE_WIDTH: ClassVar[str]
    KEY_TRACK_ID: ClassVar[str]
    KEY_VIDEO_ENCODING_STATISTICS_LEVEL: ClassVar[str]
    KEY_VIDEO_QP_AVERAGE: ClassVar[str]
    KEY_VIDEO_QP_B_MAX: ClassVar[str]
    KEY_VIDEO_QP_B_MIN: ClassVar[str]
    KEY_VIDEO_QP_I_MAX: ClassVar[str]
    KEY_VIDEO_QP_I_MIN: ClassVar[str]
    KEY_VIDEO_QP_MAX: ClassVar[str]
    KEY_VIDEO_QP_MIN: ClassVar[str]
    KEY_VIDEO_QP_P_MAX: ClassVar[str]
    KEY_VIDEO_QP_P_MIN: ClassVar[str]
    KEY_WIDTH: ClassVar[str]
    LOG_SESSION_ID: ClassVar[str]
    MIMETYPE_AUDIO_AAC: ClassVar[str]
    MIMETYPE_AUDIO_AAC_ELD: ClassVar[str]
    MIMETYPE_AUDIO_AAC_HE_V1: ClassVar[str]
    MIMETYPE_AUDIO_AAC_HE_V2: ClassVar[str]
    MIMETYPE_AUDIO_AAC_LC: ClassVar[str]
    MIMETYPE_AUDIO_AAC_XHE: ClassVar[str]
    MIMETYPE_AUDIO_AC3: ClassVar[str]
    MIMETYPE_AUDIO_AC4: ClassVar[str]
    MIMETYPE_AUDIO_AMR_NB: ClassVar[str]
    MIMETYPE_AUDIO_AMR_WB: ClassVar[str]
    MIMETYPE_AUDIO_DOLBY_MAT: ClassVar[str]
    MIMETYPE_AUDIO_DOLBY_TRUEHD: ClassVar[str]
    MIMETYPE_AUDIO_DRA: ClassVar[str]
    MIMETYPE_AUDIO_DTS: ClassVar[str]
    MIMETYPE_AUDIO_DTS_HD: ClassVar[str]
    MIMETYPE_AUDIO_DTS_UHD: ClassVar[str]
    MIMETYPE_AUDIO_EAC3: ClassVar[str]
    MIMETYPE_AUDIO_EAC3_JOC: ClassVar[str]
    MIMETYPE_AUDIO_FLAC: ClassVar[str]
    MIMETYPE_AUDIO_G711_ALAW: ClassVar[str]
    MIMETYPE_AUDIO_G711_MLAW: ClassVar[str]
    MIMETYPE_AUDIO_IEC61937: ClassVar[str]
    MIMETYPE_AUDIO_MPEG: ClassVar[str]
    MIMETYPE_AUDIO_MPEGH_BL_L3: ClassVar[str]
    MIMETYPE_AUDIO_MPEGH_BL_L4: ClassVar[str]
    MIMETYPE_AUDIO_MPEGH_LC_L3: ClassVar[str]
    MIMETYPE_AUDIO_MPEGH_LC_L4: ClassVar[str]
    MIMETYPE_AUDIO_MPEGH_MHA1: ClassVar[str]
    MIMETYPE_AUDIO_MPEGH_MHM1: ClassVar[str]
    MIMETYPE_AUDIO_MSGSM: ClassVar[str]
    MIMETYPE_AUDIO_OPUS: ClassVar[str]
    MIMETYPE_AUDIO_QCELP: ClassVar[str]
    MIMETYPE_AUDIO_RAW: ClassVar[str]
    MIMETYPE_AUDIO_SCRAMBLED: ClassVar[str]
    MIMETYPE_AUDIO_VORBIS: ClassVar[str]
    MIMETYPE_IMAGE_ANDROID_HEIC: ClassVar[str]
    MIMETYPE_IMAGE_AVIF: ClassVar[str]
    MIMETYPE_TEXT_CEA_608: ClassVar[str]
    MIMETYPE_TEXT_CEA_708: ClassVar[str]
    MIMETYPE_TEXT_SUBRIP: ClassVar[str]
    MIMETYPE_TEXT_VTT: ClassVar[str]
    MIMETYPE_VIDEO_AV1: ClassVar[str]
    MIMETYPE_VIDEO_AVC: ClassVar[str]
    MIMETYPE_VIDEO_DOLBY_VISION: ClassVar[str]
    MIMETYPE_VIDEO_H263: ClassVar[str]
    MIMETYPE_VIDEO_HEVC: ClassVar[str]
    MIMETYPE_VIDEO_MPEG2: ClassVar[str]
    MIMETYPE_VIDEO_MPEG4: ClassVar[str]
    MIMETYPE_VIDEO_RAW: ClassVar[str]
    MIMETYPE_VIDEO_SCRAMBLED: ClassVar[str]
    MIMETYPE_VIDEO_VP8: ClassVar[str]
    MIMETYPE_VIDEO_VP9: ClassVar[str]
    PICTURE_TYPE_B: ClassVar[int]
    PICTURE_TYPE_I: ClassVar[int]
    PICTURE_TYPE_P: ClassVar[int]
    PICTURE_TYPE_UNKNOWN: ClassVar[int]
    TYPE_BYTE_BUFFER: ClassVar[int]
    TYPE_FLOAT: ClassVar[int]
    TYPE_INTEGER: ClassVar[int]
    TYPE_LONG: ClassVar[int]
    TYPE_NULL: ClassVar[int]
    TYPE_STRING: ClassVar[int]
    VIDEO_ENCODING_STATISTICS_LEVEL_1: ClassVar[int]
    VIDEO_ENCODING_STATISTICS_LEVEL_NONE: ClassVar[int]
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, arg0: "MediaFormat") -> None: ...
    def containsKey(self, arg0: str) -> bool: ...
    def containsFeature(self, arg0: str) -> bool: ...
    def getValueTypeForKey(self, arg0: str) -> int: ...
    @overload
    def getNumber(self, arg0: str) -> float: ...
    @overload
    def getNumber(self, arg0: str, arg1: float) -> float: ...
    @overload
    def getInteger(self, arg0: str) -> int: ...
    @overload
    def getInteger(self, arg0: str, arg1: int) -> int: ...
    @overload
    def getLong(self, arg0: str) -> int: ...
    @overload
    def getLong(self, arg0: str, arg1: int) -> int: ...
    @overload
    def getFloat(self, arg0: str) -> float: ...
    @overload
    def getFloat(self, arg0: str, arg1: float) -> float: ...
    @overload
    def getString(self, arg0: str) -> str: ...
    @overload
    def getString(self, arg0: str, arg1: str) -> str: ...
    @overload
    def getByteBuffer(self, arg0: str) -> ByteBuffer: ...
    @overload
    def getByteBuffer(self, arg0: str, arg1: ByteBuffer) -> ByteBuffer: ...
    def getFeatureEnabled(self, arg0: str) -> bool: ...
    def setInteger(self, arg0: str, arg1: int) -> None: ...
    def setLong(self, arg0: str, arg1: int) -> None: ...
    def setFloat(self, arg0: str, arg1: float) -> None: ...
    def setString(self, arg0: str, arg1: str) -> None: ...
    def setByteBuffer(self, arg0: str, arg1: ByteBuffer) -> None: ...
    def removeKey(self, arg0: str) -> None: ...
    def removeFeature(self, arg0: str) -> None: ...
    def getKeys(self) -> set: ...
    def getFeatures(self) -> set: ...
    def setFeatureEnabled(self, arg0: str, arg1: bool) -> None: ...
    @staticmethod
    def createAudioFormat(arg0: str, arg1: int, arg2: int) -> "MediaFormat": ...
    @staticmethod
    def createSubtitleFormat(arg0: str, arg1: str) -> "MediaFormat": ...
    @staticmethod
    def createVideoFormat(arg0: str, arg1: int, arg2: int) -> "MediaFormat": ...
    def toString(self) -> str: ...

    class QpOffsetRect:
        def __init__(self, arg0: Rect, arg1: int) -> None: ...
        def set(self, arg0: Rect, arg1: int) -> None: ...
        @overload
        def flattenToString(self) -> str: ...
        @overload
        @staticmethod
        def flattenToString(arg0: list) -> str: ...
