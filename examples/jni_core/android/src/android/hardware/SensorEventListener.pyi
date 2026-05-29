from typing import Any, ClassVar, overload
from android.hardware.Sensor import Sensor
from android.hardware.SensorEvent import SensorEvent

class SensorEventListener:
    def onAccuracyChanged(self, p0: Sensor, p1: int) -> None: ...
    def onSensorChanged(self, p0: SensorEvent) -> None: ...
