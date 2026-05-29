from typing import Any, ClassVar, overload
from android.health.connect.datatypes.Metadata import Metadata
from android.health.connect.datatypes.units.BloodGlucose import BloodGlucose
from java.time.Instant import Instant
from java.time.ZoneOffset import ZoneOffset

class BloodGlucoseRecord:
    def getSpecimenSource(self) -> int: ...
    def getLevel(self) -> BloodGlucose: ...
    def getRelationToMeal(self) -> int: ...
    def getMealType(self) -> int: ...
    def equals(self, arg0: Any) -> bool: ...
    def hashCode(self) -> int: ...

    class Builder:
        def __init__(self, arg0: Metadata, arg1: Instant, arg2: int, arg3: BloodGlucose, arg4: int, arg5: int) -> None: ...
        def setZoneOffset(self, arg0: ZoneOffset) -> "Builder": ...
        def clearZoneOffset(self) -> "Builder": ...
        def build(self) -> "BloodGlucoseRecord": ...

    class RelationToMealType:
        RELATION_TO_MEAL_AFTER_MEAL: ClassVar[int]
        RELATION_TO_MEAL_BEFORE_MEAL: ClassVar[int]
        RELATION_TO_MEAL_FASTING: ClassVar[int]
        RELATION_TO_MEAL_GENERAL: ClassVar[int]
        RELATION_TO_MEAL_UNKNOWN: ClassVar[int]

    class SpecimenSource:
        SPECIMEN_SOURCE_CAPILLARY_BLOOD: ClassVar[int]
        SPECIMEN_SOURCE_INTERSTITIAL_FLUID: ClassVar[int]
        SPECIMEN_SOURCE_PLASMA: ClassVar[int]
        SPECIMEN_SOURCE_SERUM: ClassVar[int]
        SPECIMEN_SOURCE_TEARS: ClassVar[int]
        SPECIMEN_SOURCE_UNKNOWN: ClassVar[int]
        SPECIMEN_SOURCE_WHOLE_BLOOD: ClassVar[int]
