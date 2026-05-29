from typing import Any, ClassVar, overload
from android.health.connect.datatypes.Metadata import Metadata
from android.health.connect.datatypes.units.BloodGlucose import BloodGlucose
from java.time.Instant import Instant
from java.time.ZoneOffset import ZoneOffset

class BloodGlucoseRecord:
    def equals(self, p0: Any) -> bool: ...
    def hashCode(self) -> int: ...
    def getRelationToMeal(self) -> int: ...
    def getSpecimenSource(self) -> int: ...
    def getMealType(self) -> int: ...
    def getLevel(self) -> BloodGlucose: ...

    class SpecimenSource:
        SPECIMEN_SOURCE_CAPILLARY_BLOOD: ClassVar[int]
        SPECIMEN_SOURCE_INTERSTITIAL_FLUID: ClassVar[int]
        SPECIMEN_SOURCE_PLASMA: ClassVar[int]
        SPECIMEN_SOURCE_SERUM: ClassVar[int]
        SPECIMEN_SOURCE_TEARS: ClassVar[int]
        SPECIMEN_SOURCE_UNKNOWN: ClassVar[int]
        SPECIMEN_SOURCE_WHOLE_BLOOD: ClassVar[int]

    class RelationToMealType:
        RELATION_TO_MEAL_AFTER_MEAL: ClassVar[int]
        RELATION_TO_MEAL_BEFORE_MEAL: ClassVar[int]
        RELATION_TO_MEAL_FASTING: ClassVar[int]
        RELATION_TO_MEAL_GENERAL: ClassVar[int]
        RELATION_TO_MEAL_UNKNOWN: ClassVar[int]

    class Builder:
        def __init__(self, p0: Metadata, p1: Instant, p2: int, p3: BloodGlucose, p4: int, p5: int) -> None: ...
        def setZoneOffset(self, p0: ZoneOffset) -> Any: ...
        def clearZoneOffset(self) -> Any: ...
        def build(self) -> "BloodGlucoseRecord": ...
