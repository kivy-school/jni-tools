from typing import Any, ClassVar, overload
from java.time.Duration import Duration
from java.time.temporal.Temporal import Temporal

class ChronoUnit:
    NANOS: ClassVar["ChronoUnit"]
    MICROS: ClassVar["ChronoUnit"]
    MILLIS: ClassVar["ChronoUnit"]
    SECONDS: ClassVar["ChronoUnit"]
    MINUTES: ClassVar["ChronoUnit"]
    HOURS: ClassVar["ChronoUnit"]
    HALF_DAYS: ClassVar["ChronoUnit"]
    DAYS: ClassVar["ChronoUnit"]
    WEEKS: ClassVar["ChronoUnit"]
    MONTHS: ClassVar["ChronoUnit"]
    YEARS: ClassVar["ChronoUnit"]
    DECADES: ClassVar["ChronoUnit"]
    CENTURIES: ClassVar["ChronoUnit"]
    MILLENNIA: ClassVar["ChronoUnit"]
    ERAS: ClassVar["ChronoUnit"]
    FOREVER: ClassVar["ChronoUnit"]
    NANOS: ClassVar["ChronoUnit"]
    MICROS: ClassVar["ChronoUnit"]
    MILLIS: ClassVar["ChronoUnit"]
    SECONDS: ClassVar["ChronoUnit"]
    MINUTES: ClassVar["ChronoUnit"]
    HOURS: ClassVar["ChronoUnit"]
    HALF_DAYS: ClassVar["ChronoUnit"]
    DAYS: ClassVar["ChronoUnit"]
    WEEKS: ClassVar["ChronoUnit"]
    MONTHS: ClassVar["ChronoUnit"]
    YEARS: ClassVar["ChronoUnit"]
    DECADES: ClassVar["ChronoUnit"]
    CENTURIES: ClassVar["ChronoUnit"]
    MILLENNIA: ClassVar["ChronoUnit"]
    ERAS: ClassVar["ChronoUnit"]
    FOREVER: ClassVar["ChronoUnit"]
    def isDateBased(self) -> bool: ...
    def isSupportedBy(self, p0: Temporal) -> bool: ...
    def isTimeBased(self) -> bool: ...
    def getDuration(self) -> Duration: ...
    def isDurationEstimated(self) -> bool: ...
    def addTo(self, p0: Temporal, p1: int) -> Temporal: ...
    def between(self, p0: Temporal, p1: Temporal) -> int: ...
    def toString(self) -> str: ...
    @staticmethod
    def values() -> Any: ...
    @staticmethod
    def valueOf(p0: str) -> "ChronoUnit": ...
