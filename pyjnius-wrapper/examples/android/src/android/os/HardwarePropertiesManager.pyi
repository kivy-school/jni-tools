from typing import Any, ClassVar, overload
from android.os.CpuUsageInfo import CpuUsageInfo

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
    def getDeviceTemperatures(self, arg0: int, arg1: int) -> list[float]: ...
    def getCpuUsages(self) -> list[CpuUsageInfo]: ...
    def getFanSpeeds(self) -> list[float]: ...
