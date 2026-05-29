from typing import Any, ClassVar, overload
from android.health.connect.datatypes.AggregationType import AggregationType
from android.health.connect.datatypes.Metadata import Metadata
from android.health.connect.datatypes.units.Pressure import Pressure
from java.time.Instant import Instant
from java.time.ZoneOffset import ZoneOffset

class BloodPressureRecord:
    DIASTOLIC_AVG: ClassVar[AggregationType]
    DIASTOLIC_MAX: ClassVar[AggregationType]
    DIASTOLIC_MIN: ClassVar[AggregationType]
    SYSTOLIC_AVG: ClassVar[AggregationType]
    SYSTOLIC_MAX: ClassVar[AggregationType]
    SYSTOLIC_MIN: ClassVar[AggregationType]
    def equals(self, p0: Any) -> bool: ...
    def hashCode(self) -> int: ...
    def getMeasurementLocation(self) -> int: ...
    def getDiastolic(self) -> Pressure: ...
    def getBodyPosition(self) -> int: ...
    def getSystolic(self) -> Pressure: ...

    class Builder:
        def __init__(self, p0: Metadata, p1: Instant, p2: int, p3: Pressure, p4: Pressure, p5: int) -> None: ...
        def setZoneOffset(self, p0: ZoneOffset) -> Any: ...
        def clearZoneOffset(self) -> Any: ...
        def build(self) -> "BloodPressureRecord": ...

    class BodyPosition:
        BODY_POSITION_LYING_DOWN: ClassVar[int]
        BODY_POSITION_RECLINING: ClassVar[int]
        BODY_POSITION_SITTING_DOWN: ClassVar[int]
        BODY_POSITION_STANDING_UP: ClassVar[int]
        BODY_POSITION_UNKNOWN: ClassVar[int]

    class BloodPressureMeasurementLocation:
        BLOOD_PRESSURE_MEASUREMENT_LOCATION_LEFT_UPPER_ARM: ClassVar[int]
        BLOOD_PRESSURE_MEASUREMENT_LOCATION_LEFT_WRIST: ClassVar[int]
        BLOOD_PRESSURE_MEASUREMENT_LOCATION_RIGHT_UPPER_ARM: ClassVar[int]
        BLOOD_PRESSURE_MEASUREMENT_LOCATION_RIGHT_WRIST: ClassVar[int]
        BLOOD_PRESSURE_MEASUREMENT_LOCATION_UNKNOWN: ClassVar[int]
