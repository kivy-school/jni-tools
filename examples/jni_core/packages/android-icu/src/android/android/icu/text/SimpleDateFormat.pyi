from typing import Any, ClassVar, overload
from android.icu.text.DateFormatSymbols import DateFormatSymbols
from android.icu.text.DisplayContext import DisplayContext
from android.icu.text.NumberFormat import NumberFormat
from android.icu.text.TimeZoneFormat import TimeZoneFormat
from android.icu.util.Calendar import Calendar
from android.icu.util.ULocale import ULocale
from java.lang.StringBuffer import StringBuffer
from java.text.AttributedCharacterIterator import AttributedCharacterIterator
from java.text.FieldPosition import FieldPosition
from java.text.ParsePosition import ParsePosition
from java.util.Date import Date
from java.util.Locale import Locale

class SimpleDateFormat:
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
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, p0: str, p1: str, p2: ULocale) -> None: ...
    @overload
    def __init__(self, p0: str, p1: Locale) -> None: ...
    @overload
    def __init__(self, p0: str) -> None: ...
    @overload
    def __init__(self, p0: str, p1: DateFormatSymbols) -> None: ...
    @overload
    def __init__(self, p0: str, p1: ULocale) -> None: ...
    def applyLocalizedPattern(self, p0: str) -> None: ...
    def toLocalizedPattern(self) -> str: ...
    def applyPattern(self, p0: str) -> None: ...
    def set2DigitYearStart(self, p0: Date) -> None: ...
    def get2DigitYearStart(self) -> Date: ...
    def getDateFormatSymbols(self) -> DateFormatSymbols: ...
    def setDateFormatSymbols(self, p0: DateFormatSymbols) -> None: ...
    def getTimeZoneFormat(self) -> TimeZoneFormat: ...
    def setTimeZoneFormat(self, p0: TimeZoneFormat) -> None: ...
    @overload
    def setNumberFormat(self, p0: str, p1: NumberFormat) -> None: ...
    @overload
    def setNumberFormat(self, p0: NumberFormat) -> None: ...
    def getNumberFormat(self, p0: str) -> NumberFormat: ...
    def setContext(self, p0: DisplayContext) -> None: ...
    def equals(self, p0: Any) -> bool: ...
    def hashCode(self) -> int: ...
    def clone(self) -> Any: ...
    def format(self, p0: Calendar, p1: StringBuffer, p2: FieldPosition) -> StringBuffer: ...
    def parse(self, p0: str, p1: Calendar, p2: ParsePosition) -> None: ...
    def toPattern(self) -> str: ...
    def formatToCharacterIterator(self, p0: Any) -> AttributedCharacterIterator: ...
