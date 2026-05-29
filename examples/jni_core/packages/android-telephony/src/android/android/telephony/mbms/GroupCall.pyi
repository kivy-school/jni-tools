from typing import Any, ClassVar, overload

class GroupCall:
    REASON_BY_USER_REQUEST: ClassVar[int]
    REASON_FREQUENCY_CONFLICT: ClassVar[int]
    REASON_LEFT_MBMS_BROADCAST_AREA: ClassVar[int]
    REASON_NONE: ClassVar[int]
    REASON_NOT_CONNECTED_TO_HOMECARRIER_LTE: ClassVar[int]
    REASON_OUT_OF_MEMORY: ClassVar[int]
    STATE_STALLED: ClassVar[int]
    STATE_STARTED: ClassVar[int]
    STATE_STOPPED: ClassVar[int]
    def getTmgi(self) -> int: ...
    def updateGroupCall(self, p0: list, p1: list) -> None: ...
    def close(self) -> None: ...
