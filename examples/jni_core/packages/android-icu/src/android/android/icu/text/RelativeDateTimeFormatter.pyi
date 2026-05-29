from typing import Any, ClassVar, overload
from android.icu.text.ConstrainedFieldPosition import ConstrainedFieldPosition
from android.icu.text.DisplayContext import DisplayContext
from android.icu.text.NumberFormat import NumberFormat
from android.icu.util.ULocale import ULocale
from java.lang.Appendable import Appendable
from java.text.AttributedCharacterIterator import AttributedCharacterIterator
from java.util.Locale import Locale

class RelativeDateTimeFormatter:
    @overload
    def formatToValue(self, p0: float, p1: Any, p2: Any) -> Any: ...
    @overload
    def formatToValue(self, p0: float, p1: Any) -> Any: ...
    @overload
    def formatToValue(self, p0: Any, p1: Any) -> Any: ...
    def getCapitalizationContext(self) -> DisplayContext: ...
    def formatNumericToValue(self, p0: float, p1: Any) -> Any: ...
    def formatNumeric(self, p0: float, p1: Any) -> str: ...
    def combineDateAndTime(self, p0: str, p1: str) -> str: ...
    def getFormatStyle(self) -> Any: ...
    def getNumberFormat(self) -> NumberFormat: ...
    @overload
    def format(self, p0: float, p1: Any, p2: Any) -> str: ...
    @overload
    def format(self, p0: float, p1: Any) -> str: ...
    @overload
    def format(self, p0: Any, p1: Any) -> str: ...
    @overload
    @staticmethod
    def getInstance(p0: ULocale, p1: NumberFormat, p2: Any, p3: DisplayContext) -> "RelativeDateTimeFormatter": ...
    @overload
    @staticmethod
    def getInstance() -> "RelativeDateTimeFormatter": ...
    @overload
    @staticmethod
    def getInstance(p0: Locale, p1: NumberFormat) -> "RelativeDateTimeFormatter": ...
    @overload
    @staticmethod
    def getInstance(p0: ULocale) -> "RelativeDateTimeFormatter": ...
    @overload
    @staticmethod
    def getInstance(p0: Locale) -> "RelativeDateTimeFormatter": ...
    @overload
    @staticmethod
    def getInstance(p0: ULocale, p1: NumberFormat) -> "RelativeDateTimeFormatter": ...

    class Style:
        LONG: ClassVar["Style"]
        SHORT: ClassVar["Style"]
        NARROW: ClassVar["Style"]
        LONG: ClassVar[Any]
        SHORT: ClassVar[Any]
        NARROW: ClassVar[Any]
        @staticmethod
        def values() -> Any: ...
        @staticmethod
        def valueOf(p0: str) -> Any: ...

    class RelativeUnit:
        SECONDS: ClassVar["RelativeUnit"]
        MINUTES: ClassVar["RelativeUnit"]
        HOURS: ClassVar["RelativeUnit"]
        DAYS: ClassVar["RelativeUnit"]
        WEEKS: ClassVar["RelativeUnit"]
        MONTHS: ClassVar["RelativeUnit"]
        YEARS: ClassVar["RelativeUnit"]
        SECONDS: ClassVar[Any]
        MINUTES: ClassVar[Any]
        HOURS: ClassVar[Any]
        DAYS: ClassVar[Any]
        WEEKS: ClassVar[Any]
        MONTHS: ClassVar[Any]
        YEARS: ClassVar[Any]
        @staticmethod
        def values() -> Any: ...
        @staticmethod
        def valueOf(p0: str) -> Any: ...

    class RelativeDateTimeUnit:
        YEAR: ClassVar["RelativeDateTimeUnit"]
        QUARTER: ClassVar["RelativeDateTimeUnit"]
        MONTH: ClassVar["RelativeDateTimeUnit"]
        WEEK: ClassVar["RelativeDateTimeUnit"]
        DAY: ClassVar["RelativeDateTimeUnit"]
        HOUR: ClassVar["RelativeDateTimeUnit"]
        MINUTE: ClassVar["RelativeDateTimeUnit"]
        SECOND: ClassVar["RelativeDateTimeUnit"]
        SUNDAY: ClassVar["RelativeDateTimeUnit"]
        MONDAY: ClassVar["RelativeDateTimeUnit"]
        TUESDAY: ClassVar["RelativeDateTimeUnit"]
        WEDNESDAY: ClassVar["RelativeDateTimeUnit"]
        THURSDAY: ClassVar["RelativeDateTimeUnit"]
        FRIDAY: ClassVar["RelativeDateTimeUnit"]
        SATURDAY: ClassVar["RelativeDateTimeUnit"]
        YEAR: ClassVar[Any]
        QUARTER: ClassVar[Any]
        MONTH: ClassVar[Any]
        WEEK: ClassVar[Any]
        DAY: ClassVar[Any]
        HOUR: ClassVar[Any]
        MINUTE: ClassVar[Any]
        SECOND: ClassVar[Any]
        SUNDAY: ClassVar[Any]
        MONDAY: ClassVar[Any]
        TUESDAY: ClassVar[Any]
        WEDNESDAY: ClassVar[Any]
        THURSDAY: ClassVar[Any]
        FRIDAY: ClassVar[Any]
        SATURDAY: ClassVar[Any]
        @staticmethod
        def values() -> Any: ...
        @staticmethod
        def valueOf(p0: str) -> Any: ...

    class FormattedRelativeDateTime:
        def nextPosition(self, p0: ConstrainedFieldPosition) -> bool: ...
        def toCharacterIterator(self) -> AttributedCharacterIterator: ...
        def length(self) -> int: ...
        def toString(self) -> str: ...
        def charAt(self, p0: int) -> str: ...
        def subSequence(self, p0: int, p1: int) -> str: ...
        def appendTo(self, p0: Appendable) -> Appendable: ...

    class Direction:
        LAST_2: ClassVar["Direction"]
        LAST: ClassVar["Direction"]
        THIS: ClassVar["Direction"]
        NEXT: ClassVar["Direction"]
        NEXT_2: ClassVar["Direction"]
        PLAIN: ClassVar["Direction"]
        LAST_2: ClassVar[Any]
        LAST: ClassVar[Any]
        THIS: ClassVar[Any]
        NEXT: ClassVar[Any]
        NEXT_2: ClassVar[Any]
        PLAIN: ClassVar[Any]
        @staticmethod
        def values() -> Any: ...
        @staticmethod
        def valueOf(p0: str) -> Any: ...

    class AbsoluteUnit:
        SUNDAY: ClassVar["AbsoluteUnit"]
        MONDAY: ClassVar["AbsoluteUnit"]
        TUESDAY: ClassVar["AbsoluteUnit"]
        WEDNESDAY: ClassVar["AbsoluteUnit"]
        THURSDAY: ClassVar["AbsoluteUnit"]
        FRIDAY: ClassVar["AbsoluteUnit"]
        SATURDAY: ClassVar["AbsoluteUnit"]
        DAY: ClassVar["AbsoluteUnit"]
        WEEK: ClassVar["AbsoluteUnit"]
        MONTH: ClassVar["AbsoluteUnit"]
        YEAR: ClassVar["AbsoluteUnit"]
        NOW: ClassVar["AbsoluteUnit"]
        QUARTER: ClassVar["AbsoluteUnit"]
        HOUR: ClassVar["AbsoluteUnit"]
        MINUTE: ClassVar["AbsoluteUnit"]
        SUNDAY: ClassVar[Any]
        MONDAY: ClassVar[Any]
        TUESDAY: ClassVar[Any]
        WEDNESDAY: ClassVar[Any]
        THURSDAY: ClassVar[Any]
        FRIDAY: ClassVar[Any]
        SATURDAY: ClassVar[Any]
        DAY: ClassVar[Any]
        WEEK: ClassVar[Any]
        MONTH: ClassVar[Any]
        YEAR: ClassVar[Any]
        NOW: ClassVar[Any]
        QUARTER: ClassVar[Any]
        HOUR: ClassVar[Any]
        MINUTE: ClassVar[Any]
        @staticmethod
        def values() -> Any: ...
        @staticmethod
        def valueOf(p0: str) -> Any: ...
