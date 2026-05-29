from typing import Any, ClassVar, overload
from android.media.tv.TvContentRating import TvContentRating
from android.media.tv.TvInputInfo import TvInputInfo
from android.os.Handler import Handler

class TvInputManager:
    ACTION_BLOCKED_RATINGS_CHANGED: ClassVar[str]
    ACTION_PARENTAL_CONTROLS_ENABLED_CHANGED: ClassVar[str]
    ACTION_QUERY_CONTENT_RATING_SYSTEMS: ClassVar[str]
    ACTION_SETUP_INPUTS: ClassVar[str]
    ACTION_VIEW_RECORDING_SCHEDULES: ClassVar[str]
    BROADCAST_INFO_STREAM_EVENT: ClassVar[int]
    BROADCAST_INFO_TYPE_COMMAND: ClassVar[int]
    BROADCAST_INFO_TYPE_DSMCC: ClassVar[int]
    BROADCAST_INFO_TYPE_PES: ClassVar[int]
    BROADCAST_INFO_TYPE_SECTION: ClassVar[int]
    BROADCAST_INFO_TYPE_TABLE: ClassVar[int]
    BROADCAST_INFO_TYPE_TIMELINE: ClassVar[int]
    BROADCAST_INFO_TYPE_TS: ClassVar[int]
    INPUT_STATE_CONNECTED: ClassVar[int]
    INPUT_STATE_CONNECTED_STANDBY: ClassVar[int]
    INPUT_STATE_DISCONNECTED: ClassVar[int]
    META_DATA_CONTENT_RATING_SYSTEMS: ClassVar[str]
    RECORDING_ERROR_INSUFFICIENT_SPACE: ClassVar[int]
    RECORDING_ERROR_RESOURCE_BUSY: ClassVar[int]
    RECORDING_ERROR_UNKNOWN: ClassVar[int]
    SESSION_DATA_KEY_AD_BUFFER: ClassVar[str]
    SESSION_DATA_KEY_AD_RESPONSE: ClassVar[str]
    SESSION_DATA_KEY_BROADCAST_INFO_RESPONSE: ClassVar[str]
    SESSION_DATA_KEY_CHANNEL_URI: ClassVar[str]
    SESSION_DATA_KEY_TRACKS: ClassVar[str]
    SESSION_DATA_KEY_TRACK_ID: ClassVar[str]
    SESSION_DATA_KEY_TRACK_TYPE: ClassVar[str]
    SESSION_DATA_KEY_TV_MESSAGE_TYPE: ClassVar[str]
    SESSION_DATA_KEY_VIDEO_UNAVAILABLE_REASON: ClassVar[str]
    SESSION_DATA_TYPE_AD_BUFFER_CONSUMED: ClassVar[str]
    SESSION_DATA_TYPE_AD_RESPONSE: ClassVar[str]
    SESSION_DATA_TYPE_BROADCAST_INFO_RESPONSE: ClassVar[str]
    SESSION_DATA_TYPE_TRACKS_CHANGED: ClassVar[str]
    SESSION_DATA_TYPE_TRACK_SELECTED: ClassVar[str]
    SESSION_DATA_TYPE_TUNED: ClassVar[str]
    SESSION_DATA_TYPE_TV_MESSAGE: ClassVar[str]
    SESSION_DATA_TYPE_VIDEO_AVAILABLE: ClassVar[str]
    SESSION_DATA_TYPE_VIDEO_UNAVAILABLE: ClassVar[str]
    SIGNAL_STRENGTH_LOST: ClassVar[int]
    SIGNAL_STRENGTH_STRONG: ClassVar[int]
    SIGNAL_STRENGTH_WEAK: ClassVar[int]
    TIME_SHIFT_INVALID_TIME: ClassVar[int]
    TIME_SHIFT_MODE_AUTO: ClassVar[int]
    TIME_SHIFT_MODE_LOCAL: ClassVar[int]
    TIME_SHIFT_MODE_NETWORK: ClassVar[int]
    TIME_SHIFT_MODE_OFF: ClassVar[int]
    TIME_SHIFT_STATUS_AVAILABLE: ClassVar[int]
    TIME_SHIFT_STATUS_UNAVAILABLE: ClassVar[int]
    TIME_SHIFT_STATUS_UNKNOWN: ClassVar[int]
    TIME_SHIFT_STATUS_UNSUPPORTED: ClassVar[int]
    TV_MESSAGE_GROUP_ID_NONE: ClassVar[int]
    TV_MESSAGE_KEY_GROUP_ID: ClassVar[str]
    TV_MESSAGE_KEY_RAW_DATA: ClassVar[str]
    TV_MESSAGE_KEY_STREAM_ID: ClassVar[str]
    TV_MESSAGE_KEY_SUBTYPE: ClassVar[str]
    TV_MESSAGE_SUBTYPE_CC_608E: ClassVar[str]
    TV_MESSAGE_SUBTYPE_WATERMARKING_A335: ClassVar[str]
    TV_MESSAGE_TYPE_CLOSED_CAPTION: ClassVar[int]
    TV_MESSAGE_TYPE_OTHER: ClassVar[int]
    TV_MESSAGE_TYPE_WATERMARK: ClassVar[int]
    VIDEO_UNAVAILABLE_REASON_AUDIO_ONLY: ClassVar[int]
    VIDEO_UNAVAILABLE_REASON_BUFFERING: ClassVar[int]
    VIDEO_UNAVAILABLE_REASON_CAS_BLACKOUT: ClassVar[int]
    VIDEO_UNAVAILABLE_REASON_CAS_CARD_INVALID: ClassVar[int]
    VIDEO_UNAVAILABLE_REASON_CAS_CARD_MUTE: ClassVar[int]
    VIDEO_UNAVAILABLE_REASON_CAS_INSUFFICIENT_OUTPUT_PROTECTION: ClassVar[int]
    VIDEO_UNAVAILABLE_REASON_CAS_LICENSE_EXPIRED: ClassVar[int]
    VIDEO_UNAVAILABLE_REASON_CAS_NEED_ACTIVATION: ClassVar[int]
    VIDEO_UNAVAILABLE_REASON_CAS_NEED_PAIRING: ClassVar[int]
    VIDEO_UNAVAILABLE_REASON_CAS_NO_CARD: ClassVar[int]
    VIDEO_UNAVAILABLE_REASON_CAS_PVR_RECORDING_NOT_ALLOWED: ClassVar[int]
    VIDEO_UNAVAILABLE_REASON_CAS_REBOOTING: ClassVar[int]
    VIDEO_UNAVAILABLE_REASON_CAS_UNKNOWN: ClassVar[int]
    VIDEO_UNAVAILABLE_REASON_INSUFFICIENT_RESOURCE: ClassVar[int]
    VIDEO_UNAVAILABLE_REASON_NOT_CONNECTED: ClassVar[int]
    VIDEO_UNAVAILABLE_REASON_STOPPED: ClassVar[int]
    VIDEO_UNAVAILABLE_REASON_TUNING: ClassVar[int]
    VIDEO_UNAVAILABLE_REASON_UNKNOWN: ClassVar[int]
    VIDEO_UNAVAILABLE_REASON_WEAK_SIGNAL: ClassVar[int]
    def registerCallback(self, p0: Any, p1: Handler) -> None: ...
    def unregisterCallback(self, p0: Any) -> None: ...
    def getBlockedRatings(self) -> list: ...
    def getInputState(self, p0: str) -> int: ...
    def getTvInputInfo(self, p0: str) -> TvInputInfo: ...
    def getTvInputList(self) -> list: ...
    def isParentalControlsEnabled(self) -> bool: ...
    def isRatingBlocked(self, p0: TvContentRating) -> bool: ...
    def updateTvInputInfo(self, p0: TvInputInfo) -> None: ...

    class TvInputCallback:
        def __init__(self) -> None: ...
        def onInputAdded(self, p0: str) -> None: ...
        def onInputUpdated(self, p0: str) -> None: ...
        def onTvInputInfoUpdated(self, p0: TvInputInfo) -> None: ...
        def onInputStateChanged(self, p0: str, p1: int) -> None: ...
        def onInputRemoved(self, p0: str) -> None: ...
