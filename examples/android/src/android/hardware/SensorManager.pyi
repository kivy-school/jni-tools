from typing import Any, ClassVar, overload
from android.hardware.HardwareBuffer import HardwareBuffer
from android.hardware.Sensor import Sensor
from android.hardware.SensorDirectChannel import SensorDirectChannel
from android.hardware.SensorEventListener import SensorEventListener
from android.hardware.SensorListener import SensorListener
from android.hardware.TriggerEventListener import TriggerEventListener
from android.os.Handler import Handler
from android.os.MemoryFile import MemoryFile

class SensorManager:
    AXIS_MINUS_X: ClassVar[int]
    AXIS_MINUS_Y: ClassVar[int]
    AXIS_MINUS_Z: ClassVar[int]
    AXIS_X: ClassVar[int]
    AXIS_Y: ClassVar[int]
    AXIS_Z: ClassVar[int]
    DATA_X: ClassVar[int]
    DATA_Y: ClassVar[int]
    DATA_Z: ClassVar[int]
    GRAVITY_DEATH_STAR_I: ClassVar[float]
    GRAVITY_EARTH: ClassVar[float]
    GRAVITY_JUPITER: ClassVar[float]
    GRAVITY_MARS: ClassVar[float]
    GRAVITY_MERCURY: ClassVar[float]
    GRAVITY_MOON: ClassVar[float]
    GRAVITY_NEPTUNE: ClassVar[float]
    GRAVITY_PLUTO: ClassVar[float]
    GRAVITY_SATURN: ClassVar[float]
    GRAVITY_SUN: ClassVar[float]
    GRAVITY_THE_ISLAND: ClassVar[float]
    GRAVITY_URANUS: ClassVar[float]
    GRAVITY_VENUS: ClassVar[float]
    LIGHT_CLOUDY: ClassVar[float]
    LIGHT_FULLMOON: ClassVar[float]
    LIGHT_NO_MOON: ClassVar[float]
    LIGHT_OVERCAST: ClassVar[float]
    LIGHT_SHADE: ClassVar[float]
    LIGHT_SUNLIGHT: ClassVar[float]
    LIGHT_SUNLIGHT_MAX: ClassVar[float]
    LIGHT_SUNRISE: ClassVar[float]
    MAGNETIC_FIELD_EARTH_MAX: ClassVar[float]
    MAGNETIC_FIELD_EARTH_MIN: ClassVar[float]
    PRESSURE_STANDARD_ATMOSPHERE: ClassVar[float]
    RAW_DATA_INDEX: ClassVar[int]
    RAW_DATA_X: ClassVar[int]
    RAW_DATA_Y: ClassVar[int]
    RAW_DATA_Z: ClassVar[int]
    SENSOR_ACCELEROMETER: ClassVar[int]
    SENSOR_ALL: ClassVar[int]
    SENSOR_DELAY_FASTEST: ClassVar[int]
    SENSOR_DELAY_GAME: ClassVar[int]
    SENSOR_DELAY_NORMAL: ClassVar[int]
    SENSOR_DELAY_UI: ClassVar[int]
    SENSOR_LIGHT: ClassVar[int]
    SENSOR_MAGNETIC_FIELD: ClassVar[int]
    SENSOR_MAX: ClassVar[int]
    SENSOR_MIN: ClassVar[int]
    SENSOR_ORIENTATION: ClassVar[int]
    SENSOR_ORIENTATION_RAW: ClassVar[int]
    SENSOR_PROXIMITY: ClassVar[int]
    SENSOR_STATUS_ACCURACY_HIGH: ClassVar[int]
    SENSOR_STATUS_ACCURACY_LOW: ClassVar[int]
    SENSOR_STATUS_ACCURACY_MEDIUM: ClassVar[int]
    SENSOR_STATUS_NO_CONTACT: ClassVar[int]
    SENSOR_STATUS_UNRELIABLE: ClassVar[int]
    SENSOR_TEMPERATURE: ClassVar[int]
    SENSOR_TRICORDER: ClassVar[int]
    STANDARD_GRAVITY: ClassVar[float]
    def getSensors(self) -> int: ...
    def getSensorList(self, arg0: int) -> list: ...
    def getDynamicSensorList(self, arg0: int) -> list: ...
    @overload
    def getDefaultSensor(self, arg0: int) -> Sensor: ...
    @overload
    def getDefaultSensor(self, arg0: int, arg1: bool) -> Sensor: ...
    @overload
    def registerListener(self, arg0: SensorListener, arg1: int) -> bool: ...
    @overload
    def registerListener(self, arg0: SensorListener, arg1: int, arg2: int) -> bool: ...
    @overload
    def registerListener(self, arg0: SensorEventListener, arg1: Sensor, arg2: int) -> bool: ...
    @overload
    def registerListener(self, arg0: SensorEventListener, arg1: Sensor, arg2: int, arg3: int) -> bool: ...
    @overload
    def registerListener(self, arg0: SensorEventListener, arg1: Sensor, arg2: int, arg3: Handler) -> bool: ...
    @overload
    def registerListener(self, arg0: SensorEventListener, arg1: Sensor, arg2: int, arg3: int, arg4: Handler) -> bool: ...
    @overload
    def unregisterListener(self, arg0: SensorListener) -> None: ...
    @overload
    def unregisterListener(self, arg0: SensorListener, arg1: int) -> None: ...
    @overload
    def unregisterListener(self, arg0: SensorEventListener, arg1: Sensor) -> None: ...
    @overload
    def unregisterListener(self, arg0: SensorEventListener) -> None: ...
    def flush(self, arg0: SensorEventListener) -> bool: ...
    @overload
    def createDirectChannel(self, arg0: MemoryFile) -> SensorDirectChannel: ...
    @overload
    def createDirectChannel(self, arg0: HardwareBuffer) -> SensorDirectChannel: ...
    @overload
    def registerDynamicSensorCallback(self, arg0: "DynamicSensorCallback") -> None: ...
    @overload
    def registerDynamicSensorCallback(self, arg0: "DynamicSensorCallback", arg1: Handler) -> None: ...
    def unregisterDynamicSensorCallback(self, arg0: "DynamicSensorCallback") -> None: ...
    def isDynamicSensorDiscoverySupported(self) -> bool: ...
    @staticmethod
    def getRotationMatrix(arg0: list[float], arg1: list[float], arg2: list[float], arg3: list[float]) -> bool: ...
    @staticmethod
    def getInclination(arg0: list[float]) -> float: ...
    @staticmethod
    def remapCoordinateSystem(arg0: list[float], arg1: int, arg2: int, arg3: list[float]) -> bool: ...
    @staticmethod
    def getOrientation(arg0: list[float], arg1: list[float]) -> list[float]: ...
    @staticmethod
    def getAltitude(arg0: float, arg1: float) -> float: ...
    @staticmethod
    def getAngleChange(arg0: list[float], arg1: list[float], arg2: list[float]) -> None: ...
    @staticmethod
    def getRotationMatrixFromVector(arg0: list[float], arg1: list[float]) -> None: ...
    @staticmethod
    def getQuaternionFromVector(arg0: list[float], arg1: list[float]) -> None: ...
    def requestTriggerSensor(self, arg0: TriggerEventListener, arg1: Sensor) -> bool: ...
    def cancelTriggerSensor(self, arg0: TriggerEventListener, arg1: Sensor) -> bool: ...

    class DynamicSensorCallback:
        def __init__(self) -> None: ...
        def onDynamicSensorConnected(self, arg0: Sensor) -> None: ...
        def onDynamicSensorDisconnected(self, arg0: Sensor) -> None: ...
