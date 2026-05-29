from typing import Any, ClassVar, overload
from android.app.PendingIntent import PendingIntent

class SmsManager:
    RESULT_ERROR_GENERIC_FAILURE: ClassVar[int]
    RESULT_ERROR_NO_SERVICE: ClassVar[int]
    RESULT_ERROR_NULL_PDU: ClassVar[int]
    RESULT_ERROR_RADIO_OFF: ClassVar[int]
    STATUS_ON_SIM_FREE: ClassVar[int]
    STATUS_ON_SIM_READ: ClassVar[int]
    STATUS_ON_SIM_SENT: ClassVar[int]
    STATUS_ON_SIM_UNREAD: ClassVar[int]
    STATUS_ON_SIM_UNSENT: ClassVar[int]
    def sendDataMessage(self, p0: str, p1: str, p2: int, p3: Any, p4: PendingIntent, p5: PendingIntent) -> None: ...
    def sendTextMessage(self, p0: str, p1: str, p2: str, p3: PendingIntent, p4: PendingIntent) -> None: ...
    def divideMessage(self, p0: str) -> list: ...
    def sendMultipartTextMessage(self, p0: str, p1: str, p2: list, p3: list, p4: list) -> None: ...
    @staticmethod
    def getDefault() -> "SmsManager": ...
