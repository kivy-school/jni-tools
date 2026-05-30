from typing import Any, ClassVar, overload
from android.content.Context import Context
from java.lang.StringBuilder import StringBuilder
from java.util.Formatter import Formatter

class DateUtils:
    ABBREV_MONTH_FORMAT: ClassVar[str]
    ABBREV_WEEKDAY_FORMAT: ClassVar[str]
    DAY_IN_MILLIS: ClassVar[int]
    FORMAT_12HOUR: ClassVar[int]
    FORMAT_24HOUR: ClassVar[int]
    FORMAT_ABBREV_ALL: ClassVar[int]
    FORMAT_ABBREV_MONTH: ClassVar[int]
    FORMAT_ABBREV_RELATIVE: ClassVar[int]
    FORMAT_ABBREV_TIME: ClassVar[int]
    FORMAT_ABBREV_WEEKDAY: ClassVar[int]
    FORMAT_CAP_AMPM: ClassVar[int]
    FORMAT_CAP_MIDNIGHT: ClassVar[int]
    FORMAT_CAP_NOON: ClassVar[int]
    FORMAT_CAP_NOON_MIDNIGHT: ClassVar[int]
    FORMAT_NO_MIDNIGHT: ClassVar[int]
    FORMAT_NO_MONTH_DAY: ClassVar[int]
    FORMAT_NO_NOON: ClassVar[int]
    FORMAT_NO_NOON_MIDNIGHT: ClassVar[int]
    FORMAT_NO_YEAR: ClassVar[int]
    FORMAT_NUMERIC_DATE: ClassVar[int]
    FORMAT_SHOW_DATE: ClassVar[int]
    FORMAT_SHOW_TIME: ClassVar[int]
    FORMAT_SHOW_WEEKDAY: ClassVar[int]
    FORMAT_SHOW_YEAR: ClassVar[int]
    FORMAT_UTC: ClassVar[int]
    HOUR_IN_MILLIS: ClassVar[int]
    HOUR_MINUTE_24: ClassVar[str]
    LENGTH_LONG: ClassVar[int]
    LENGTH_MEDIUM: ClassVar[int]
    LENGTH_SHORT: ClassVar[int]
    LENGTH_SHORTER: ClassVar[int]
    LENGTH_SHORTEST: ClassVar[int]
    MINUTE_IN_MILLIS: ClassVar[int]
    MONTH_DAY_FORMAT: ClassVar[str]
    MONTH_FORMAT: ClassVar[str]
    NUMERIC_MONTH_FORMAT: ClassVar[str]
    SECOND_IN_MILLIS: ClassVar[int]
    WEEKDAY_FORMAT: ClassVar[str]
    WEEK_IN_MILLIS: ClassVar[int]
    YEAR_FORMAT: ClassVar[str]
    YEAR_FORMAT_TWO_DIGITS: ClassVar[str]
    YEAR_IN_MILLIS: ClassVar[int]
    sameMonthTable: ClassVar[Any]
    sameYearTable: ClassVar[Any]
    def __init__(self) -> None: ...
    @overload
    @staticmethod
    def formatDateRange(p0: Context, p1: Formatter, p2: int, p3: int, p4: int, p5: str) -> Formatter: ...
    @overload
    @staticmethod
    def formatDateRange(p0: Context, p1: Formatter, p2: int, p3: int, p4: int) -> Formatter: ...
    @overload
    @staticmethod
    def formatDateRange(p0: Context, p1: int, p2: int, p3: int) -> str: ...
    @staticmethod
    def formatDateTime(p0: Context, p1: int, p2: int) -> str: ...
    @overload
    @staticmethod
    def formatElapsedTime(p0: StringBuilder, p1: int) -> str: ...
    @overload
    @staticmethod
    def formatElapsedTime(p0: int) -> str: ...
    @staticmethod
    def formatSameDayTime(p0: int, p1: int, p2: int, p3: int) -> str: ...
    @staticmethod
    def getAMPMString(p0: int) -> str: ...
    @staticmethod
    def getDayOfWeekString(p0: int, p1: int) -> str: ...
    @staticmethod
    def getMonthString(p0: int, p1: int) -> str: ...
    @staticmethod
    def getRelativeDateTimeString(p0: Context, p1: int, p2: int, p3: int, p4: int) -> str: ...
    @overload
    @staticmethod
    def getRelativeTimeSpanString(p0: int) -> str: ...
    @overload
    @staticmethod
    def getRelativeTimeSpanString(p0: int, p1: int, p2: int, p3: int) -> str: ...
    @overload
    @staticmethod
    def getRelativeTimeSpanString(p0: int, p1: int, p2: int) -> str: ...
    @overload
    @staticmethod
    def getRelativeTimeSpanString(p0: Context, p1: int) -> str: ...
    @overload
    @staticmethod
    def getRelativeTimeSpanString(p0: Context, p1: int, p2: bool) -> str: ...
    @staticmethod
    def isToday(p0: int) -> bool: ...

from typing import Any, ClassVar, overload
from android.content.Context import Context

class Formatter:
    def __init__(self) -> None: ...
    @staticmethod
    def formatIpAddress(p0: int) -> str: ...
    @staticmethod
    def formatFileSize(p0: Context, p1: int) -> str: ...
    @staticmethod
    def formatShortFileSize(p0: Context, p1: int) -> str: ...

from typing import Any, ClassVar, overload
from android.content.Context import Context
from java.util.Calendar import Calendar
from java.util.Date import Date
from java.util.Locale import Locale

class DateFormat:
    def __init__(self) -> None: ...
    @staticmethod
    def getBestDateTimePattern(p0: Locale, p1: str) -> str: ...
    @staticmethod
    def getDateFormat(p0: Context) -> "DateFormat": ...
    @staticmethod
    def getDateFormatOrder(p0: Context) -> Any: ...
    @staticmethod
    def getLongDateFormat(p0: Context) -> "DateFormat": ...
    @staticmethod
    def getMediumDateFormat(p0: Context) -> "DateFormat": ...
    @staticmethod
    def getTimeFormat(p0: Context) -> "DateFormat": ...
    @staticmethod
    def is24HourFormat(p0: Context) -> bool: ...
    @overload
    @staticmethod
    def format(p0: str, p1: int) -> str: ...
    @overload
    @staticmethod
    def format(p0: str, p1: Calendar) -> str: ...
    @overload
    @staticmethod
    def format(p0: str, p1: Date) -> str: ...

from typing import Any, ClassVar, overload

class Time:
    EPOCH_JULIAN_DAY: ClassVar[int]
    FRIDAY: ClassVar[int]
    HOUR: ClassVar[int]
    MINUTE: ClassVar[int]
    MONDAY: ClassVar[int]
    MONDAY_BEFORE_JULIAN_EPOCH: ClassVar[int]
    MONTH: ClassVar[int]
    MONTH_DAY: ClassVar[int]
    SATURDAY: ClassVar[int]
    SECOND: ClassVar[int]
    SUNDAY: ClassVar[int]
    THURSDAY: ClassVar[int]
    TIMEZONE_UTC: ClassVar[str]
    TUESDAY: ClassVar[int]
    WEDNESDAY: ClassVar[int]
    WEEK_DAY: ClassVar[int]
    WEEK_NUM: ClassVar[int]
    YEAR: ClassVar[int]
    YEAR_DAY: ClassVar[int]
    allDay: bool
    gmtoff: int
    hour: int
    isDst: int
    minute: int
    month: int
    monthDay: int
    second: int
    timezone: str
    weekDay: int
    year: int
    yearDay: int
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, p0: "Time") -> None: ...
    @overload
    def __init__(self, p0: str) -> None: ...
    def format2445(self) -> str: ...
    def format3339(self, p0: bool) -> str: ...
    @staticmethod
    def getCurrentTimezone() -> str: ...
    @staticmethod
    def getJulianDay(p0: int, p1: int) -> int: ...
    @staticmethod
    def getJulianMondayFromWeeksSinceEpoch(p0: int) -> int: ...
    def getWeekNumber(self) -> int: ...
    @staticmethod
    def getWeeksSinceEpochFromJulianDay(p0: int, p1: int) -> int: ...
    @staticmethod
    def isEpoch(p0: "Time") -> bool: ...
    def parse3339(self, p0: str) -> bool: ...
    def setJulianDay(self, p0: int) -> int: ...
    def setToNow(self) -> None: ...
    def switchTimezone(self, p0: str) -> None: ...
    def toString(self) -> str: ...
    @staticmethod
    def compare(p0: "Time", p1: "Time") -> int: ...
    def clear(self, p0: str) -> None: ...
    def format(self, p0: str) -> str: ...
    @overload
    def set(self, p0: int, p1: int, p2: int) -> None: ...
    @overload
    def set(self, p0: int, p1: int, p2: int, p3: int, p4: int, p5: int) -> None: ...
    @overload
    def set(self, p0: int) -> None: ...
    @overload
    def set(self, p0: "Time") -> None: ...
    def toMillis(self, p0: bool) -> int: ...
    def parse(self, p0: str) -> bool: ...
    def before(self, p0: "Time") -> bool: ...
    def after(self, p0: "Time") -> bool: ...
    def normalize(self, p0: bool) -> int: ...
    def getActualMaximum(self, p0: int) -> int: ...

