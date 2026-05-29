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
    @staticmethod
    def getInstance() -> "RelativeDateTimeFormatter": ...
    @overload
    @staticmethod
    def getInstance(arg0: ULocale) -> "RelativeDateTimeFormatter": ...
    @overload
    @staticmethod
    def getInstance(arg0: Locale) -> "RelativeDateTimeFormatter": ...
    @overload
    @staticmethod
    def getInstance(arg0: ULocale, arg1: NumberFormat) -> "RelativeDateTimeFormatter": ...
    @overload
    @staticmethod
    def getInstance(arg0: ULocale, arg1: NumberFormat, arg2: "Style", arg3: DisplayContext) -> "RelativeDateTimeFormatter": ...
    @overload
    @staticmethod
    def getInstance(arg0: Locale, arg1: NumberFormat) -> "RelativeDateTimeFormatter": ...
    @overload
    def format(self, arg0: float, arg1: "Direction", arg2: "RelativeUnit") -> str: ...
    @overload
    def format(self, arg0: "Direction", arg1: "AbsoluteUnit") -> str: ...
    @overload
    def format(self, arg0: float, arg1: "RelativeDateTimeUnit") -> str: ...
    @overload
    def formatToValue(self, arg0: float, arg1: "Direction", arg2: "RelativeUnit") -> "FormattedRelativeDateTime": ...
    @overload
    def formatToValue(self, arg0: "Direction", arg1: "AbsoluteUnit") -> "FormattedRelativeDateTime": ...
    @overload
    def formatToValue(self, arg0: float, arg1: "RelativeDateTimeUnit") -> "FormattedRelativeDateTime": ...
    def formatNumeric(self, arg0: float, arg1: "RelativeDateTimeUnit") -> str: ...
    def formatNumericToValue(self, arg0: float, arg1: "RelativeDateTimeUnit") -> "FormattedRelativeDateTime": ...
    def combineDateAndTime(self, arg0: str, arg1: str) -> str: ...
    def getNumberFormat(self) -> NumberFormat: ...
    def getCapitalizationContext(self) -> DisplayContext: ...
    def getFormatStyle(self) -> "Style": ...

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
        @staticmethod
        def values() -> list["AbsoluteUnit"]: ...
        @staticmethod
        def valueOf(arg0: str) -> "AbsoluteUnit": ...

    class Direction:
        LAST_2: ClassVar["Direction"]
        LAST: ClassVar["Direction"]
        THIS: ClassVar["Direction"]
        NEXT: ClassVar["Direction"]
        NEXT_2: ClassVar["Direction"]
        PLAIN: ClassVar["Direction"]
        @staticmethod
        def values() -> list["Direction"]: ...
        @staticmethod
        def valueOf(arg0: str) -> "Direction": ...

    class FormattedRelativeDateTime:
        def toString(self) -> str: ...
        def length(self) -> int: ...
        def charAt(self, arg0: int) -> str: ...
        def subSequence(self, arg0: int, arg1: int) -> str: ...
        def appendTo(self, arg0: Appendable) -> Appendable: ...
        def nextPosition(self, arg0: ConstrainedFieldPosition) -> bool: ...
        def toCharacterIterator(self) -> AttributedCharacterIterator: ...

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
        @staticmethod
        def values() -> list["RelativeDateTimeUnit"]: ...
        @staticmethod
        def valueOf(arg0: str) -> "RelativeDateTimeUnit": ...

    class RelativeUnit:
        SECONDS: ClassVar["RelativeUnit"]
        MINUTES: ClassVar["RelativeUnit"]
        HOURS: ClassVar["RelativeUnit"]
        DAYS: ClassVar["RelativeUnit"]
        WEEKS: ClassVar["RelativeUnit"]
        MONTHS: ClassVar["RelativeUnit"]
        YEARS: ClassVar["RelativeUnit"]
        @staticmethod
        def values() -> list["RelativeUnit"]: ...
        @staticmethod
        def valueOf(arg0: str) -> "RelativeUnit": ...

    class Style:
        LONG: ClassVar["Style"]
        SHORT: ClassVar["Style"]
        NARROW: ClassVar["Style"]
        @staticmethod
        def values() -> list["Style"]: ...
        @staticmethod
        def valueOf(arg0: str) -> "Style": ...
