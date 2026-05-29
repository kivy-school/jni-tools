from typing import Any, ClassVar, overload
from android.icu.text.TimeZoneNames import TimeZoneNames
from android.icu.util.Output import Output
from android.icu.util.TimeZone import TimeZone
from android.icu.util.ULocale import ULocale
from java.lang.StringBuffer import StringBuffer
from java.text.AttributedCharacterIterator import AttributedCharacterIterator
from java.text.FieldPosition import FieldPosition
from java.text.ParsePosition import ParsePosition
from java.util.EnumSet import EnumSet
from java.util.Locale import Locale

class TimeZoneFormat:
    def parseObject(self, p0: str, p1: ParsePosition) -> Any: ...
    @overload
    def cloneAsThawed(self) -> Any: ...
    @overload
    def cloneAsThawed(self) -> "TimeZoneFormat": ...
    def setGMTPattern(self, p0: str) -> "TimeZoneFormat": ...
    def setGMTOffsetDigits(self, p0: str) -> "TimeZoneFormat": ...
    def setGMTZeroFormat(self, p0: str) -> "TimeZoneFormat": ...
    def getGMTOffsetDigits(self) -> str: ...
    def parseOffsetISO8601(self, p0: str, p1: ParsePosition) -> int: ...
    def getGMTPattern(self) -> str: ...
    def getTimeZoneNames(self) -> TimeZoneNames: ...
    def getGMTZeroFormat(self) -> str: ...
    def setTimeZoneNames(self, p0: TimeZoneNames) -> "TimeZoneFormat": ...
    def formatOffsetISO8601Basic(self, p0: int, p1: bool, p2: bool, p3: bool) -> str: ...
    def formatOffsetISO8601Extended(self, p0: int, p1: bool, p2: bool, p3: bool) -> str: ...
    def formatOffsetLocalizedGMT(self, p0: int) -> str: ...
    def formatOffsetShortLocalizedGMT(self, p0: int) -> str: ...
    def getDefaultParseOptions(self) -> EnumSet: ...
    def getGMTOffsetPattern(self, p0: Any) -> str: ...
    def parseOffsetLocalizedGMT(self, p0: str, p1: ParsePosition) -> int: ...
    def parseOffsetShortLocalizedGMT(self, p0: str, p1: ParsePosition) -> int: ...
    def setDefaultParseOptions(self, p0: EnumSet) -> "TimeZoneFormat": ...
    def setGMTOffsetPattern(self, p0: Any, p1: str) -> "TimeZoneFormat": ...
    @overload
    def format(self, p0: Any, p1: TimeZone, p2: int) -> str: ...
    @overload
    def format(self, p0: Any, p1: TimeZone, p2: int, p3: Output) -> str: ...
    @overload
    def format(self, p0: Any, p1: StringBuffer, p2: FieldPosition) -> StringBuffer: ...
    @overload
    @staticmethod
    def getInstance(p0: Locale) -> "TimeZoneFormat": ...
    @overload
    @staticmethod
    def getInstance(p0: ULocale) -> "TimeZoneFormat": ...
    @overload
    def parse(self, p0: Any, p1: str, p2: ParsePosition, p3: Output) -> TimeZone: ...
    @overload
    def parse(self, p0: Any, p1: str, p2: ParsePosition, p3: EnumSet, p4: Output) -> TimeZone: ...
    @overload
    def parse(self, p0: str) -> TimeZone: ...
    @overload
    def parse(self, p0: str, p1: ParsePosition) -> TimeZone: ...
    def isFrozen(self) -> bool: ...
    def formatToCharacterIterator(self, p0: Any) -> AttributedCharacterIterator: ...
    @overload
    def freeze(self) -> Any: ...
    @overload
    def freeze(self) -> "TimeZoneFormat": ...

    class TimeType:
        DAYLIGHT: ClassVar["TimeType"]
        STANDARD: ClassVar["TimeType"]
        UNKNOWN: ClassVar["TimeType"]
        DAYLIGHT: ClassVar[Any]
        STANDARD: ClassVar[Any]
        UNKNOWN: ClassVar[Any]
        @staticmethod
        def values() -> Any: ...
        @staticmethod
        def valueOf(p0: str) -> Any: ...

    class Style:
        EXEMPLAR_LOCATION: ClassVar["Style"]
        GENERIC_LOCATION: ClassVar["Style"]
        GENERIC_LONG: ClassVar["Style"]
        GENERIC_SHORT: ClassVar["Style"]
        ISO_BASIC_FIXED: ClassVar["Style"]
        ISO_BASIC_FULL: ClassVar["Style"]
        ISO_BASIC_LOCAL_FIXED: ClassVar["Style"]
        ISO_BASIC_LOCAL_FULL: ClassVar["Style"]
        ISO_BASIC_LOCAL_SHORT: ClassVar["Style"]
        ISO_BASIC_SHORT: ClassVar["Style"]
        ISO_EXTENDED_FIXED: ClassVar["Style"]
        ISO_EXTENDED_FULL: ClassVar["Style"]
        ISO_EXTENDED_LOCAL_FIXED: ClassVar["Style"]
        ISO_EXTENDED_LOCAL_FULL: ClassVar["Style"]
        LOCALIZED_GMT: ClassVar["Style"]
        LOCALIZED_GMT_SHORT: ClassVar["Style"]
        SPECIFIC_LONG: ClassVar["Style"]
        SPECIFIC_SHORT: ClassVar["Style"]
        ZONE_ID: ClassVar["Style"]
        ZONE_ID_SHORT: ClassVar["Style"]
        EXEMPLAR_LOCATION: ClassVar[Any]
        GENERIC_LOCATION: ClassVar[Any]
        GENERIC_LONG: ClassVar[Any]
        GENERIC_SHORT: ClassVar[Any]
        ISO_BASIC_FIXED: ClassVar[Any]
        ISO_BASIC_FULL: ClassVar[Any]
        ISO_BASIC_LOCAL_FIXED: ClassVar[Any]
        ISO_BASIC_LOCAL_FULL: ClassVar[Any]
        ISO_BASIC_LOCAL_SHORT: ClassVar[Any]
        ISO_BASIC_SHORT: ClassVar[Any]
        ISO_EXTENDED_FIXED: ClassVar[Any]
        ISO_EXTENDED_FULL: ClassVar[Any]
        ISO_EXTENDED_LOCAL_FIXED: ClassVar[Any]
        ISO_EXTENDED_LOCAL_FULL: ClassVar[Any]
        LOCALIZED_GMT: ClassVar[Any]
        LOCALIZED_GMT_SHORT: ClassVar[Any]
        SPECIFIC_LONG: ClassVar[Any]
        SPECIFIC_SHORT: ClassVar[Any]
        ZONE_ID: ClassVar[Any]
        ZONE_ID_SHORT: ClassVar[Any]
        @staticmethod
        def values() -> Any: ...
        @staticmethod
        def valueOf(p0: str) -> Any: ...

    class ParseOption:
        ALL_STYLES: ClassVar["ParseOption"]
        TZ_DATABASE_ABBREVIATIONS: ClassVar["ParseOption"]
        ALL_STYLES: ClassVar[Any]
        TZ_DATABASE_ABBREVIATIONS: ClassVar[Any]
        @staticmethod
        def values() -> Any: ...
        @staticmethod
        def valueOf(p0: str) -> Any: ...

    class GMTOffsetPatternType:
        NEGATIVE_H: ClassVar["GMTOffsetPatternType"]
        NEGATIVE_HM: ClassVar["GMTOffsetPatternType"]
        NEGATIVE_HMS: ClassVar["GMTOffsetPatternType"]
        POSITIVE_H: ClassVar["GMTOffsetPatternType"]
        POSITIVE_HM: ClassVar["GMTOffsetPatternType"]
        POSITIVE_HMS: ClassVar["GMTOffsetPatternType"]
        NEGATIVE_H: ClassVar[Any]
        NEGATIVE_HM: ClassVar[Any]
        NEGATIVE_HMS: ClassVar[Any]
        POSITIVE_H: ClassVar[Any]
        POSITIVE_HM: ClassVar[Any]
        POSITIVE_HMS: ClassVar[Any]
        @staticmethod
        def values() -> Any: ...
        @staticmethod
        def valueOf(p0: str) -> Any: ...
