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
    ERA_FIELD: ClassVar[int]
    YEAR_FIELD: ClassVar[int]
    MONTH_FIELD: ClassVar[int]
    DATE_FIELD: ClassVar[int]
    HOUR_OF_DAY1_FIELD: ClassVar[int]
    HOUR_OF_DAY0_FIELD: ClassVar[int]
    MINUTE_FIELD: ClassVar[int]
    SECOND_FIELD: ClassVar[int]
    MILLISECOND_FIELD: ClassVar[int]
    DAY_OF_WEEK_FIELD: ClassVar[int]
    DAY_OF_YEAR_FIELD: ClassVar[int]
    DAY_OF_WEEK_IN_MONTH_FIELD: ClassVar[int]
    WEEK_OF_YEAR_FIELD: ClassVar[int]
    WEEK_OF_MONTH_FIELD: ClassVar[int]
    AM_PM_FIELD: ClassVar[int]
    HOUR1_FIELD: ClassVar[int]
    HOUR0_FIELD: ClassVar[int]
    TIMEZONE_FIELD: ClassVar[int]
    FULL: ClassVar[int]
    LONG: ClassVar[int]
    MEDIUM: ClassVar[int]
    SHORT: ClassVar[int]
    DEFAULT: ClassVar[int]
    def isLenient(self) -> bool: ...
    def setLenient(self, p0: bool) -> None: ...
    def equals(self, p0: Any) -> bool: ...
    def hashCode(self) -> int: ...
    def clone(self) -> Any: ...
    @overload
    def format(self, p0: Any, p1: StringBuffer, p2: FieldPosition) -> StringBuffer: ...
    @overload
    def format(self, p0: Date, p1: StringBuffer, p2: FieldPosition) -> StringBuffer: ...
    @overload
    def format(self, p0: Date) -> str: ...
    @staticmethod
    def getInstance() -> "DateFormat": ...
    @overload
    def parse(self, p0: str, p1: ParsePosition) -> Date: ...
    @overload
    def parse(self, p0: str) -> Date: ...
    def getTimeZone(self) -> TimeZone: ...
    def setTimeZone(self, p0: TimeZone) -> None: ...
    def getCalendar(self) -> Calendar: ...
    @overload
    @staticmethod
    def getDateInstance() -> "DateFormat": ...
    @overload
    @staticmethod
    def getDateInstance(p0: int) -> "DateFormat": ...
    @overload
    @staticmethod
    def getDateInstance(p0: int, p1: Locale) -> "DateFormat": ...
    @overload
    @staticmethod
    def getDateTimeInstance(p0: int, p1: int, p2: Locale) -> "DateFormat": ...
    @overload
    @staticmethod
    def getDateTimeInstance(p0: int, p1: int) -> "DateFormat": ...
    @overload
    @staticmethod
    def getDateTimeInstance() -> "DateFormat": ...
    def getNumberFormat(self) -> NumberFormat: ...
    @overload
    @staticmethod
    def getTimeInstance() -> "DateFormat": ...
    @overload
    @staticmethod
    def getTimeInstance(p0: int) -> "DateFormat": ...
    @overload
    @staticmethod
    def getTimeInstance(p0: int, p1: Locale) -> "DateFormat": ...
    def parseObject(self, p0: str, p1: ParsePosition) -> Any: ...
    def setCalendar(self, p0: Calendar) -> None: ...
    def setNumberFormat(self, p0: NumberFormat) -> None: ...
    @staticmethod
    def getAvailableLocales() -> Any: ...

    class Field:
        ERA: ClassVar[Any]
        YEAR: ClassVar[Any]
        MONTH: ClassVar[Any]
        DAY_OF_MONTH: ClassVar[Any]
        HOUR_OF_DAY1: ClassVar[Any]
        HOUR_OF_DAY0: ClassVar[Any]
        MINUTE: ClassVar[Any]
        SECOND: ClassVar[Any]
        MILLISECOND: ClassVar[Any]
        DAY_OF_WEEK: ClassVar[Any]
        DAY_OF_YEAR: ClassVar[Any]
        DAY_OF_WEEK_IN_MONTH: ClassVar[Any]
        WEEK_OF_YEAR: ClassVar[Any]
        WEEK_OF_MONTH: ClassVar[Any]
        AM_PM: ClassVar[Any]
        HOUR1: ClassVar[Any]
        HOUR0: ClassVar[Any]
        TIME_ZONE: ClassVar[Any]
        LANGUAGE: ClassVar[Any]
        READING: ClassVar[Any]
        INPUT_METHOD_SEGMENT: ClassVar[Any]
        def getCalendarField(self) -> int: ...
        @staticmethod
        def ofCalendarField(p0: int) -> Any: ...
