from typing import Any, ClassVar, overload
from android.telephony.satellite.SatelliteStateChangeListener import SatelliteStateChangeListener
from java.util.concurrent.Executor import Executor

class SatelliteManager:
    def registerStateChangeListener(self, p0: Executor, p1: SatelliteStateChangeListener) -> None: ...
    def unregisterStateChangeListener(self, p0: SatelliteStateChangeListener) -> None: ...
