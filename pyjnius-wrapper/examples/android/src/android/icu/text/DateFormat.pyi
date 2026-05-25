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

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Type:
    """Forward declaration for ``android.icu.text.DisplayContext.Type``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.icu.text.DisplayContext.Type')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/icu/text/DisplayContext/Type
    """
    ...

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
    calendar: Calendar
    numberFormat: NumberFormat
    def __init__(self) -> None: ...
    @overload
    def format(self, arg0: Any, arg1: StringBuffer, arg2: FieldPosition) -> StringBuffer: ...
    @overload
    def format(self, arg0: Calendar, arg1: StringBuffer, arg2: FieldPosition) -> StringBuffer: ...
    @overload
    def format(self, arg0: Date, arg1: StringBuffer, arg2: FieldPosition) -> StringBuffer: ...
    @overload
    def format(self, arg0: Date) -> str: ...
    @overload
    def parse(self, arg0: str) -> Date: ...
    @overload
    def parse(self, arg0: str, arg1: Calendar, arg2: ParsePosition) -> None: ...
    @overload
    def parse(self, arg0: str, arg1: ParsePosition) -> Date: ...
    def parseObject(self, arg0: str, arg1: ParsePosition) -> Any: ...
    @overload
    @staticmethod
    def getTimeInstance() -> "DateFormat": ...
    @overload
    @staticmethod
    def getTimeInstance(arg0: int) -> "DateFormat": ...
    @overload
    @staticmethod
    def getTimeInstance(arg0: int, arg1: Locale) -> "DateFormat": ...
    @overload
    @staticmethod
    def getTimeInstance(arg0: int, arg1: ULocale) -> "DateFormat": ...
    @overload
    @staticmethod
    def getTimeInstance(arg0: Calendar, arg1: int, arg2: Locale) -> "DateFormat": ...
    @overload
    @staticmethod
    def getTimeInstance(arg0: Calendar, arg1: int, arg2: ULocale) -> "DateFormat": ...
    @overload
    @staticmethod
    def getTimeInstance(arg0: Calendar, arg1: int) -> "DateFormat": ...
    @overload
    @staticmethod
    def getDateInstance() -> "DateFormat": ...
    @overload
    @staticmethod
    def getDateInstance(arg0: int) -> "DateFormat": ...
    @overload
    @staticmethod
    def getDateInstance(arg0: int, arg1: Locale) -> "DateFormat": ...
    @overload
    @staticmethod
    def getDateInstance(arg0: int, arg1: ULocale) -> "DateFormat": ...
    @overload
    @staticmethod
    def getDateInstance(arg0: Calendar, arg1: int, arg2: Locale) -> "DateFormat": ...
    @overload
    @staticmethod
    def getDateInstance(arg0: Calendar, arg1: int, arg2: ULocale) -> "DateFormat": ...
    @overload
    @staticmethod
    def getDateInstance(arg0: Calendar, arg1: int) -> "DateFormat": ...
    @overload
    @staticmethod
    def getDateTimeInstance() -> "DateFormat": ...
    @overload
    @staticmethod
    def getDateTimeInstance(arg0: int, arg1: int) -> "DateFormat": ...
    @overload
    @staticmethod
    def getDateTimeInstance(arg0: int, arg1: int, arg2: Locale) -> "DateFormat": ...
    @overload
    @staticmethod
    def getDateTimeInstance(arg0: int, arg1: int, arg2: ULocale) -> "DateFormat": ...
    @overload
    @staticmethod
    def getDateTimeInstance(arg0: Calendar, arg1: int, arg2: int, arg3: Locale) -> "DateFormat": ...
    @overload
    @staticmethod
    def getDateTimeInstance(arg0: Calendar, arg1: int, arg2: int, arg3: ULocale) -> "DateFormat": ...
    @overload
    @staticmethod
    def getDateTimeInstance(arg0: Calendar, arg1: int, arg2: int) -> "DateFormat": ...
    @overload
    @staticmethod
    def getInstance() -> "DateFormat": ...
    @overload
    @staticmethod
    def getInstance(arg0: Calendar, arg1: Locale) -> "DateFormat": ...
    @overload
    @staticmethod
    def getInstance(arg0: Calendar, arg1: ULocale) -> "DateFormat": ...
    @overload
    @staticmethod
    def getInstance(arg0: Calendar) -> "DateFormat": ...
    @staticmethod
    def getAvailableLocales() -> list[Locale]: ...
    def setCalendar(self, arg0: Calendar) -> None: ...
    def getCalendar(self) -> Calendar: ...
    def setNumberFormat(self, arg0: NumberFormat) -> None: ...
    def getNumberFormat(self) -> NumberFormat: ...
    def setTimeZone(self, arg0: TimeZone) -> None: ...
    def getTimeZone(self) -> TimeZone: ...
    def setLenient(self, arg0: bool) -> None: ...
    def isLenient(self) -> bool: ...
    def setCalendarLenient(self, arg0: bool) -> None: ...
    def isCalendarLenient(self) -> bool: ...
    def setBooleanAttribute(self, arg0: "BooleanAttribute", arg1: bool) -> "DateFormat": ...
    def getBooleanAttribute(self, arg0: "BooleanAttribute") -> bool: ...
    def setContext(self, arg0: DisplayContext) -> None: ...
    def getContext(self, arg0: Type) -> DisplayContext: ...
    def hashCode(self) -> int: ...
    def equals(self, arg0: Any) -> bool: ...
    def clone(self) -> Any: ...
    @overload
    @staticmethod
    def getInstanceForSkeleton(arg0: str) -> "DateFormat": ...
    @overload
    @staticmethod
    def getInstanceForSkeleton(arg0: str, arg1: Locale) -> "DateFormat": ...
    @overload
    @staticmethod
    def getInstanceForSkeleton(arg0: str, arg1: ULocale) -> "DateFormat": ...
    @overload
    @staticmethod
    def getInstanceForSkeleton(arg0: Calendar, arg1: str, arg2: Locale) -> "DateFormat": ...
    @overload
    @staticmethod
    def getInstanceForSkeleton(arg0: Calendar, arg1: str, arg2: ULocale) -> "DateFormat": ...
    @overload
    @staticmethod
    def getPatternInstance(arg0: str) -> "DateFormat": ...
    @overload
    @staticmethod
    def getPatternInstance(arg0: str, arg1: Locale) -> "DateFormat": ...
    @overload
    @staticmethod
    def getPatternInstance(arg0: str, arg1: ULocale) -> "DateFormat": ...
    @overload
    @staticmethod
    def getPatternInstance(arg0: Calendar, arg1: str, arg2: Locale) -> "DateFormat": ...
    @overload
    @staticmethod
    def getPatternInstance(arg0: Calendar, arg1: str, arg2: ULocale) -> "DateFormat": ...

    class BooleanAttribute:
        PARSE_ALLOW_WHITESPACE: ClassVar["BooleanAttribute"]
        PARSE_ALLOW_NUMERIC: ClassVar["BooleanAttribute"]
        PARSE_MULTIPLE_PATTERNS_FOR_MATCH: ClassVar["BooleanAttribute"]
        PARSE_PARTIAL_LITERAL_MATCH: ClassVar["BooleanAttribute"]
        @staticmethod
        def values() -> list["BooleanAttribute"]: ...
        @staticmethod
        def valueOf(arg0: str) -> "BooleanAttribute": ...

    class Field:
        AM_PM: ClassVar["Field"]
        AM_PM_MIDNIGHT_NOON: ClassVar["Field"]
        DAY_OF_MONTH: ClassVar["Field"]
        DAY_OF_WEEK: ClassVar["Field"]
        DAY_OF_WEEK_IN_MONTH: ClassVar["Field"]
        DAY_OF_YEAR: ClassVar["Field"]
        DOW_LOCAL: ClassVar["Field"]
        ERA: ClassVar["Field"]
        EXTENDED_YEAR: ClassVar["Field"]
        FLEXIBLE_DAY_PERIOD: ClassVar["Field"]
        HOUR0: ClassVar["Field"]
        HOUR1: ClassVar["Field"]
        HOUR_OF_DAY0: ClassVar["Field"]
        HOUR_OF_DAY1: ClassVar["Field"]
        JULIAN_DAY: ClassVar["Field"]
        MILLISECOND: ClassVar["Field"]
        MILLISECONDS_IN_DAY: ClassVar["Field"]
        MINUTE: ClassVar["Field"]
        MONTH: ClassVar["Field"]
        QUARTER: ClassVar["Field"]
        SECOND: ClassVar["Field"]
        TIME_ZONE: ClassVar["Field"]
        WEEK_OF_MONTH: ClassVar["Field"]
        WEEK_OF_YEAR: ClassVar["Field"]
        YEAR: ClassVar["Field"]
        YEAR_WOY: ClassVar["Field"]
        def __init__(self, arg0: str, arg1: int) -> None: ...
        @staticmethod
        def ofCalendarField(arg0: int) -> "Field": ...
        def getCalendarField(self) -> int: ...
        def readResolve(self) -> Any: ...

    class HourCycle:
        HOUR_CYCLE_11: ClassVar["HourCycle"]
        HOUR_CYCLE_12: ClassVar["HourCycle"]
        HOUR_CYCLE_23: ClassVar["HourCycle"]
        HOUR_CYCLE_24: ClassVar["HourCycle"]
        @staticmethod
        def values() -> list["HourCycle"]: ...
        @staticmethod
        def valueOf(arg0: str) -> "HourCycle": ...
