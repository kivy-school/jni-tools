from typing import Any, ClassVar, overload
from android.hardware.Sensor import Sensor
from android.hardware.SensorEvent import SensorEvent

class SensorEventListener:
    def onSensorChanged(self, arg0: SensorEvent) -> None: ...
    def onAccuracyChanged(self, arg0: Sensor, arg1: int) -> None: ...
