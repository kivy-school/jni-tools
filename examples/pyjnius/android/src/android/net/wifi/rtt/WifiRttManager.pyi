from typing import Any, ClassVar, overload
from android.net.wifi.rtt.RangingRequest import RangingRequest
from android.net.wifi.rtt.RangingResultCallback import RangingResultCallback
from android.os.Bundle import Bundle
from java.util.concurrent.Executor import Executor

class WifiRttManager:
    ACTION_WIFI_RTT_STATE_CHANGED: ClassVar[str]
    CHARACTERISTICS_KEY_BOOLEAN_LCI: ClassVar[str]
    CHARACTERISTICS_KEY_BOOLEAN_LCR: ClassVar[str]
    CHARACTERISTICS_KEY_BOOLEAN_NTB_INITIATOR: ClassVar[str]
    CHARACTERISTICS_KEY_BOOLEAN_ONE_SIDED_RTT: ClassVar[str]
    CHARACTERISTICS_KEY_BOOLEAN_STA_RESPONDER: ClassVar[str]
    def isAvailable(self) -> bool: ...
    def startRanging(self, arg0: RangingRequest, arg1: Executor, arg2: RangingResultCallback) -> None: ...
    def getRttCharacteristics(self) -> Bundle: ...
