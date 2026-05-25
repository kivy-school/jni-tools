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
    sameMonthTable: ClassVar[list[int]]
    sameYearTable: ClassVar[list[int]]
    def __init__(self) -> None: ...
    @staticmethod
    def getDayOfWeekString(arg0: int, arg1: int) -> str: ...
    @staticmethod
    def getAMPMString(arg0: int) -> str: ...
    @staticmethod
    def getMonthString(arg0: int, arg1: int) -> str: ...
    @overload
    @staticmethod
    def getRelativeTimeSpanString(arg0: int) -> str: ...
    @overload
    @staticmethod
    def getRelativeTimeSpanString(arg0: int, arg1: int, arg2: int) -> str: ...
    @overload
    @staticmethod
    def getRelativeTimeSpanString(arg0: int, arg1: int, arg2: int, arg3: int) -> str: ...
    @overload
    @staticmethod
    def getRelativeTimeSpanString(arg0: Context, arg1: int, arg2: bool) -> str: ...
    @overload
    @staticmethod
    def getRelativeTimeSpanString(arg0: Context, arg1: int) -> str: ...
    @staticmethod
    def getRelativeDateTimeString(arg0: Context, arg1: int, arg2: int, arg3: int, arg4: int) -> str: ...
    @overload
    @staticmethod
    def formatElapsedTime(arg0: int) -> str: ...
    @overload
    @staticmethod
    def formatElapsedTime(arg0: StringBuilder, arg1: int) -> str: ...
    @staticmethod
    def formatSameDayTime(arg0: int, arg1: int, arg2: int, arg3: int) -> str: ...
    @staticmethod
    def isToday(arg0: int) -> bool: ...
    @overload
    @staticmethod
    def formatDateRange(arg0: Context, arg1: int, arg2: int, arg3: int) -> str: ...
    @overload
    @staticmethod
    def formatDateRange(arg0: Context, arg1: Formatter, arg2: int, arg3: int, arg4: int) -> Formatter: ...
    @overload
    @staticmethod
    def formatDateRange(arg0: Context, arg1: Formatter, arg2: int, arg3: int, arg4: int, arg5: str) -> Formatter: ...
    @staticmethod
    def formatDateTime(arg0: Context, arg1: int, arg2: int) -> str: ...
