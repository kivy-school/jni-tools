from typing import Any, ClassVar, overload
from android.icu.text.ConstrainedFieldPosition import ConstrainedFieldPosition
from android.icu.text.DisplayContext import DisplayContext
from android.icu.text.NumberFormat import NumberFormat
from android.icu.util.ULocale import ULocale
from java.lang.Appendable import Appendable
from java.text.AttributedCharacterIterator import AttributedCharacterIterator
from java.util.Locale import Locale

class RelativeDateTimeFormatter:
    def getNumberFormat(self) -> NumberFormat: ...
    def combineDateAndTime(self, p0: str, p1: str) -> str: ...
    def formatNumeric(self, p0: float, p1: Any) -> str: ...
    def formatNumericToValue(self, p0: float, p1: Any) -> Any: ...
    def getCapitalizationContext(self) -> DisplayContext: ...
    def getFormatStyle(self) -> Any: ...
    @overload
    def formatToValue(self, p0: float, p1: Any, p2: Any) -> Any: ...
    @overload
    def formatToValue(self, p0: float, p1: Any) -> Any: ...
    @overload
    def formatToValue(self, p0: Any, p1: Any) -> Any: ...
    @overload
    def format(self, p0: float, p1: Any) -> str: ...
    @overload
    def format(self, p0: Any, p1: Any) -> str: ...
    @overload
    def format(self, p0: float, p1: Any, p2: Any) -> str: ...
    @overload
    @staticmethod
    def getInstance(p0: Locale) -> "RelativeDateTimeFormatter": ...
    @overload
    @staticmethod
    def getInstance(p0: Locale, p1: NumberFormat) -> "RelativeDateTimeFormatter": ...
    @overload
    @staticmethod
    def getInstance(p0: ULocale) -> "RelativeDateTimeFormatter": ...
    @overload
    @staticmethod
    def getInstance(p0: ULocale, p1: NumberFormat, p2: Any, p3: DisplayContext) -> "RelativeDateTimeFormatter": ...
    @overload
    @staticmethod
    def getInstance(p0: ULocale, p1: NumberFormat) -> "RelativeDateTimeFormatter": ...
    @overload
    @staticmethod
    def getInstance() -> "RelativeDateTimeFormatter": ...

    class Style:
        LONG: ClassVar["Style"]
        NARROW: ClassVar["Style"]
        SHORT: ClassVar["Style"]
        LONG: ClassVar[Any]
        NARROW: ClassVar[Any]
        SHORT: ClassVar[Any]
        @staticmethod
        def values() -> Any: ...
        @staticmethod
        def valueOf(p0: str) -> Any: ...

    class RelativeUnit:
        DAYS: ClassVar["RelativeUnit"]
        HOURS: ClassVar["RelativeUnit"]
        MINUTES: ClassVar["RelativeUnit"]
        MONTHS: ClassVar["RelativeUnit"]
        SECONDS: ClassVar["RelativeUnit"]
        WEEKS: ClassVar["RelativeUnit"]
        YEARS: ClassVar["RelativeUnit"]
        DAYS: ClassVar[Any]
        HOURS: ClassVar[Any]
        MINUTES: ClassVar[Any]
        MONTHS: ClassVar[Any]
        SECONDS: ClassVar[Any]
        WEEKS: ClassVar[Any]
        YEARS: ClassVar[Any]
        @staticmethod
        def values() -> Any: ...
        @staticmethod
        def valueOf(p0: str) -> Any: ...

    class RelativeDateTimeUnit:
        DAY: ClassVar["RelativeDateTimeUnit"]
        FRIDAY: ClassVar["RelativeDateTimeUnit"]
        HOUR: ClassVar["RelativeDateTimeUnit"]
        MINUTE: ClassVar["RelativeDateTimeUnit"]
        MONDAY: ClassVar["RelativeDateTimeUnit"]
        MONTH: ClassVar["RelativeDateTimeUnit"]
        QUARTER: ClassVar["RelativeDateTimeUnit"]
        SATURDAY: ClassVar["RelativeDateTimeUnit"]
        SECOND: ClassVar["RelativeDateTimeUnit"]
        SUNDAY: ClassVar["RelativeDateTimeUnit"]
        THURSDAY: ClassVar["RelativeDateTimeUnit"]
        TUESDAY: ClassVar["RelativeDateTimeUnit"]
        WEDNESDAY: ClassVar["RelativeDateTimeUnit"]
        WEEK: ClassVar["RelativeDateTimeUnit"]
        YEAR: ClassVar["RelativeDateTimeUnit"]
        DAY: ClassVar[Any]
        FRIDAY: ClassVar[Any]
        HOUR: ClassVar[Any]
        MINUTE: ClassVar[Any]
        MONDAY: ClassVar[Any]
        MONTH: ClassVar[Any]
        QUARTER: ClassVar[Any]
        SATURDAY: ClassVar[Any]
        SECOND: ClassVar[Any]
        SUNDAY: ClassVar[Any]
        THURSDAY: ClassVar[Any]
        TUESDAY: ClassVar[Any]
        WEDNESDAY: ClassVar[Any]
        WEEK: ClassVar[Any]
        YEAR: ClassVar[Any]
        @staticmethod
        def values() -> Any: ...
        @staticmethod
        def valueOf(p0: str) -> Any: ...

    class FormattedRelativeDateTime:
        def appendTo(self, p0: Appendable) -> Appendable: ...
        def nextPosition(self, p0: ConstrainedFieldPosition) -> bool: ...
        def toCharacterIterator(self) -> AttributedCharacterIterator: ...
        def length(self) -> int: ...
        def toString(self) -> str: ...
        def charAt(self, p0: int) -> str: ...
        def subSequence(self, p0: int, p1: int) -> str: ...

    class Direction:
        LAST: ClassVar["Direction"]
        LAST_2: ClassVar["Direction"]
        NEXT: ClassVar["Direction"]
        NEXT_2: ClassVar["Direction"]
        PLAIN: ClassVar["Direction"]
        THIS: ClassVar["Direction"]
        LAST: ClassVar[Any]
        LAST_2: ClassVar[Any]
        NEXT: ClassVar[Any]
        NEXT_2: ClassVar[Any]
        PLAIN: ClassVar[Any]
        THIS: ClassVar[Any]
        @staticmethod
        def values() -> Any: ...
        @staticmethod
        def valueOf(p0: str) -> Any: ...

    class AbsoluteUnit:
        DAY: ClassVar["AbsoluteUnit"]
        FRIDAY: ClassVar["AbsoluteUnit"]
        HOUR: ClassVar["AbsoluteUnit"]
        MINUTE: ClassVar["AbsoluteUnit"]
        MONDAY: ClassVar["AbsoluteUnit"]
        MONTH: ClassVar["AbsoluteUnit"]
        NOW: ClassVar["AbsoluteUnit"]
        QUARTER: ClassVar["AbsoluteUnit"]
        SATURDAY: ClassVar["AbsoluteUnit"]
        SUNDAY: ClassVar["AbsoluteUnit"]
        THURSDAY: ClassVar["AbsoluteUnit"]
        TUESDAY: ClassVar["AbsoluteUnit"]
        WEDNESDAY: ClassVar["AbsoluteUnit"]
        WEEK: ClassVar["AbsoluteUnit"]
        YEAR: ClassVar["AbsoluteUnit"]
        DAY: ClassVar[Any]
        FRIDAY: ClassVar[Any]
        HOUR: ClassVar[Any]
        MINUTE: ClassVar[Any]
        MONDAY: ClassVar[Any]
        MONTH: ClassVar[Any]
        NOW: ClassVar[Any]
        QUARTER: ClassVar[Any]
        SATURDAY: ClassVar[Any]
        SUNDAY: ClassVar[Any]
        THURSDAY: ClassVar[Any]
        TUESDAY: ClassVar[Any]
        WEDNESDAY: ClassVar[Any]
        WEEK: ClassVar[Any]
        YEAR: ClassVar[Any]
        @staticmethod
        def values() -> Any: ...
        @staticmethod
        def valueOf(p0: str) -> Any: ...
