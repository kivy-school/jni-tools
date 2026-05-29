from typing import Any, ClassVar, overload

class Sensor:
    REPORTING_MODE_CONTINUOUS: ClassVar[int]
    REPORTING_MODE_ONE_SHOT: ClassVar[int]
    REPORTING_MODE_ON_CHANGE: ClassVar[int]
    REPORTING_MODE_SPECIAL_TRIGGER: ClassVar[int]
    STRING_TYPE_ACCELEROMETER: ClassVar[str]
    STRING_TYPE_ACCELEROMETER_LIMITED_AXES: ClassVar[str]
    STRING_TYPE_ACCELEROMETER_LIMITED_AXES_UNCALIBRATED: ClassVar[str]
    STRING_TYPE_ACCELEROMETER_UNCALIBRATED: ClassVar[str]
    STRING_TYPE_AMBIENT_TEMPERATURE: ClassVar[str]
    STRING_TYPE_GAME_ROTATION_VECTOR: ClassVar[str]
    STRING_TYPE_GEOMAGNETIC_ROTATION_VECTOR: ClassVar[str]
    STRING_TYPE_GRAVITY: ClassVar[str]
    STRING_TYPE_GYROSCOPE: ClassVar[str]
    STRING_TYPE_GYROSCOPE_LIMITED_AXES: ClassVar[str]
    STRING_TYPE_GYROSCOPE_LIMITED_AXES_UNCALIBRATED: ClassVar[str]
    STRING_TYPE_GYROSCOPE_UNCALIBRATED: ClassVar[str]
    STRING_TYPE_HEADING: ClassVar[str]
    STRING_TYPE_HEAD_TRACKER: ClassVar[str]
    STRING_TYPE_HEART_BEAT: ClassVar[str]
    STRING_TYPE_HEART_RATE: ClassVar[str]
    STRING_TYPE_HINGE_ANGLE: ClassVar[str]
    STRING_TYPE_LIGHT: ClassVar[str]
    STRING_TYPE_LINEAR_ACCELERATION: ClassVar[str]
    STRING_TYPE_LOW_LATENCY_OFFBODY_DETECT: ClassVar[str]
    STRING_TYPE_MAGNETIC_FIELD: ClassVar[str]
    STRING_TYPE_MAGNETIC_FIELD_UNCALIBRATED: ClassVar[str]
    STRING_TYPE_MOTION_DETECT: ClassVar[str]
    STRING_TYPE_ORIENTATION: ClassVar[str]
    STRING_TYPE_POSE_6DOF: ClassVar[str]
    STRING_TYPE_PRESSURE: ClassVar[str]
    STRING_TYPE_PROXIMITY: ClassVar[str]
    STRING_TYPE_RELATIVE_HUMIDITY: ClassVar[str]
    STRING_TYPE_ROTATION_VECTOR: ClassVar[str]
    STRING_TYPE_SIGNIFICANT_MOTION: ClassVar[str]
    STRING_TYPE_STATIONARY_DETECT: ClassVar[str]
    STRING_TYPE_STEP_COUNTER: ClassVar[str]
    STRING_TYPE_STEP_DETECTOR: ClassVar[str]
    STRING_TYPE_TEMPERATURE: ClassVar[str]
    TYPE_ACCELEROMETER: ClassVar[int]
    TYPE_ACCELEROMETER_LIMITED_AXES: ClassVar[int]
    TYPE_ACCELEROMETER_LIMITED_AXES_UNCALIBRATED: ClassVar[int]
    TYPE_ACCELEROMETER_UNCALIBRATED: ClassVar[int]
    TYPE_ALL: ClassVar[int]
    TYPE_AMBIENT_TEMPERATURE: ClassVar[int]
    TYPE_DEVICE_PRIVATE_BASE: ClassVar[int]
    TYPE_GAME_ROTATION_VECTOR: ClassVar[int]
    TYPE_GEOMAGNETIC_ROTATION_VECTOR: ClassVar[int]
    TYPE_GRAVITY: ClassVar[int]
    TYPE_GYROSCOPE: ClassVar[int]
    TYPE_GYROSCOPE_LIMITED_AXES: ClassVar[int]
    TYPE_GYROSCOPE_LIMITED_AXES_UNCALIBRATED: ClassVar[int]
    TYPE_GYROSCOPE_UNCALIBRATED: ClassVar[int]
    TYPE_HEADING: ClassVar[int]
    TYPE_HEAD_TRACKER: ClassVar[int]
    TYPE_HEART_BEAT: ClassVar[int]
    TYPE_HEART_RATE: ClassVar[int]
    TYPE_HINGE_ANGLE: ClassVar[int]
    TYPE_LIGHT: ClassVar[int]
    TYPE_LINEAR_ACCELERATION: ClassVar[int]
    TYPE_LOW_LATENCY_OFFBODY_DETECT: ClassVar[int]
    TYPE_MAGNETIC_FIELD: ClassVar[int]
    TYPE_MAGNETIC_FIELD_UNCALIBRATED: ClassVar[int]
    TYPE_MOTION_DETECT: ClassVar[int]
    TYPE_ORIENTATION: ClassVar[int]
    TYPE_POSE_6DOF: ClassVar[int]
    TYPE_PRESSURE: ClassVar[int]
    TYPE_PROXIMITY: ClassVar[int]
    TYPE_RELATIVE_HUMIDITY: ClassVar[int]
    TYPE_ROTATION_VECTOR: ClassVar[int]
    TYPE_SIGNIFICANT_MOTION: ClassVar[int]
    TYPE_STATIONARY_DETECT: ClassVar[int]
    TYPE_STEP_COUNTER: ClassVar[int]
    TYPE_STEP_DETECTOR: ClassVar[int]
    TYPE_TEMPERATURE: ClassVar[int]
    def getName(self) -> str: ...
    def toString(self) -> str: ...
    def getId(self) -> int: ...
    def getType(self) -> int: ...
    def getFifoMaxEventCount(self) -> int: ...
    def getFifoReservedEventCount(self) -> int: ...
    def getHighestDirectReportRateLevel(self) -> int: ...
    def getMaxDelay(self) -> int: ...
    def getMaximumRange(self) -> float: ...
    def getMinDelay(self) -> int: ...
    def getReportingMode(self) -> int: ...
    def getResolution(self) -> float: ...
    def getStringType(self) -> str: ...
    def getVendor(self) -> str: ...
    def isAdditionalInfoSupported(self) -> bool: ...
    def isDirectChannelTypeSupported(self, p0: int) -> bool: ...
    def isDynamicSensor(self) -> bool: ...
    def isWakeUpSensor(self) -> bool: ...
    def getPower(self) -> float: ...
    def getVersion(self) -> int: ...
