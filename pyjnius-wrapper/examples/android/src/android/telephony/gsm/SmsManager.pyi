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
    @staticmethod
    def getDefault() -> "SmsManager": ...
    def sendTextMessage(self, arg0: str, arg1: str, arg2: str, arg3: PendingIntent, arg4: PendingIntent) -> None: ...
    def divideMessage(self, arg0: str) -> list: ...
    def sendMultipartTextMessage(self, arg0: str, arg1: str, arg2: list, arg3: list, arg4: list) -> None: ...
    def sendDataMessage(self, arg0: str, arg1: str, arg2: int, arg3: list[int], arg4: PendingIntent, arg5: PendingIntent) -> None: ...
