from typing import Any, ClassVar, overload
from android.hardware.Sensor import Sensor

class TriggerEvent:
    sensor: Sensor
    timestamp: int
    values: Any
