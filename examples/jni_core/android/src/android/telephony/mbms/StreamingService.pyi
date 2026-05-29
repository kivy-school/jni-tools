from typing import Any, ClassVar, overload
from android.net.Uri import Uri
from android.telephony.mbms.StreamingServiceInfo import StreamingServiceInfo

class StreamingService:
    BROADCAST_METHOD: ClassVar[int]
    REASON_BY_USER_REQUEST: ClassVar[int]
    REASON_END_OF_SESSION: ClassVar[int]
    REASON_FREQUENCY_CONFLICT: ClassVar[int]
    REASON_LEFT_MBMS_BROADCAST_AREA: ClassVar[int]
    REASON_NONE: ClassVar[int]
    REASON_NOT_CONNECTED_TO_HOMECARRIER_LTE: ClassVar[int]
    REASON_OUT_OF_MEMORY: ClassVar[int]
    STATE_STALLED: ClassVar[int]
    STATE_STARTED: ClassVar[int]
    STATE_STOPPED: ClassVar[int]
    UNICAST_METHOD: ClassVar[int]
    def getInfo(self) -> StreamingServiceInfo: ...
    def getPlaybackUri(self) -> Uri: ...
    def close(self) -> None: ...
