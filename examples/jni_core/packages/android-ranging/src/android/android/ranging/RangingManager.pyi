from typing import Any, ClassVar, overload
from android.ranging.RangingCapabilities import RangingCapabilities
from android.ranging.RangingSession import RangingSession
from java.util.concurrent.Executor import Executor

class RangingManager:
    BLE_CS: ClassVar[int]
    BLE_RSSI: ClassVar[int]
    UWB: ClassVar[int]
    WIFI_NAN_RTT: ClassVar[int]
    def unregisterCapabilitiesCallback(self, p0: Any) -> None: ...
    def createRangingSession(self, p0: Executor, p1: Any) -> RangingSession: ...
    def registerCapabilitiesCallback(self, p0: Executor, p1: Any) -> None: ...

    class RangingCapabilitiesCallback:
        def onRangingCapabilities(self, p0: RangingCapabilities) -> None: ...
