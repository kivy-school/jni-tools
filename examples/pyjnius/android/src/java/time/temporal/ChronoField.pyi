from typing import Any, ClassVar, overload
from java.time.temporal.Temporal import Temporal
from java.time.temporal.TemporalAccessor import TemporalAccessor
from java.time.temporal.TemporalUnit import TemporalUnit
from java.time.temporal.ValueRange import ValueRange
from java.util.Locale import Locale

class ChronoField:
    NANO_OF_SECOND: ClassVar["ChronoField"]
    NANO_OF_DAY: ClassVar["ChronoField"]
    MICRO_OF_SECOND: ClassVar["ChronoField"]
    MICRO_OF_DAY: ClassVar["ChronoField"]
    MILLI_OF_SECOND: ClassVar["ChronoField"]
    MILLI_OF_DAY: ClassVar["ChronoField"]
    SECOND_OF_MINUTE: ClassVar["ChronoField"]
    SECOND_OF_DAY: ClassVar["ChronoField"]
    MINUTE_OF_HOUR: ClassVar["ChronoField"]
    MINUTE_OF_DAY: ClassVar["ChronoField"]
    HOUR_OF_AMPM: ClassVar["ChronoField"]
    CLOCK_HOUR_OF_AMPM: ClassVar["ChronoField"]
    HOUR_OF_DAY: ClassVar["ChronoField"]
    CLOCK_HOUR_OF_DAY: ClassVar["ChronoField"]
    AMPM_OF_DAY: ClassVar["ChronoField"]
    DAY_OF_WEEK: ClassVar["ChronoField"]
    ALIGNED_DAY_OF_WEEK_IN_MONTH: ClassVar["ChronoField"]
    ALIGNED_DAY_OF_WEEK_IN_YEAR: ClassVar["ChronoField"]
    DAY_OF_MONTH: ClassVar["ChronoField"]
    DAY_OF_YEAR: ClassVar["ChronoField"]
    EPOCH_DAY: ClassVar["ChronoField"]
    ALIGNED_WEEK_OF_MONTH: ClassVar["ChronoField"]
    ALIGNED_WEEK_OF_YEAR: ClassVar["ChronoField"]
    MONTH_OF_YEAR: ClassVar["ChronoField"]
    PROLEPTIC_MONTH: ClassVar["ChronoField"]
    YEAR_OF_ERA: ClassVar["ChronoField"]
    YEAR: ClassVar["ChronoField"]
    ERA: ClassVar["ChronoField"]
    INSTANT_SECONDS: ClassVar["ChronoField"]
    OFFSET_SECONDS: ClassVar["ChronoField"]
    @staticmethod
    def values() -> list["ChronoField"]: ...
    @staticmethod
    def valueOf(arg0: str) -> "ChronoField": ...
    def getDisplayName(self, arg0: Locale) -> str: ...
    def getBaseUnit(self) -> TemporalUnit: ...
    def getRangeUnit(self) -> TemporalUnit: ...
    def range(self) -> ValueRange: ...
    def isDateBased(self) -> bool: ...
    def isTimeBased(self) -> bool: ...
    def checkValidValue(self, arg0: int) -> int: ...
    def checkValidIntValue(self, arg0: int) -> int: ...
    def isSupportedBy(self, arg0: TemporalAccessor) -> bool: ...
    def rangeRefinedBy(self, arg0: TemporalAccessor) -> ValueRange: ...
    def getFrom(self, arg0: TemporalAccessor) -> int: ...
    def adjustInto(self, arg0: Temporal, arg1: int) -> Temporal: ...
    def toString(self) -> str: ...
