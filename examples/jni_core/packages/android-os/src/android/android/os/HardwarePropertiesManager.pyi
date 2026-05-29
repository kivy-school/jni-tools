from typing import Any, ClassVar, overload

class HardwarePropertiesManager:
    DEVICE_TEMPERATURE_BATTERY: ClassVar[int]
    DEVICE_TEMPERATURE_CPU: ClassVar[int]
    DEVICE_TEMPERATURE_GPU: ClassVar[int]
    DEVICE_TEMPERATURE_SKIN: ClassVar[int]
    TEMPERATURE_CURRENT: ClassVar[int]
    TEMPERATURE_SHUTDOWN: ClassVar[int]
    TEMPERATURE_THROTTLING: ClassVar[int]
    TEMPERATURE_THROTTLING_BELOW_VR_MIN: ClassVar[int]
    UNDEFINED_TEMPERATURE: ClassVar[float]
    def getFanSpeeds(self) -> Any: ...
    def getCpuUsages(self) -> Any: ...
    def getDeviceTemperatures(self, p0: int, p1: int) -> Any: ...
