from typing import Any, ClassVar, overload
from android.hardware.Sensor import Sensor

class SensorEventListener2:
    def onFlushCompleted(self, p0: Sensor) -> None: ...
