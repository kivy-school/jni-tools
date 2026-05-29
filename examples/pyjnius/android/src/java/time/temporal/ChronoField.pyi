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
    def toString(self) -> str: ...
    @staticmethod
    def values() -> Any: ...
    @staticmethod
    def valueOf(p0: str) -> "ChronoField": ...
    def getDisplayName(self, p0: Locale) -> str: ...
    def range(self) -> ValueRange: ...
    def getBaseUnit(self) -> TemporalUnit: ...
    def getRangeUnit(self) -> TemporalUnit: ...
    def isTimeBased(self) -> bool: ...
    def checkValidIntValue(self, p0: int) -> int: ...
    def checkValidValue(self, p0: int) -> int: ...
    def isDateBased(self) -> bool: ...
    def rangeRefinedBy(self, p0: TemporalAccessor) -> ValueRange: ...
    def getFrom(self, p0: TemporalAccessor) -> int: ...
    def adjustInto(self, p0: Temporal, p1: int) -> Temporal: ...
    def isSupportedBy(self, p0: TemporalAccessor) -> bool: ...
