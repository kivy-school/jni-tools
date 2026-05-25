from typing import Any, ClassVar, overload
from android.icu.text.DisplayContext import DisplayContext
from android.icu.text.NumberFormat import NumberFormat
from android.icu.util.Calendar import Calendar
from android.icu.util.TimeZone import TimeZone
from android.icu.util.ULocale import ULocale
from java.lang.StringBuffer import StringBuffer
from java.text.FieldPosition import FieldPosition
from java.text.ParsePosition import ParsePosition
from java.util.Date import Date
from java.util.Locale import Locale

class DateFormat:
    ABBR_GENERIC_TZ: ClassVar[str]
    ABBR_MONTH: ClassVar[str]
    ABBR_MONTH_DAY: ClassVar[str]
    ABBR_MONTH_WEEKDAY_DAY: ClassVar[str]
    ABBR_QUARTER: ClassVar[str]
    ABBR_SPECIFIC_TZ: ClassVar[str]
    ABBR_UTC_TZ: ClassVar[str]
    ABBR_WEEKDAY: ClassVar[str]
    AM_PM_FIELD: ClassVar[int]
    AM_PM_MIDNIGHT_NOON_FIELD: ClassVar[int]
    DATE_FIELD: ClassVar[int]
    DAY: ClassVar[str]
    DAY_OF_WEEK_FIELD: ClassVar[int]
    DAY_OF_WEEK_IN_MONTH_FIELD: ClassVar[int]
    DAY_OF_YEAR_FIELD: ClassVar[int]
    DEFAULT: ClassVar[int]
    DOW_LOCAL_FIELD: ClassVar[int]
    ERA_FIELD: ClassVar[int]
    EXTENDED_YEAR_FIELD: ClassVar[int]
    FLEXIBLE_DAY_PERIOD_FIELD: ClassVar[int]
    FRACTIONAL_SECOND_FIELD: ClassVar[int]
    FULL: ClassVar[int]
    GENERIC_TZ: ClassVar[str]
    HOUR: ClassVar[str]
    HOUR0_FIELD: ClassVar[int]
    HOUR1_FIELD: ClassVar[int]
    HOUR24: ClassVar[str]
    HOUR24_MINUTE: ClassVar[str]
    HOUR24_MINUTE_SECOND: ClassVar[str]
    HOUR_MINUTE: ClassVar[str]
    HOUR_MINUTE_SECOND: ClassVar[str]
    HOUR_OF_DAY0_FIELD: ClassVar[int]
    HOUR_OF_DAY1_FIELD: ClassVar[int]
    JULIAN_DAY_FIELD: ClassVar[int]
    LOCATION_TZ: ClassVar[str]
    LONG: ClassVar[int]
    MEDIUM: ClassVar[int]
    MILLISECONDS_IN_DAY_FIELD: ClassVar[int]
    MILLISECOND_FIELD: ClassVar[int]
    MINUTE: ClassVar[str]
    MINUTE_FIELD: ClassVar[int]
    MINUTE_SECOND: ClassVar[str]
    MONTH: ClassVar[str]
    MONTH_DAY: ClassVar[str]
    MONTH_FIELD: ClassVar[int]
    MONTH_WEEKDAY_DAY: ClassVar[str]
    NONE: ClassVar[int]
    NUM_MONTH: ClassVar[str]
    NUM_MONTH_DAY: ClassVar[str]
    NUM_MONTH_WEEKDAY_DAY: ClassVar[str]
    QUARTER: ClassVar[str]
    QUARTER_FIELD: ClassVar[int]
    RELATIVE: ClassVar[int]
    RELATIVE_DEFAULT: ClassVar[int]
    RELATIVE_FULL: ClassVar[int]
    RELATIVE_LONG: ClassVar[int]
    RELATIVE_MEDIUM: ClassVar[int]
    RELATIVE_SHORT: ClassVar[int]
    SECOND: ClassVar[str]
    SECOND_FIELD: ClassVar[int]
    SHORT: ClassVar[int]
    SPECIFIC_TZ: ClassVar[str]
    STANDALONE_DAY_FIELD: ClassVar[int]
    STANDALONE_MONTH_FIELD: ClassVar[int]
    STANDALONE_QUARTER_FIELD: ClassVar[int]
    TIMEZONE_FIELD: ClassVar[int]
    TIMEZONE_GENERIC_FIELD: ClassVar[int]
    TIMEZONE_ISO_FIELD: ClassVar[int]
    TIMEZONE_ISO_LOCAL_FIELD: ClassVar[int]
    TIMEZONE_LOCALIZED_GMT_OFFSET_FIELD: ClassVar[int]
    TIMEZONE_RFC_FIELD: ClassVar[int]
    TIMEZONE_SPECIAL_FIELD: ClassVar[int]
    WEEKDAY: ClassVar[str]
    WEEK_OF_MONTH_FIELD: ClassVar[int]
    WEEK_OF_YEAR_FIELD: ClassVar[int]
    YEAR: ClassVar[str]
    YEAR_ABBR_MONTH: ClassVar[str]
    YEAR_ABBR_MONTH_DAY: ClassVar[str]
    YEAR_ABBR_MONTH_WEEKDAY_DAY: ClassVar[str]
    YEAR_ABBR_QUARTER: ClassVar[str]
    YEAR_FIELD: ClassVar[int]
    YEAR_MONTH: ClassVar[str]
    YEAR_MONTH_DAY: ClassVar[str]
    YEAR_MONTH_WEEKDAY_DAY: ClassVar[str]
    YEAR_NAME_FIELD: ClassVar[int]
    YEAR_NUM_MONTH: ClassVar[str]
    YEAR_NUM_MONTH_DAY: ClassVar[str]
    YEAR_NUM_MONTH_WEEKDAY_DAY: ClassVar[str]
    YEAR_QUARTER: ClassVar[str]
    YEAR_WOY_FIELD: ClassVar[int]
    def setLenient(self, p0: bool) -> None: ...
    def isLenient(self) -> bool: ...
    def parseObject(self, p0: str, p1: ParsePosition) -> Any: ...
    @overload
    @staticmethod
    def getTimeInstance() -> "DateFormat": ...
    @overload
    @staticmethod
    def getTimeInstance(p0: Calendar, p1: int) -> "DateFormat": ...
    @overload
    @staticmethod
    def getTimeInstance(p0: int) -> "DateFormat": ...
    @overload
    @staticmethod
    def getTimeInstance(p0: int, p1: Locale) -> "DateFormat": ...
    @overload
    @staticmethod
    def getTimeInstance(p0: int, p1: ULocale) -> "DateFormat": ...
    @overload
    @staticmethod
    def getTimeInstance(p0: Calendar, p1: int, p2: Locale) -> "DateFormat": ...
    @overload
    @staticmethod
    def getTimeInstance(p0: Calendar, p1: int, p2: ULocale) -> "DateFormat": ...
    @overload
    @staticmethod
    def getDateInstance() -> "DateFormat": ...
    @overload
    @staticmethod
    def getDateInstance(p0: int) -> "DateFormat": ...
    @overload
    @staticmethod
    def getDateInstance(p0: int, p1: ULocale) -> "DateFormat": ...
    @overload
    @staticmethod
    def getDateInstance(p0: int, p1: Locale) -> "DateFormat": ...
    @overload
    @staticmethod
    def getDateInstance(p0: Calendar, p1: int, p2: ULocale) -> "DateFormat": ...
    @overload
    @staticmethod
    def getDateInstance(p0: Calendar, p1: int, p2: Locale) -> "DateFormat": ...
    @overload
    @staticmethod
    def getDateInstance(p0: Calendar, p1: int) -> "DateFormat": ...
    @overload
    @staticmethod
    def getDateTimeInstance(p0: int, p1: int, p2: ULocale) -> "DateFormat": ...
    @overload
    @staticmethod
    def getDateTimeInstance(p0: Calendar, p1: int, p2: int, p3: ULocale) -> "DateFormat": ...
    @overload
    @staticmethod
    def getDateTimeInstance(p0: Calendar, p1: int, p2: int, p3: Locale) -> "DateFormat": ...
    @overload
    @staticmethod
    def getDateTimeInstance(p0: Calendar, p1: int, p2: int) -> "DateFormat": ...
    @overload
    @staticmethod
    def getDateTimeInstance() -> "DateFormat": ...
    @overload
    @staticmethod
    def getDateTimeInstance(p0: int, p1: int) -> "DateFormat": ...
    @overload
    @staticmethod
    def getDateTimeInstance(p0: int, p1: int, p2: Locale) -> "DateFormat": ...
    def setCalendar(self, p0: Calendar) -> None: ...
    def getCalendar(self) -> Calendar: ...
    def setNumberFormat(self, p0: NumberFormat) -> None: ...
    def getNumberFormat(self) -> NumberFormat: ...
    def setCalendarLenient(self, p0: bool) -> None: ...
    def isCalendarLenient(self) -> bool: ...
    def setBooleanAttribute(self, p0: Any, p1: bool) -> "DateFormat": ...
    def getBooleanAttribute(self, p0: Any) -> bool: ...
    def setContext(self, p0: DisplayContext) -> None: ...
    @overload
    @staticmethod
    def getInstanceForSkeleton(p0: Calendar, p1: str, p2: ULocale) -> "DateFormat": ...
    @overload
    @staticmethod
    def getInstanceForSkeleton(p0: str, p1: Locale) -> "DateFormat": ...
    @overload
    @staticmethod
    def getInstanceForSkeleton(p0: str) -> "DateFormat": ...
    @overload
    @staticmethod
    def getInstanceForSkeleton(p0: str, p1: ULocale) -> "DateFormat": ...
    @overload
    @staticmethod
    def getInstanceForSkeleton(p0: Calendar, p1: str, p2: Locale) -> "DateFormat": ...
    @overload
    @staticmethod
    def getPatternInstance(p0: str, p1: ULocale) -> "DateFormat": ...
    @overload
    @staticmethod
    def getPatternInstance(p0: Calendar, p1: str, p2: Locale) -> "DateFormat": ...
    @overload
    @staticmethod
    def getPatternInstance(p0: str) -> "DateFormat": ...
    @overload
    @staticmethod
    def getPatternInstance(p0: str, p1: Locale) -> "DateFormat": ...
    @overload
    @staticmethod
    def getPatternInstance(p0: Calendar, p1: str, p2: ULocale) -> "DateFormat": ...
    def getTimeZone(self) -> TimeZone: ...
    def setTimeZone(self, p0: TimeZone) -> None: ...
    @staticmethod
    def getAvailableLocales() -> Any: ...
    def equals(self, p0: Any) -> bool: ...
    def hashCode(self) -> int: ...
    def clone(self) -> Any: ...
    @overload
    def format(self, p0: Date) -> str: ...
    @overload
    def format(self, p0: Any, p1: StringBuffer, p2: FieldPosition) -> StringBuffer: ...
    @overload
    def format(self, p0: Calendar, p1: StringBuffer, p2: FieldPosition) -> StringBuffer: ...
    @overload
    def format(self, p0: Date, p1: StringBuffer, p2: FieldPosition) -> StringBuffer: ...
    @overload
    @staticmethod
    def getInstance(p0: Calendar, p1: ULocale) -> "DateFormat": ...
    @overload
    @staticmethod
    def getInstance(p0: Calendar) -> "DateFormat": ...
    @overload
    @staticmethod
    def getInstance(p0: Calendar, p1: Locale) -> "DateFormat": ...
    @overload
    @staticmethod
    def getInstance() -> "DateFormat": ...
    def getContext(self, p0: Any) -> DisplayContext: ...
    @overload
    def parse(self, p0: str, p1: ParsePosition) -> Date: ...
    @overload
    def parse(self, p0: str, p1: Calendar, p2: ParsePosition) -> None: ...
    @overload
    def parse(self, p0: str) -> Date: ...

    class HourCycle:
        HOUR_CYCLE_11: ClassVar["HourCycle"]
        HOUR_CYCLE_12: ClassVar["HourCycle"]
        HOUR_CYCLE_23: ClassVar["HourCycle"]
        HOUR_CYCLE_24: ClassVar["HourCycle"]
        HOUR_CYCLE_11: ClassVar[Any]
        HOUR_CYCLE_12: ClassVar[Any]
        HOUR_CYCLE_23: ClassVar[Any]
        HOUR_CYCLE_24: ClassVar[Any]
        @staticmethod
        def values() -> Any: ...
        @staticmethod
        def valueOf(p0: str) -> Any: ...

    class Field:
        AM_PM: ClassVar[Any]
        AM_PM_MIDNIGHT_NOON: ClassVar[Any]
        DAY_OF_MONTH: ClassVar[Any]
        DAY_OF_WEEK: ClassVar[Any]
        DAY_OF_WEEK_IN_MONTH: ClassVar[Any]
        DAY_OF_YEAR: ClassVar[Any]
        DOW_LOCAL: ClassVar[Any]
        ERA: ClassVar[Any]
        EXTENDED_YEAR: ClassVar[Any]
        FLEXIBLE_DAY_PERIOD: ClassVar[Any]
        HOUR0: ClassVar[Any]
        HOUR1: ClassVar[Any]
        HOUR_OF_DAY0: ClassVar[Any]
        HOUR_OF_DAY1: ClassVar[Any]
        JULIAN_DAY: ClassVar[Any]
        MILLISECOND: ClassVar[Any]
        MILLISECONDS_IN_DAY: ClassVar[Any]
        MINUTE: ClassVar[Any]
        MONTH: ClassVar[Any]
        QUARTER: ClassVar[Any]
        SECOND: ClassVar[Any]
        TIME_ZONE: ClassVar[Any]
        WEEK_OF_MONTH: ClassVar[Any]
        WEEK_OF_YEAR: ClassVar[Any]
        YEAR: ClassVar[Any]
        YEAR_WOY: ClassVar[Any]
        LANGUAGE: ClassVar[Any]
        READING: ClassVar[Any]
        INPUT_METHOD_SEGMENT: ClassVar[Any]
        @staticmethod
        def ofCalendarField(p0: int) -> Any: ...
        def getCalendarField(self) -> int: ...

    class BooleanAttribute:
        PARSE_ALLOW_WHITESPACE: ClassVar["BooleanAttribute"]
        PARSE_ALLOW_NUMERIC: ClassVar["BooleanAttribute"]
        PARSE_MULTIPLE_PATTERNS_FOR_MATCH: ClassVar["BooleanAttribute"]
        PARSE_PARTIAL_LITERAL_MATCH: ClassVar["BooleanAttribute"]
        PARSE_ALLOW_WHITESPACE: ClassVar[Any]
        PARSE_ALLOW_NUMERIC: ClassVar[Any]
        PARSE_MULTIPLE_PATTERNS_FOR_MATCH: ClassVar[Any]
        PARSE_PARTIAL_LITERAL_MATCH: ClassVar[Any]
        @staticmethod
        def values() -> Any: ...
        @staticmethod
        def valueOf(p0: str) -> Any: ...
