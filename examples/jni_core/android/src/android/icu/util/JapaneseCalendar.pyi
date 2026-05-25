from typing import Any, ClassVar, overload
from android.icu.util.TimeZone import TimeZone
from android.icu.util.ULocale import ULocale
from java.util.Date import Date
from java.util.Locale import Locale

class JapaneseCalendar:
    HEISEI: ClassVar[int]
    MEIJI: ClassVar[int]
    REIWA: ClassVar[int]
    SHOWA: ClassVar[int]
    TAISHO: ClassVar[int]
    AD: ClassVar[int]
    BC: ClassVar[int]
    AM: ClassVar[int]
    AM_PM: ClassVar[int]
    APRIL: ClassVar[int]
    AUGUST: ClassVar[int]
    DATE: ClassVar[int]
    DAY_OF_MONTH: ClassVar[int]
    DAY_OF_WEEK: ClassVar[int]
    DAY_OF_WEEK_IN_MONTH: ClassVar[int]
    DAY_OF_YEAR: ClassVar[int]
    DECEMBER: ClassVar[int]
    DOW_LOCAL: ClassVar[int]
    DST_OFFSET: ClassVar[int]
    ERA: ClassVar[int]
    EXTENDED_YEAR: ClassVar[int]
    FEBRUARY: ClassVar[int]
    FRIDAY: ClassVar[int]
    HOUR: ClassVar[int]
    HOUR_OF_DAY: ClassVar[int]
    IS_LEAP_MONTH: ClassVar[int]
    JANUARY: ClassVar[int]
    JULIAN_DAY: ClassVar[int]
    JULY: ClassVar[int]
    JUNE: ClassVar[int]
    MARCH: ClassVar[int]
    MAY: ClassVar[int]
    MILLISECOND: ClassVar[int]
    MILLISECONDS_IN_DAY: ClassVar[int]
    MINUTE: ClassVar[int]
    MONDAY: ClassVar[int]
    MONTH: ClassVar[int]
    NOVEMBER: ClassVar[int]
    OCTOBER: ClassVar[int]
    PM: ClassVar[int]
    SATURDAY: ClassVar[int]
    SECOND: ClassVar[int]
    SEPTEMBER: ClassVar[int]
    SUNDAY: ClassVar[int]
    THURSDAY: ClassVar[int]
    TUESDAY: ClassVar[int]
    UNDECIMBER: ClassVar[int]
    WALLTIME_FIRST: ClassVar[int]
    WALLTIME_LAST: ClassVar[int]
    WALLTIME_NEXT_VALID: ClassVar[int]
    WEDNESDAY: ClassVar[int]
    WEEK_OF_MONTH: ClassVar[int]
    WEEK_OF_YEAR: ClassVar[int]
    YEAR: ClassVar[int]
    YEAR_WOY: ClassVar[int]
    ZONE_OFFSET: ClassVar[int]
    @overload
    def __init__(self, p0: int, p1: int, p2: int, p3: int, p4: int, p5: int) -> None: ...
    @overload
    def __init__(self, p0: int, p1: int, p2: int) -> None: ...
    @overload
    def __init__(self, p0: int, p1: int, p2: int, p3: int) -> None: ...
    @overload
    def __init__(self, p0: ULocale) -> None: ...
    @overload
    def __init__(self, p0: Locale) -> None: ...
    @overload
    def __init__(self, p0: TimeZone) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, p0: TimeZone, p1: Locale) -> None: ...
    @overload
    def __init__(self, p0: TimeZone, p1: ULocale) -> None: ...
    @overload
    def __init__(self, p0: Date) -> None: ...
    def getActualMaximum(self, p0: int) -> int: ...
    def getType(self) -> str: ...
