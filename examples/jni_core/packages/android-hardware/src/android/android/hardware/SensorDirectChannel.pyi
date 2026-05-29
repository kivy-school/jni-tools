from typing import Any, ClassVar, overload
from android.hardware.Sensor import Sensor

class SensorDirectChannel:
    RATE_FAST: ClassVar[int]
    RATE_NORMAL: ClassVar[int]
    RATE_STOP: ClassVar[int]
    RATE_VERY_FAST: ClassVar[int]
    TYPE_HARDWARE_BUFFER: ClassVar[int]
    TYPE_MEMORY_FILE: ClassVar[int]
    def isOpen(self) -> bool: ...
    def close(self) -> None: ...
    def configure(self, p0: Sensor, p1: int) -> int: ...
