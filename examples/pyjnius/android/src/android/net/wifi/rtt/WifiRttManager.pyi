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
    CHARACTERISTICS_KEY_BOOLEAN_RANGING_FRAME_PROTECTION_SUPPORTED: ClassVar[str]
    CHARACTERISTICS_KEY_BOOLEAN_SECURE_HE_LTF_SUPPORTED: ClassVar[str]
    CHARACTERISTICS_KEY_BOOLEAN_STA_RESPONDER: ClassVar[str]
    CHARACTERISTICS_KEY_INT_MAX_SUPPORTED_SECURE_HE_LTF_PROTO_VERSION: ClassVar[str]
    def isAvailable(self) -> bool: ...
    def startRanging(self, p0: RangingRequest, p1: Executor, p2: RangingResultCallback) -> None: ...
    def getRttCharacteristics(self) -> Bundle: ...
