from typing import Any, ClassVar, overload
from java.lang.StringBuffer import StringBuffer
from java.text.FieldPosition import FieldPosition
from java.text.NumberFormat import NumberFormat
from java.text.ParsePosition import ParsePosition
from java.util.Calendar import Calendar
from java.util.Date import Date
from java.util.Locale import Locale
from java.util.TimeZone import TimeZone

class DateFormat:
    AM_PM_FIELD: ClassVar[int]
    DATE_FIELD: ClassVar[int]
    DAY_OF_WEEK_FIELD: ClassVar[int]
    DAY_OF_WEEK_IN_MONTH_FIELD: ClassVar[int]
    DAY_OF_YEAR_FIELD: ClassVar[int]
    DEFAULT: ClassVar[int]
    ERA_FIELD: ClassVar[int]
    FULL: ClassVar[int]
    HOUR0_FIELD: ClassVar[int]
    HOUR1_FIELD: ClassVar[int]
    HOUR_OF_DAY0_FIELD: ClassVar[int]
    HOUR_OF_DAY1_FIELD: ClassVar[int]
    LONG: ClassVar[int]
    MEDIUM: ClassVar[int]
    MILLISECOND_FIELD: ClassVar[int]
    MINUTE_FIELD: ClassVar[int]
    MONTH_FIELD: ClassVar[int]
    SECOND_FIELD: ClassVar[int]
    SHORT: ClassVar[int]
    TIMEZONE_FIELD: ClassVar[int]
    WEEK_OF_MONTH_FIELD: ClassVar[int]
    WEEK_OF_YEAR_FIELD: ClassVar[int]
    YEAR_FIELD: ClassVar[int]
    calendar: Calendar
    numberFormat: NumberFormat
    def __init__(self) -> None: ...
    @overload
    def format(self, arg0: Any, arg1: StringBuffer, arg2: FieldPosition) -> StringBuffer: ...
    @overload
    def format(self, arg0: Date, arg1: StringBuffer, arg2: FieldPosition) -> StringBuffer: ...
    @overload
    def format(self, arg0: Date) -> str: ...
    @overload
    def parse(self, arg0: str) -> Date: ...
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
    def getDateInstance() -> "DateFormat": ...
    @overload
    @staticmethod
    def getDateInstance(arg0: int) -> "DateFormat": ...
    @overload
    @staticmethod
    def getDateInstance(arg0: int, arg1: Locale) -> "DateFormat": ...
    @overload
    @staticmethod
    def getDateTimeInstance() -> "DateFormat": ...
    @overload
    @staticmethod
    def getDateTimeInstance(arg0: int, arg1: int) -> "DateFormat": ...
    @overload
    @staticmethod
    def getDateTimeInstance(arg0: int, arg1: int, arg2: Locale) -> "DateFormat": ...
    @staticmethod
    def getInstance() -> "DateFormat": ...
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
    def hashCode(self) -> int: ...
    def equals(self, arg0: Any) -> bool: ...
    def clone(self) -> Any: ...

    class Field:
        AM_PM: ClassVar["Field"]
        DAY_OF_MONTH: ClassVar["Field"]
        DAY_OF_WEEK: ClassVar["Field"]
        DAY_OF_WEEK_IN_MONTH: ClassVar["Field"]
        DAY_OF_YEAR: ClassVar["Field"]
        ERA: ClassVar["Field"]
        HOUR0: ClassVar["Field"]
        HOUR1: ClassVar["Field"]
        HOUR_OF_DAY0: ClassVar["Field"]
        HOUR_OF_DAY1: ClassVar["Field"]
        MILLISECOND: ClassVar["Field"]
        MINUTE: ClassVar["Field"]
        MONTH: ClassVar["Field"]
        SECOND: ClassVar["Field"]
        TIME_ZONE: ClassVar["Field"]
        WEEK_OF_MONTH: ClassVar["Field"]
        WEEK_OF_YEAR: ClassVar["Field"]
        YEAR: ClassVar["Field"]
        def __init__(self, arg0: str, arg1: int) -> None: ...
        @staticmethod
        def ofCalendarField(arg0: int) -> "Field": ...
        def getCalendarField(self) -> int: ...
        def readResolve(self) -> Any: ...
