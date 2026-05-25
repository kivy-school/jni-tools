from typing import Any, ClassVar, overload
from android.hardware.Sensor import Sensor

class SensorEvent:
    accuracy: int
    firstEventAfterDiscontinuity: bool
    sensor: Sensor
    timestamp: int
    values: list[float]
