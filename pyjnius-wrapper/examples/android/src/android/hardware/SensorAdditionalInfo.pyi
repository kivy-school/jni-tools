from typing import Any, ClassVar, overload
from android.hardware.Sensor import Sensor

class SensorAdditionalInfo:
    TYPE_FRAME_BEGIN: ClassVar[int]
    TYPE_FRAME_END: ClassVar[int]
    TYPE_INTERNAL_TEMPERATURE: ClassVar[int]
    TYPE_SAMPLING: ClassVar[int]
    TYPE_SENSOR_PLACEMENT: ClassVar[int]
    TYPE_UNTRACKED_DELAY: ClassVar[int]
    TYPE_VEC3_CALIBRATION: ClassVar[int]
    floatValues: list[float]
    intValues: list[int]
    sensor: Sensor
    serial: int
    type: int
