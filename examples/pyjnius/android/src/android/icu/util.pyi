from typing import Any, ClassVar, overload
from android.icu.util.TimeUnit import TimeUnit

class MeasureUnit:
    ACRE: ClassVar["MeasureUnit"]
    ACRE_FOOT: ClassVar["MeasureUnit"]
    AMPERE: ClassVar["MeasureUnit"]
    ARC_MINUTE: ClassVar["MeasureUnit"]
    ARC_SECOND: ClassVar["MeasureUnit"]
    ASTRONOMICAL_UNIT: ClassVar["MeasureUnit"]
    ATMOSPHERE: ClassVar["MeasureUnit"]
    BEAUFORT: ClassVar["MeasureUnit"]
    BIT: ClassVar["MeasureUnit"]
    BUSHEL: ClassVar["MeasureUnit"]
    BYTE: ClassVar["MeasureUnit"]
    CALORIE: ClassVar["MeasureUnit"]
    CANDELA: ClassVar["MeasureUnit"]
    CARAT: ClassVar["MeasureUnit"]
    CELSIUS: ClassVar["MeasureUnit"]
    CENTILITER: ClassVar["MeasureUnit"]
    CENTIMETER: ClassVar["MeasureUnit"]
    CENTURY: ClassVar["MeasureUnit"]
    CUBIC_CENTIMETER: ClassVar["MeasureUnit"]
    CUBIC_FOOT: ClassVar["MeasureUnit"]
    CUBIC_INCH: ClassVar["MeasureUnit"]
    CUBIC_KILOMETER: ClassVar["MeasureUnit"]
    CUBIC_METER: ClassVar["MeasureUnit"]
    CUBIC_MILE: ClassVar["MeasureUnit"]
    CUBIC_YARD: ClassVar["MeasureUnit"]
    CUP: ClassVar["MeasureUnit"]
    CUP_METRIC: ClassVar["MeasureUnit"]
    DAY: ClassVar[TimeUnit]
    DECADE: ClassVar["MeasureUnit"]
    DECILITER: ClassVar["MeasureUnit"]
    DECIMETER: ClassVar["MeasureUnit"]
    DEGREE: ClassVar["MeasureUnit"]
    DOT: ClassVar["MeasureUnit"]
    DOT_PER_CENTIMETER: ClassVar["MeasureUnit"]
    DOT_PER_INCH: ClassVar["MeasureUnit"]
    EM: ClassVar["MeasureUnit"]
    FAHRENHEIT: ClassVar["MeasureUnit"]
    FATHOM: ClassVar["MeasureUnit"]
    FLUID_OUNCE: ClassVar["MeasureUnit"]
    FOODCALORIE: ClassVar["MeasureUnit"]
    FOOT: ClassVar["MeasureUnit"]
    FURLONG: ClassVar["MeasureUnit"]
    GALLON: ClassVar["MeasureUnit"]
    GALLON_IMPERIAL: ClassVar["MeasureUnit"]
    GASOLINE_ENERGY_DENSITY: ClassVar["MeasureUnit"]
    GENERIC_TEMPERATURE: ClassVar["MeasureUnit"]
    GIGABIT: ClassVar["MeasureUnit"]
    GIGABYTE: ClassVar["MeasureUnit"]
    GIGAHERTZ: ClassVar["MeasureUnit"]
    GIGAWATT: ClassVar["MeasureUnit"]
    GRAM: ClassVar["MeasureUnit"]
    G_FORCE: ClassVar["MeasureUnit"]
    HECTARE: ClassVar["MeasureUnit"]
    HECTOLITER: ClassVar["MeasureUnit"]
    HECTOPASCAL: ClassVar["MeasureUnit"]
    HERTZ: ClassVar["MeasureUnit"]
    HORSEPOWER: ClassVar["MeasureUnit"]
    HOUR: ClassVar[TimeUnit]
    INCH: ClassVar["MeasureUnit"]
    INCH_HG: ClassVar["MeasureUnit"]
    ITEM: ClassVar["MeasureUnit"]
    JOULE: ClassVar["MeasureUnit"]
    KARAT: ClassVar["MeasureUnit"]
    KELVIN: ClassVar["MeasureUnit"]
    KILOBIT: ClassVar["MeasureUnit"]
    KILOBYTE: ClassVar["MeasureUnit"]
    KILOCALORIE: ClassVar["MeasureUnit"]
    KILOGRAM: ClassVar["MeasureUnit"]
    KILOHERTZ: ClassVar["MeasureUnit"]
    KILOJOULE: ClassVar["MeasureUnit"]
    KILOMETER: ClassVar["MeasureUnit"]
    KILOMETER_PER_HOUR: ClassVar["MeasureUnit"]
    KILOWATT: ClassVar["MeasureUnit"]
    KILOWATT_HOUR: ClassVar["MeasureUnit"]
    KILOWATT_HOUR_PER_100_KILOMETER: ClassVar["MeasureUnit"]
    KNOT: ClassVar["MeasureUnit"]
    LIGHT_YEAR: ClassVar["MeasureUnit"]
    LITER: ClassVar["MeasureUnit"]
    LITER_PER_100KILOMETERS: ClassVar["MeasureUnit"]
    LITER_PER_KILOMETER: ClassVar["MeasureUnit"]
    LUMEN: ClassVar["MeasureUnit"]
    LUX: ClassVar["MeasureUnit"]
    MEGABIT: ClassVar["MeasureUnit"]
    MEGABYTE: ClassVar["MeasureUnit"]
    MEGAHERTZ: ClassVar["MeasureUnit"]
    MEGALITER: ClassVar["MeasureUnit"]
    MEGAPIXEL: ClassVar["MeasureUnit"]
    MEGAWATT: ClassVar["MeasureUnit"]
    METER: ClassVar["MeasureUnit"]
    METER_PER_SECOND: ClassVar["MeasureUnit"]
    METER_PER_SECOND_SQUARED: ClassVar["MeasureUnit"]
    METRIC_TON: ClassVar["MeasureUnit"]
    MICROGRAM: ClassVar["MeasureUnit"]
    MICROMETER: ClassVar["MeasureUnit"]
    MICROSECOND: ClassVar["MeasureUnit"]
    MILE: ClassVar["MeasureUnit"]
    MILE_PER_GALLON: ClassVar["MeasureUnit"]
    MILE_PER_GALLON_IMPERIAL: ClassVar["MeasureUnit"]
    MILE_PER_HOUR: ClassVar["MeasureUnit"]
    MILE_SCANDINAVIAN: ClassVar["MeasureUnit"]
    MILLIAMPERE: ClassVar["MeasureUnit"]
    MILLIBAR: ClassVar["MeasureUnit"]
    MILLIGRAM: ClassVar["MeasureUnit"]
    MILLIGRAM_OFGLUCOSE_PER_DECILITER: ClassVar["MeasureUnit"]
    MILLIGRAM_PER_DECILITER: ClassVar["MeasureUnit"]
    MILLILITER: ClassVar["MeasureUnit"]
    MILLIMETER: ClassVar["MeasureUnit"]
    MILLIMETER_OF_MERCURY: ClassVar["MeasureUnit"]
    MILLIMOLE_PER_LITER: ClassVar["MeasureUnit"]
    MILLISECOND: ClassVar["MeasureUnit"]
    MILLIWATT: ClassVar["MeasureUnit"]
    MINUTE: ClassVar[TimeUnit]
    MONTH: ClassVar[TimeUnit]
    NANOMETER: ClassVar["MeasureUnit"]
    NANOSECOND: ClassVar["MeasureUnit"]
    NAUTICAL_MILE: ClassVar["MeasureUnit"]
    OHM: ClassVar["MeasureUnit"]
    OUNCE: ClassVar["MeasureUnit"]
    OUNCE_TROY: ClassVar["MeasureUnit"]
    PARSEC: ClassVar["MeasureUnit"]
    PART_PER_MILLION: ClassVar["MeasureUnit"]
    PERCENT: ClassVar["MeasureUnit"]
    PERMILLE: ClassVar["MeasureUnit"]
    PETABYTE: ClassVar["MeasureUnit"]
    PICOMETER: ClassVar["MeasureUnit"]
    PINT: ClassVar["MeasureUnit"]
    PINT_METRIC: ClassVar["MeasureUnit"]
    PIXEL: ClassVar["MeasureUnit"]
    PIXEL_PER_CENTIMETER: ClassVar["MeasureUnit"]
    PIXEL_PER_INCH: ClassVar["MeasureUnit"]
    POINT: ClassVar["MeasureUnit"]
    POUND: ClassVar["MeasureUnit"]
    POUND_PER_SQUARE_INCH: ClassVar["MeasureUnit"]
    QUART: ClassVar["MeasureUnit"]
    QUARTER: ClassVar["MeasureUnit"]
    RADIAN: ClassVar["MeasureUnit"]
    REVOLUTION_ANGLE: ClassVar["MeasureUnit"]
    SECOND: ClassVar[TimeUnit]
    SQUARE_CENTIMETER: ClassVar["MeasureUnit"]
    SQUARE_FOOT: ClassVar["MeasureUnit"]
    SQUARE_INCH: ClassVar["MeasureUnit"]
    SQUARE_KILOMETER: ClassVar["MeasureUnit"]
    SQUARE_METER: ClassVar["MeasureUnit"]
    SQUARE_MILE: ClassVar["MeasureUnit"]
    SQUARE_YARD: ClassVar["MeasureUnit"]
    STONE: ClassVar["MeasureUnit"]
    TABLESPOON: ClassVar["MeasureUnit"]
    TEASPOON: ClassVar["MeasureUnit"]
    TERABIT: ClassVar["MeasureUnit"]
    TERABYTE: ClassVar["MeasureUnit"]
    TON: ClassVar["MeasureUnit"]
    TONNE: ClassVar["MeasureUnit"]
    VOLT: ClassVar["MeasureUnit"]
    WATT: ClassVar["MeasureUnit"]
    WEEK: ClassVar[TimeUnit]
    YARD: ClassVar["MeasureUnit"]
    YEAR: ClassVar[TimeUnit]
    def getSubtype(self) -> str: ...
    @staticmethod
    def forIdentifier(p0: str) -> "MeasureUnit": ...
    @overload
    @staticmethod
    def getAvailable() -> set: ...
    @overload
    @staticmethod
    def getAvailable(p0: str) -> set: ...
    @staticmethod
    def getAvailableTypes() -> set: ...
    def getComplexity(self) -> Any: ...
    def getDimensionality(self) -> int: ...
    def reciprocal(self) -> "MeasureUnit": ...
    def splitToSingleUnits(self) -> list: ...
    def withDimensionality(self, p0: int) -> "MeasureUnit": ...
    def product(self, p0: "MeasureUnit") -> "MeasureUnit": ...
    def equals(self, p0: Any) -> bool: ...
    def toString(self) -> str: ...
    def hashCode(self) -> int: ...
    def getType(self) -> str: ...
    def getIdentifier(self) -> str: ...
    def getPrefix(self) -> Any: ...
    def withPrefix(self, p0: Any) -> "MeasureUnit": ...

    class MeasurePrefix:
        ATTO: ClassVar["MeasurePrefix"]
        CENTI: ClassVar["MeasurePrefix"]
        DECI: ClassVar["MeasurePrefix"]
        DEKA: ClassVar["MeasurePrefix"]
        EXA: ClassVar["MeasurePrefix"]
        EXBI: ClassVar["MeasurePrefix"]
        FEMTO: ClassVar["MeasurePrefix"]
        GIBI: ClassVar["MeasurePrefix"]
        GIGA: ClassVar["MeasurePrefix"]
        HECTO: ClassVar["MeasurePrefix"]
        KIBI: ClassVar["MeasurePrefix"]
        KILO: ClassVar["MeasurePrefix"]
        MEBI: ClassVar["MeasurePrefix"]
        MEGA: ClassVar["MeasurePrefix"]
        MICRO: ClassVar["MeasurePrefix"]
        MILLI: ClassVar["MeasurePrefix"]
        NANO: ClassVar["MeasurePrefix"]
        ONE: ClassVar["MeasurePrefix"]
        PEBI: ClassVar["MeasurePrefix"]
        PETA: ClassVar["MeasurePrefix"]
        PICO: ClassVar["MeasurePrefix"]
        TEBI: ClassVar["MeasurePrefix"]
        TERA: ClassVar["MeasurePrefix"]
        YOBI: ClassVar["MeasurePrefix"]
        YOCTO: ClassVar["MeasurePrefix"]
        YOTTA: ClassVar["MeasurePrefix"]
        ZEBI: ClassVar["MeasurePrefix"]
        ZEPTO: ClassVar["MeasurePrefix"]
        ZETTA: ClassVar["MeasurePrefix"]
        ATTO: ClassVar[Any]
        CENTI: ClassVar[Any]
        DECI: ClassVar[Any]
        DEKA: ClassVar[Any]
        EXA: ClassVar[Any]
        EXBI: ClassVar[Any]
        FEMTO: ClassVar[Any]
        GIBI: ClassVar[Any]
        GIGA: ClassVar[Any]
        HECTO: ClassVar[Any]
        KIBI: ClassVar[Any]
        KILO: ClassVar[Any]
        MEBI: ClassVar[Any]
        MEGA: ClassVar[Any]
        MICRO: ClassVar[Any]
        MILLI: ClassVar[Any]
        NANO: ClassVar[Any]
        ONE: ClassVar[Any]
        PEBI: ClassVar[Any]
        PETA: ClassVar[Any]
        PICO: ClassVar[Any]
        TEBI: ClassVar[Any]
        TERA: ClassVar[Any]
        YOBI: ClassVar[Any]
        YOCTO: ClassVar[Any]
        YOTTA: ClassVar[Any]
        ZEBI: ClassVar[Any]
        ZEPTO: ClassVar[Any]
        ZETTA: ClassVar[Any]
        @staticmethod
        def values() -> Any: ...
        @staticmethod
        def valueOf(p0: str) -> Any: ...
        def getBase(self) -> int: ...
        def getPower(self) -> int: ...

    class Complexity:
        COMPOUND: ClassVar["Complexity"]
        MIXED: ClassVar["Complexity"]
        SINGLE: ClassVar["Complexity"]
        COMPOUND: ClassVar[Any]
        MIXED: ClassVar[Any]
        SINGLE: ClassVar[Any]
        @staticmethod
        def values() -> Any: ...
        @staticmethod
        def valueOf(p0: str) -> Any: ...

from typing import Any, ClassVar, overload

class Output:
    value: Any
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, p0: Any) -> None: ...
    def toString(self) -> str: ...

from typing import Any, ClassVar, overload
from android.icu.util.TimeZone import TimeZone
from android.icu.util.ULocale import ULocale
from java.util.Date import Date
from java.util.Locale import Locale

class JapaneseCalendar:
    HEISEI: ClassVar[int]
    MEIJI: ClassVar[int]
    REIWA: ClassVar[int]
    SHOWA: ClassVar[int]
    TAISHO: ClassVar[int]
    AD: ClassVar[int]
    BC: ClassVar[int]
    AM: ClassVar[int]
    AM_PM: ClassVar[int]
    APRIL: ClassVar[int]
    AUGUST: ClassVar[int]
    DATE: ClassVar[int]
    DAY_OF_MONTH: ClassVar[int]
    DAY_OF_WEEK: ClassVar[int]
    DAY_OF_WEEK_IN_MONTH: ClassVar[int]
    DAY_OF_YEAR: ClassVar[int]
    DECEMBER: ClassVar[int]
    DOW_LOCAL: ClassVar[int]
    DST_OFFSET: ClassVar[int]
    ERA: ClassVar[int]
    EXTENDED_YEAR: ClassVar[int]
    FEBRUARY: ClassVar[int]
    FRIDAY: ClassVar[int]
    HOUR: ClassVar[int]
    HOUR_OF_DAY: ClassVar[int]
    IS_LEAP_MONTH: ClassVar[int]
    JANUARY: ClassVar[int]
    JULIAN_DAY: ClassVar[int]
    JULY: ClassVar[int]
    JUNE: ClassVar[int]
    MARCH: ClassVar[int]
    MAY: ClassVar[int]
    MILLISECOND: ClassVar[int]
    MILLISECONDS_IN_DAY: ClassVar[int]
    MINUTE: ClassVar[int]
    MONDAY: ClassVar[int]
    MONTH: ClassVar[int]
    NOVEMBER: ClassVar[int]
    OCTOBER: ClassVar[int]
    ORDINAL_MONTH: ClassVar[int]
    PM: ClassVar[int]
    SATURDAY: ClassVar[int]
    SECOND: ClassVar[int]
    SEPTEMBER: ClassVar[int]
    SUNDAY: ClassVar[int]
    THURSDAY: ClassVar[int]
    TUESDAY: ClassVar[int]
    UNDECIMBER: ClassVar[int]
    WALLTIME_FIRST: ClassVar[int]
    WALLTIME_LAST: ClassVar[int]
    WALLTIME_NEXT_VALID: ClassVar[int]
    WEDNESDAY: ClassVar[int]
    WEEK_OF_MONTH: ClassVar[int]
    WEEK_OF_YEAR: ClassVar[int]
    YEAR: ClassVar[int]
    YEAR_WOY: ClassVar[int]
    ZONE_OFFSET: ClassVar[int]
    @overload
    def __init__(self, p0: int, p1: int, p2: int, p3: int) -> None: ...
    @overload
    def __init__(self, p0: int, p1: int, p2: int, p3: int, p4: int, p5: int) -> None: ...
    @overload
    def __init__(self, p0: Date) -> None: ...
    @overload
    def __init__(self, p0: Locale) -> None: ...
    @overload
    def __init__(self, p0: TimeZone, p1: ULocale) -> None: ...
    @overload
    def __init__(self, p0: TimeZone) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, p0: TimeZone, p1: Locale) -> None: ...
    @overload
    def __init__(self, p0: ULocale) -> None: ...
    @overload
    def __init__(self, p0: int, p1: int, p2: int) -> None: ...
    def getType(self) -> str: ...
    def getActualMaximum(self, p0: int) -> int: ...

from typing import Any, ClassVar, overload
from java.lang.Throwable import Throwable

class ICUUncheckedIOException:
    @overload
    def __init__(self, p0: Throwable) -> None: ...
    @overload
    def __init__(self, p0: str, p1: Throwable) -> None: ...
    @overload
    def __init__(self, p0: str) -> None: ...
    @overload
    def __init__(self) -> None: ...

from typing import Any, ClassVar, overload

class ValueIterator:
    def setRange(self, p0: int, p1: int) -> None: ...
    def reset(self) -> None: ...
    def next(self, p0: Any) -> bool: ...

    class Element:
        integer: int
        value: Any
        def __init__(self) -> None: ...

from typing import Any, ClassVar, overload
from android.icu.util.MeasureUnit import MeasureUnit

class Measure:
    def __init__(self, p0: float, p1: MeasureUnit) -> None: ...
    def getUnit(self) -> MeasureUnit: ...
    def equals(self, p0: Any) -> bool: ...
    def toString(self) -> str: ...
    def hashCode(self) -> int: ...
    def getNumber(self) -> float: ...

from typing import Any, ClassVar, overload
from android.icu.math.BigDecimal import BigDecimal

class UniversalTimeScale:
    DB2_TIME: ClassVar[int]
    DOTNET_DATE_TIME: ClassVar[int]
    EPOCH_OFFSET_PLUS_1_VALUE: ClassVar[int]
    EPOCH_OFFSET_VALUE: ClassVar[int]
    EXCEL_TIME: ClassVar[int]
    FROM_MAX_VALUE: ClassVar[int]
    FROM_MIN_VALUE: ClassVar[int]
    ICU4C_TIME: ClassVar[int]
    JAVA_TIME: ClassVar[int]
    MAC_OLD_TIME: ClassVar[int]
    MAC_TIME: ClassVar[int]
    MAX_SCALE: ClassVar[int]
    TO_MAX_VALUE: ClassVar[int]
    TO_MIN_VALUE: ClassVar[int]
    UNITS_VALUE: ClassVar[int]
    UNIX_MICROSECONDS_TIME: ClassVar[int]
    UNIX_TIME: ClassVar[int]
    WINDOWS_FILE_TIME: ClassVar[int]
    @overload
    @staticmethod
    def bigDecimalFrom(p0: float, p1: int) -> BigDecimal: ...
    @overload
    @staticmethod
    def bigDecimalFrom(p0: BigDecimal, p1: int) -> BigDecimal: ...
    @overload
    @staticmethod
    def bigDecimalFrom(p0: int, p1: int) -> BigDecimal: ...
    @staticmethod
    def getTimeScaleValue(p0: int, p1: int) -> int: ...
    @overload
    @staticmethod
    def toBigDecimal(p0: int, p1: int) -> BigDecimal: ...
    @overload
    @staticmethod
    def toBigDecimal(p0: BigDecimal, p1: int) -> BigDecimal: ...
    @staticmethod
    def toLong(p0: int, p1: int) -> int: ...
    @staticmethod
    def from_(p0: int, p1: int) -> int: ...

from typing import Any, ClassVar, overload

class VersionInfo:
    ICU_VERSION: ClassVar["VersionInfo"]
    UCOL_BUILDER_VERSION: ClassVar["VersionInfo"]
    UCOL_RUNTIME_VERSION: ClassVar["VersionInfo"]
    UNICODE_10_0: ClassVar["VersionInfo"]
    UNICODE_11_0: ClassVar["VersionInfo"]
    UNICODE_12_0: ClassVar["VersionInfo"]
    UNICODE_12_1: ClassVar["VersionInfo"]
    UNICODE_13_0: ClassVar["VersionInfo"]
    UNICODE_14_0: ClassVar["VersionInfo"]
    UNICODE_15_0: ClassVar["VersionInfo"]
    UNICODE_15_1: ClassVar["VersionInfo"]
    UNICODE_16_0: ClassVar["VersionInfo"]
    UNICODE_1_0: ClassVar["VersionInfo"]
    UNICODE_1_0_1: ClassVar["VersionInfo"]
    UNICODE_1_1_0: ClassVar["VersionInfo"]
    UNICODE_1_1_5: ClassVar["VersionInfo"]
    UNICODE_2_0: ClassVar["VersionInfo"]
    UNICODE_2_1_2: ClassVar["VersionInfo"]
    UNICODE_2_1_5: ClassVar["VersionInfo"]
    UNICODE_2_1_8: ClassVar["VersionInfo"]
    UNICODE_2_1_9: ClassVar["VersionInfo"]
    UNICODE_3_0: ClassVar["VersionInfo"]
    UNICODE_3_0_1: ClassVar["VersionInfo"]
    UNICODE_3_1_0: ClassVar["VersionInfo"]
    UNICODE_3_1_1: ClassVar["VersionInfo"]
    UNICODE_3_2: ClassVar["VersionInfo"]
    UNICODE_4_0: ClassVar["VersionInfo"]
    UNICODE_4_0_1: ClassVar["VersionInfo"]
    UNICODE_4_1: ClassVar["VersionInfo"]
    UNICODE_5_0: ClassVar["VersionInfo"]
    UNICODE_5_1: ClassVar["VersionInfo"]
    UNICODE_5_2: ClassVar["VersionInfo"]
    UNICODE_6_0: ClassVar["VersionInfo"]
    UNICODE_6_1: ClassVar["VersionInfo"]
    UNICODE_6_2: ClassVar["VersionInfo"]
    UNICODE_6_3: ClassVar["VersionInfo"]
    UNICODE_7_0: ClassVar["VersionInfo"]
    UNICODE_8_0: ClassVar["VersionInfo"]
    UNICODE_9_0: ClassVar["VersionInfo"]
    def getMicro(self) -> int: ...
    def getMilli(self) -> int: ...
    def equals(self, p0: Any) -> bool: ...
    def toString(self) -> str: ...
    def hashCode(self) -> int: ...
    @overload
    def compareTo(self, p0: Any) -> int: ...
    @overload
    def compareTo(self, p0: "VersionInfo") -> int: ...
    @overload
    @staticmethod
    def getInstance(p0: int, p1: int) -> "VersionInfo": ...
    @overload
    @staticmethod
    def getInstance(p0: int, p1: int, p2: int) -> "VersionInfo": ...
    @overload
    @staticmethod
    def getInstance(p0: int, p1: int, p2: int, p3: int) -> "VersionInfo": ...
    @overload
    @staticmethod
    def getInstance(p0: str) -> "VersionInfo": ...
    @overload
    @staticmethod
    def getInstance(p0: int) -> "VersionInfo": ...
    def getMajor(self) -> int: ...
    def getMinor(self) -> int: ...

from typing import Any, ClassVar, overload
from android.icu.util.ULocale import ULocale
from java.util.Date import Date
from java.util.Locale import Locale

class TimeZone:
    GENERIC_LOCATION: ClassVar[int]
    GMT_ZONE: ClassVar["TimeZone"]
    LONG: ClassVar[int]
    LONG_GENERIC: ClassVar[int]
    LONG_GMT: ClassVar[int]
    SHORT: ClassVar[int]
    SHORT_COMMONLY_USED: ClassVar[int]
    SHORT_GENERIC: ClassVar[int]
    SHORT_GMT: ClassVar[int]
    TIMEZONE_ICU: ClassVar[int]
    TIMEZONE_JDK: ClassVar[int]
    UNKNOWN_ZONE: ClassVar["TimeZone"]
    UNKNOWN_ZONE_ID: ClassVar[str]
    def __init__(self) -> None: ...
    @overload
    def cloneAsThawed(self) -> "TimeZone": ...
    @overload
    def cloneAsThawed(self) -> Any: ...
    @staticmethod
    def countEquivalentIDs(p0: str) -> int: ...
    @overload
    @staticmethod
    def getCanonicalID(p0: str) -> str: ...
    @overload
    @staticmethod
    def getCanonicalID(p0: str, p1: Any) -> str: ...
    @staticmethod
    def getEquivalentID(p0: str, p1: int) -> str: ...
    @staticmethod
    def getFrozenTimeZone(p0: str) -> "TimeZone": ...
    @staticmethod
    def getIDForWindowsID(p0: str, p1: str) -> str: ...
    @staticmethod
    def getIanaID(p0: str) -> str: ...
    @staticmethod
    def getTZDataVersion() -> str: ...
    @staticmethod
    def getWindowsID(p0: str) -> str: ...
    def inDaylightTime(self, p0: Date) -> bool: ...
    def getRawOffset(self) -> int: ...
    def getDSTSavings(self) -> int: ...
    def useDaylightTime(self) -> bool: ...
    @overload
    @staticmethod
    def getAvailableIDs(p0: int) -> Any: ...
    @overload
    @staticmethod
    def getAvailableIDs(p0: str) -> Any: ...
    @overload
    @staticmethod
    def getAvailableIDs() -> Any: ...
    @overload
    @staticmethod
    def getAvailableIDs(p0: Any, p1: str, p2: int) -> set: ...
    def setID(self, p0: str) -> None: ...
    def equals(self, p0: Any) -> bool: ...
    def hashCode(self) -> int: ...
    def clone(self) -> Any: ...
    @staticmethod
    def getDefault() -> "TimeZone": ...
    @overload
    def freeze(self) -> Any: ...
    @overload
    def freeze(self) -> "TimeZone": ...
    @overload
    def getOffset(self, p0: int, p1: int, p2: int, p3: int, p4: int, p5: int) -> int: ...
    @overload
    def getOffset(self, p0: int) -> int: ...
    @overload
    def getOffset(self, p0: int, p1: bool, p2: Any) -> None: ...
    def setRawOffset(self, p0: int) -> None: ...
    def observesDaylightTime(self) -> bool: ...
    def hasSameRules(self, p0: "TimeZone") -> bool: ...
    @overload
    @staticmethod
    def getTimeZone(p0: str) -> "TimeZone": ...
    @overload
    @staticmethod
    def getTimeZone(p0: str, p1: int) -> "TimeZone": ...
    @overload
    def getDisplayName(self, p0: bool, p1: int) -> str: ...
    @overload
    def getDisplayName(self, p0: bool, p1: int, p2: ULocale) -> str: ...
    @overload
    def getDisplayName(self, p0: bool, p1: int, p2: Locale) -> str: ...
    @overload
    def getDisplayName(self, p0: Locale) -> str: ...
    @overload
    def getDisplayName(self, p0: ULocale) -> str: ...
    @overload
    def getDisplayName(self) -> str: ...
    def isFrozen(self) -> bool: ...
    @staticmethod
    def getRegion(p0: str) -> str: ...
    def getID(self) -> str: ...

    class SystemTimeZoneType:
        ANY: ClassVar["SystemTimeZoneType"]
        CANONICAL: ClassVar["SystemTimeZoneType"]
        CANONICAL_LOCATION: ClassVar["SystemTimeZoneType"]
        ANY: ClassVar[Any]
        CANONICAL: ClassVar[Any]
        CANONICAL_LOCATION: ClassVar[Any]
        @staticmethod
        def values() -> Any: ...
        @staticmethod
        def valueOf(p0: str) -> Any: ...

from typing import Any, ClassVar, overload
from java.util.Iterator import Iterator
from java.util.Locale import Locale

class ULocale:
    CANADA: ClassVar["ULocale"]
    CANADA_FRENCH: ClassVar["ULocale"]
    CHINA: ClassVar["ULocale"]
    CHINESE: ClassVar["ULocale"]
    ENGLISH: ClassVar["ULocale"]
    FRANCE: ClassVar["ULocale"]
    FRENCH: ClassVar["ULocale"]
    GERMAN: ClassVar["ULocale"]
    GERMANY: ClassVar["ULocale"]
    ITALIAN: ClassVar["ULocale"]
    ITALY: ClassVar["ULocale"]
    JAPAN: ClassVar["ULocale"]
    JAPANESE: ClassVar["ULocale"]
    KOREA: ClassVar["ULocale"]
    KOREAN: ClassVar["ULocale"]
    PRC: ClassVar["ULocale"]
    PRIVATE_USE_EXTENSION: ClassVar[str]
    ROOT: ClassVar["ULocale"]
    SIMPLIFIED_CHINESE: ClassVar["ULocale"]
    TAIWAN: ClassVar["ULocale"]
    TRADITIONAL_CHINESE: ClassVar["ULocale"]
    UK: ClassVar["ULocale"]
    UNICODE_LOCALE_EXTENSION: ClassVar[str]
    US: ClassVar["ULocale"]
    @overload
    def __init__(self, p0: str) -> None: ...
    @overload
    def __init__(self, p0: str, p1: str, p2: str) -> None: ...
    @overload
    def __init__(self, p0: str, p1: str) -> None: ...
    @overload
    @staticmethod
    def acceptLanguage(p0: str, p1: Any, p2: Any) -> "ULocale": ...
    @overload
    @staticmethod
    def acceptLanguage(p0: Any, p1: Any) -> "ULocale": ...
    @overload
    @staticmethod
    def acceptLanguage(p0: str, p1: Any) -> "ULocale": ...
    @overload
    @staticmethod
    def acceptLanguage(p0: Any, p1: Any, p2: Any) -> "ULocale": ...
    @staticmethod
    def addLikelySubtags(p0: "ULocale") -> "ULocale": ...
    @overload
    @staticmethod
    def createCanonical(p0: "ULocale") -> "ULocale": ...
    @overload
    @staticmethod
    def createCanonical(p0: str) -> "ULocale": ...
    @staticmethod
    def forLocale(p0: Locale) -> "ULocale": ...
    @staticmethod
    def getAvailableLocalesByType(p0: Any) -> list: ...
    @overload
    def getBaseName(self) -> str: ...
    @overload
    @staticmethod
    def getBaseName(p0: str) -> str: ...
    def getCharacterOrientation(self) -> str: ...
    @overload
    @staticmethod
    def getDisplayKeyword(p0: str, p1: "ULocale") -> str: ...
    @overload
    @staticmethod
    def getDisplayKeyword(p0: str, p1: str) -> str: ...
    @overload
    @staticmethod
    def getDisplayKeyword(p0: str) -> str: ...
    @overload
    def getDisplayKeywordValue(self, p0: str) -> str: ...
    @overload
    @staticmethod
    def getDisplayKeywordValue(p0: str, p1: str, p2: "ULocale") -> str: ...
    @overload
    @staticmethod
    def getDisplayKeywordValue(p0: str, p1: str, p2: str) -> str: ...
    @overload
    def getDisplayKeywordValue(self, p0: str, p1: "ULocale") -> str: ...
    @overload
    @staticmethod
    def getDisplayLanguageWithDialect(p0: str, p1: str) -> str: ...
    @overload
    @staticmethod
    def getDisplayLanguageWithDialect(p0: str, p1: "ULocale") -> str: ...
    @overload
    def getDisplayLanguageWithDialect(self, p0: "ULocale") -> str: ...
    @overload
    def getDisplayLanguageWithDialect(self) -> str: ...
    @overload
    def getDisplayNameWithDialect(self, p0: "ULocale") -> str: ...
    @overload
    @staticmethod
    def getDisplayNameWithDialect(p0: str, p1: str) -> str: ...
    @overload
    def getDisplayNameWithDialect(self) -> str: ...
    @overload
    @staticmethod
    def getDisplayNameWithDialect(p0: str, p1: "ULocale") -> str: ...
    @overload
    @staticmethod
    def getFallback(p0: str) -> str: ...
    @overload
    def getFallback(self) -> "ULocale": ...
    @overload
    def getKeywordValue(self, p0: str) -> str: ...
    @overload
    @staticmethod
    def getKeywordValue(p0: str, p1: str) -> str: ...
    @overload
    @staticmethod
    def getKeywords(p0: str) -> Iterator: ...
    @overload
    def getKeywords(self) -> Iterator: ...
    def getLineOrientation(self) -> str: ...
    def isRightToLeft(self) -> bool: ...
    @staticmethod
    def minimizeSubtags(p0: "ULocale") -> "ULocale": ...
    @overload
    def setKeywordValue(self, p0: str, p1: str) -> "ULocale": ...
    @overload
    @staticmethod
    def setKeywordValue(p0: str, p1: str, p2: str) -> str: ...
    @staticmethod
    def toLegacyKey(p0: str) -> str: ...
    @staticmethod
    def toLegacyType(p0: str, p1: str) -> str: ...
    def toLocale(self) -> Locale: ...
    @staticmethod
    def toUnicodeLocaleKey(p0: str) -> str: ...
    @staticmethod
    def toUnicodeLocaleType(p0: str, p1: str) -> str: ...
    @overload
    def getLanguage(self) -> str: ...
    @overload
    @staticmethod
    def getLanguage(p0: str) -> str: ...
    @overload
    @staticmethod
    def getName(p0: str) -> str: ...
    @overload
    def getName(self) -> str: ...
    def equals(self, p0: Any) -> bool: ...
    def toString(self) -> str: ...
    def hashCode(self) -> int: ...
    def clone(self) -> Any: ...
    @overload
    def compareTo(self, p0: "ULocale") -> int: ...
    @overload
    def compareTo(self, p0: Any) -> int: ...
    @overload
    @staticmethod
    def getDefault(p0: Any) -> "ULocale": ...
    @overload
    @staticmethod
    def getDefault() -> "ULocale": ...
    @overload
    @staticmethod
    def getDisplayName(p0: str, p1: str) -> str: ...
    @overload
    @staticmethod
    def getDisplayName(p0: str, p1: "ULocale") -> str: ...
    @overload
    def getDisplayName(self) -> str: ...
    @overload
    def getDisplayName(self, p0: "ULocale") -> str: ...
    @staticmethod
    def getAvailableLocales() -> Any: ...
    @staticmethod
    def getISOCountries() -> Any: ...
    @staticmethod
    def getISOLanguages() -> Any: ...
    @overload
    @staticmethod
    def getCountry(p0: str) -> str: ...
    @overload
    def getCountry(self) -> str: ...
    def getExtension(self, p0: str) -> str: ...
    def getExtensionKeys(self) -> set: ...
    def toLanguageTag(self) -> str: ...
    @staticmethod
    def forLanguageTag(p0: str) -> "ULocale": ...
    @overload
    @staticmethod
    def getISO3Language(p0: str) -> str: ...
    @overload
    def getISO3Language(self) -> str: ...
    @overload
    @staticmethod
    def getISO3Country(p0: str) -> str: ...
    @overload
    def getISO3Country(self) -> str: ...
    @staticmethod
    def canonicalize(p0: str) -> str: ...
    @overload
    def getScript(self) -> str: ...
    @overload
    @staticmethod
    def getScript(p0: str) -> str: ...
    @overload
    @staticmethod
    def getVariant(p0: str) -> str: ...
    @overload
    def getVariant(self) -> str: ...
    def getUnicodeLocaleAttributes(self) -> set: ...
    def getUnicodeLocaleType(self, p0: str) -> str: ...
    def getUnicodeLocaleKeys(self) -> set: ...
    @overload
    def getDisplayLanguage(self) -> str: ...
    @overload
    def getDisplayLanguage(self, p0: "ULocale") -> str: ...
    @overload
    @staticmethod
    def getDisplayLanguage(p0: str, p1: "ULocale") -> str: ...
    @overload
    @staticmethod
    def getDisplayLanguage(p0: str, p1: str) -> str: ...
    @overload
    @staticmethod
    def getDisplayScript(p0: str, p1: "ULocale") -> str: ...
    @overload
    @staticmethod
    def getDisplayScript(p0: str, p1: str) -> str: ...
    @overload
    def getDisplayScript(self, p0: "ULocale") -> str: ...
    @overload
    def getDisplayScript(self) -> str: ...
    @overload
    @staticmethod
    def getDisplayCountry(p0: str, p1: "ULocale") -> str: ...
    @overload
    def getDisplayCountry(self) -> str: ...
    @overload
    @staticmethod
    def getDisplayCountry(p0: str, p1: str) -> str: ...
    @overload
    def getDisplayCountry(self, p0: "ULocale") -> str: ...
    @overload
    @staticmethod
    def getDisplayVariant(p0: str, p1: "ULocale") -> str: ...
    @overload
    def getDisplayVariant(self, p0: "ULocale") -> str: ...
    @overload
    def getDisplayVariant(self) -> str: ...
    @overload
    @staticmethod
    def getDisplayVariant(p0: str, p1: str) -> str: ...

    class Category:
        DISPLAY: ClassVar["Category"]
        FORMAT: ClassVar["Category"]
        DISPLAY: ClassVar[Any]
        FORMAT: ClassVar[Any]
        @staticmethod
        def values() -> Any: ...
        @staticmethod
        def valueOf(p0: str) -> Any: ...

    class Builder:
        def __init__(self) -> None: ...
        def setExtension(self, p0: str, p1: str) -> Any: ...
        def addUnicodeLocaleAttribute(self, p0: str) -> Any: ...
        def setScript(self, p0: str) -> Any: ...
        def clearExtensions(self) -> Any: ...
        def setVariant(self, p0: str) -> Any: ...
        def removeUnicodeLocaleAttribute(self, p0: str) -> Any: ...
        def setRegion(self, p0: str) -> Any: ...
        def setUnicodeLocaleKeyword(self, p0: str, p1: str) -> Any: ...
        def clear(self) -> Any: ...
        def setLocale(self, p0: "ULocale") -> Any: ...
        def setLanguage(self, p0: str) -> Any: ...
        def build(self) -> "ULocale": ...
        def setLanguageTag(self, p0: str) -> Any: ...

    class AvailableType:
        DEFAULT: ClassVar["AvailableType"]
        ONLY_LEGACY_ALIASES: ClassVar["AvailableType"]
        WITH_LEGACY_ALIASES: ClassVar["AvailableType"]
        DEFAULT: ClassVar[Any]
        ONLY_LEGACY_ALIASES: ClassVar[Any]
        WITH_LEGACY_ALIASES: ClassVar[Any]
        @staticmethod
        def values() -> Any: ...
        @staticmethod
        def valueOf(p0: str) -> Any: ...

from typing import Any, ClassVar, overload
from android.icu.util.TimeZone import TimeZone
from android.icu.util.ULocale import ULocale
from java.util.Date import Date
from java.util.Locale import Locale

class HebrewCalendar:
    ADAR: ClassVar[int]
    ADAR_1: ClassVar[int]
    AV: ClassVar[int]
    ELUL: ClassVar[int]
    HESHVAN: ClassVar[int]
    IYAR: ClassVar[int]
    KISLEV: ClassVar[int]
    NISAN: ClassVar[int]
    SHEVAT: ClassVar[int]
    SIVAN: ClassVar[int]
    TAMUZ: ClassVar[int]
    TEVET: ClassVar[int]
    TISHRI: ClassVar[int]
    AM: ClassVar[int]
    AM_PM: ClassVar[int]
    APRIL: ClassVar[int]
    AUGUST: ClassVar[int]
    DATE: ClassVar[int]
    DAY_OF_MONTH: ClassVar[int]
    DAY_OF_WEEK: ClassVar[int]
    DAY_OF_WEEK_IN_MONTH: ClassVar[int]
    DAY_OF_YEAR: ClassVar[int]
    DECEMBER: ClassVar[int]
    DOW_LOCAL: ClassVar[int]
    DST_OFFSET: ClassVar[int]
    ERA: ClassVar[int]
    EXTENDED_YEAR: ClassVar[int]
    FEBRUARY: ClassVar[int]
    FRIDAY: ClassVar[int]
    HOUR: ClassVar[int]
    HOUR_OF_DAY: ClassVar[int]
    IS_LEAP_MONTH: ClassVar[int]
    JANUARY: ClassVar[int]
    JULIAN_DAY: ClassVar[int]
    JULY: ClassVar[int]
    JUNE: ClassVar[int]
    MARCH: ClassVar[int]
    MAY: ClassVar[int]
    MILLISECOND: ClassVar[int]
    MILLISECONDS_IN_DAY: ClassVar[int]
    MINUTE: ClassVar[int]
    MONDAY: ClassVar[int]
    MONTH: ClassVar[int]
    NOVEMBER: ClassVar[int]
    OCTOBER: ClassVar[int]
    ORDINAL_MONTH: ClassVar[int]
    PM: ClassVar[int]
    SATURDAY: ClassVar[int]
    SECOND: ClassVar[int]
    SEPTEMBER: ClassVar[int]
    SUNDAY: ClassVar[int]
    THURSDAY: ClassVar[int]
    TUESDAY: ClassVar[int]
    UNDECIMBER: ClassVar[int]
    WALLTIME_FIRST: ClassVar[int]
    WALLTIME_LAST: ClassVar[int]
    WALLTIME_NEXT_VALID: ClassVar[int]
    WEDNESDAY: ClassVar[int]
    WEEK_OF_MONTH: ClassVar[int]
    WEEK_OF_YEAR: ClassVar[int]
    YEAR: ClassVar[int]
    YEAR_WOY: ClassVar[int]
    ZONE_OFFSET: ClassVar[int]
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, p0: int, p1: int, p2: int) -> None: ...
    @overload
    def __init__(self, p0: TimeZone) -> None: ...
    @overload
    def __init__(self, p0: TimeZone, p1: Locale) -> None: ...
    @overload
    def __init__(self, p0: TimeZone, p1: ULocale) -> None: ...
    @overload
    def __init__(self, p0: ULocale) -> None: ...
    @overload
    def __init__(self, p0: Locale) -> None: ...
    @overload
    def __init__(self, p0: Date) -> None: ...
    @overload
    def __init__(self, p0: int, p1: int, p2: int, p3: int, p4: int, p5: int) -> None: ...
    def getTemporalMonthCode(self) -> str: ...
    def inTemporalLeapYear(self) -> bool: ...
    def setTemporalMonthCode(self, p0: str) -> None: ...
    def add(self, p0: int, p1: int) -> None: ...
    def getType(self) -> str: ...
    def roll(self, p0: int, p1: int) -> None: ...

from typing import Any, ClassVar, overload

class IllformedLocaleException:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, p0: str, p1: int) -> None: ...
    @overload
    def __init__(self, p0: str) -> None: ...
    def getErrorIndex(self) -> int: ...

from typing import Any, ClassVar, overload
from android.icu.util.TimeZone import TimeZone
from android.icu.util.ULocale import ULocale
from java.util.Date import Date
from java.util.Locale import Locale

class IndianCalendar:
    AGRAHAYANA: ClassVar[int]
    ASADHA: ClassVar[int]
    ASVINA: ClassVar[int]
    BHADRA: ClassVar[int]
    CHAITRA: ClassVar[int]
    IE: ClassVar[int]
    JYAISTHA: ClassVar[int]
    KARTIKA: ClassVar[int]
    MAGHA: ClassVar[int]
    PAUSA: ClassVar[int]
    PHALGUNA: ClassVar[int]
    SRAVANA: ClassVar[int]
    VAISAKHA: ClassVar[int]
    AM: ClassVar[int]
    AM_PM: ClassVar[int]
    APRIL: ClassVar[int]
    AUGUST: ClassVar[int]
    DATE: ClassVar[int]
    DAY_OF_MONTH: ClassVar[int]
    DAY_OF_WEEK: ClassVar[int]
    DAY_OF_WEEK_IN_MONTH: ClassVar[int]
    DAY_OF_YEAR: ClassVar[int]
    DECEMBER: ClassVar[int]
    DOW_LOCAL: ClassVar[int]
    DST_OFFSET: ClassVar[int]
    ERA: ClassVar[int]
    EXTENDED_YEAR: ClassVar[int]
    FEBRUARY: ClassVar[int]
    FRIDAY: ClassVar[int]
    HOUR: ClassVar[int]
    HOUR_OF_DAY: ClassVar[int]
    IS_LEAP_MONTH: ClassVar[int]
    JANUARY: ClassVar[int]
    JULIAN_DAY: ClassVar[int]
    JULY: ClassVar[int]
    JUNE: ClassVar[int]
    MARCH: ClassVar[int]
    MAY: ClassVar[int]
    MILLISECOND: ClassVar[int]
    MILLISECONDS_IN_DAY: ClassVar[int]
    MINUTE: ClassVar[int]
    MONDAY: ClassVar[int]
    MONTH: ClassVar[int]
    NOVEMBER: ClassVar[int]
    OCTOBER: ClassVar[int]
    ORDINAL_MONTH: ClassVar[int]
    PM: ClassVar[int]
    SATURDAY: ClassVar[int]
    SECOND: ClassVar[int]
    SEPTEMBER: ClassVar[int]
    SUNDAY: ClassVar[int]
    THURSDAY: ClassVar[int]
    TUESDAY: ClassVar[int]
    UNDECIMBER: ClassVar[int]
    WALLTIME_FIRST: ClassVar[int]
    WALLTIME_LAST: ClassVar[int]
    WALLTIME_NEXT_VALID: ClassVar[int]
    WEDNESDAY: ClassVar[int]
    WEEK_OF_MONTH: ClassVar[int]
    WEEK_OF_YEAR: ClassVar[int]
    YEAR: ClassVar[int]
    YEAR_WOY: ClassVar[int]
    ZONE_OFFSET: ClassVar[int]
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, p0: Locale) -> None: ...
    @overload
    def __init__(self, p0: ULocale) -> None: ...
    @overload
    def __init__(self, p0: TimeZone, p1: Locale) -> None: ...
    @overload
    def __init__(self, p0: TimeZone, p1: ULocale) -> None: ...
    @overload
    def __init__(self, p0: TimeZone) -> None: ...
    @overload
    def __init__(self, p0: Date) -> None: ...
    @overload
    def __init__(self, p0: int, p1: int, p2: int, p3: int, p4: int, p5: int) -> None: ...
    @overload
    def __init__(self, p0: int, p1: int, p2: int) -> None: ...
    def getType(self) -> str: ...

from typing import Any, ClassVar, overload
from android.icu.util.MeasureUnit import MeasureUnit

class TimeUnit:
    ACRE: ClassVar[MeasureUnit]
    ACRE_FOOT: ClassVar[MeasureUnit]
    AMPERE: ClassVar[MeasureUnit]
    ARC_MINUTE: ClassVar[MeasureUnit]
    ARC_SECOND: ClassVar[MeasureUnit]
    ASTRONOMICAL_UNIT: ClassVar[MeasureUnit]
    ATMOSPHERE: ClassVar[MeasureUnit]
    BEAUFORT: ClassVar[MeasureUnit]
    BIT: ClassVar[MeasureUnit]
    BUSHEL: ClassVar[MeasureUnit]
    BYTE: ClassVar[MeasureUnit]
    CALORIE: ClassVar[MeasureUnit]
    CANDELA: ClassVar[MeasureUnit]
    CARAT: ClassVar[MeasureUnit]
    CELSIUS: ClassVar[MeasureUnit]
    CENTILITER: ClassVar[MeasureUnit]
    CENTIMETER: ClassVar[MeasureUnit]
    CENTURY: ClassVar[MeasureUnit]
    CUBIC_CENTIMETER: ClassVar[MeasureUnit]
    CUBIC_FOOT: ClassVar[MeasureUnit]
    CUBIC_INCH: ClassVar[MeasureUnit]
    CUBIC_KILOMETER: ClassVar[MeasureUnit]
    CUBIC_METER: ClassVar[MeasureUnit]
    CUBIC_MILE: ClassVar[MeasureUnit]
    CUBIC_YARD: ClassVar[MeasureUnit]
    CUP: ClassVar[MeasureUnit]
    CUP_METRIC: ClassVar[MeasureUnit]
    DAY: ClassVar["TimeUnit"]
    DECADE: ClassVar[MeasureUnit]
    DECILITER: ClassVar[MeasureUnit]
    DECIMETER: ClassVar[MeasureUnit]
    DEGREE: ClassVar[MeasureUnit]
    DOT: ClassVar[MeasureUnit]
    DOT_PER_CENTIMETER: ClassVar[MeasureUnit]
    DOT_PER_INCH: ClassVar[MeasureUnit]
    EM: ClassVar[MeasureUnit]
    FAHRENHEIT: ClassVar[MeasureUnit]
    FATHOM: ClassVar[MeasureUnit]
    FLUID_OUNCE: ClassVar[MeasureUnit]
    FOODCALORIE: ClassVar[MeasureUnit]
    FOOT: ClassVar[MeasureUnit]
    FURLONG: ClassVar[MeasureUnit]
    GALLON: ClassVar[MeasureUnit]
    GALLON_IMPERIAL: ClassVar[MeasureUnit]
    GASOLINE_ENERGY_DENSITY: ClassVar[MeasureUnit]
    GENERIC_TEMPERATURE: ClassVar[MeasureUnit]
    GIGABIT: ClassVar[MeasureUnit]
    GIGABYTE: ClassVar[MeasureUnit]
    GIGAHERTZ: ClassVar[MeasureUnit]
    GIGAWATT: ClassVar[MeasureUnit]
    GRAM: ClassVar[MeasureUnit]
    G_FORCE: ClassVar[MeasureUnit]
    HECTARE: ClassVar[MeasureUnit]
    HECTOLITER: ClassVar[MeasureUnit]
    HECTOPASCAL: ClassVar[MeasureUnit]
    HERTZ: ClassVar[MeasureUnit]
    HORSEPOWER: ClassVar[MeasureUnit]
    HOUR: ClassVar["TimeUnit"]
    INCH: ClassVar[MeasureUnit]
    INCH_HG: ClassVar[MeasureUnit]
    ITEM: ClassVar[MeasureUnit]
    JOULE: ClassVar[MeasureUnit]
    KARAT: ClassVar[MeasureUnit]
    KELVIN: ClassVar[MeasureUnit]
    KILOBIT: ClassVar[MeasureUnit]
    KILOBYTE: ClassVar[MeasureUnit]
    KILOCALORIE: ClassVar[MeasureUnit]
    KILOGRAM: ClassVar[MeasureUnit]
    KILOHERTZ: ClassVar[MeasureUnit]
    KILOJOULE: ClassVar[MeasureUnit]
    KILOMETER: ClassVar[MeasureUnit]
    KILOMETER_PER_HOUR: ClassVar[MeasureUnit]
    KILOWATT: ClassVar[MeasureUnit]
    KILOWATT_HOUR: ClassVar[MeasureUnit]
    KILOWATT_HOUR_PER_100_KILOMETER: ClassVar[MeasureUnit]
    KNOT: ClassVar[MeasureUnit]
    LIGHT_YEAR: ClassVar[MeasureUnit]
    LITER: ClassVar[MeasureUnit]
    LITER_PER_100KILOMETERS: ClassVar[MeasureUnit]
    LITER_PER_KILOMETER: ClassVar[MeasureUnit]
    LUMEN: ClassVar[MeasureUnit]
    LUX: ClassVar[MeasureUnit]
    MEGABIT: ClassVar[MeasureUnit]
    MEGABYTE: ClassVar[MeasureUnit]
    MEGAHERTZ: ClassVar[MeasureUnit]
    MEGALITER: ClassVar[MeasureUnit]
    MEGAPIXEL: ClassVar[MeasureUnit]
    MEGAWATT: ClassVar[MeasureUnit]
    METER: ClassVar[MeasureUnit]
    METER_PER_SECOND: ClassVar[MeasureUnit]
    METER_PER_SECOND_SQUARED: ClassVar[MeasureUnit]
    METRIC_TON: ClassVar[MeasureUnit]
    MICROGRAM: ClassVar[MeasureUnit]
    MICROMETER: ClassVar[MeasureUnit]
    MICROSECOND: ClassVar[MeasureUnit]
    MILE: ClassVar[MeasureUnit]
    MILE_PER_GALLON: ClassVar[MeasureUnit]
    MILE_PER_GALLON_IMPERIAL: ClassVar[MeasureUnit]
    MILE_PER_HOUR: ClassVar[MeasureUnit]
    MILE_SCANDINAVIAN: ClassVar[MeasureUnit]
    MILLIAMPERE: ClassVar[MeasureUnit]
    MILLIBAR: ClassVar[MeasureUnit]
    MILLIGRAM: ClassVar[MeasureUnit]
    MILLIGRAM_OFGLUCOSE_PER_DECILITER: ClassVar[MeasureUnit]
    MILLIGRAM_PER_DECILITER: ClassVar[MeasureUnit]
    MILLILITER: ClassVar[MeasureUnit]
    MILLIMETER: ClassVar[MeasureUnit]
    MILLIMETER_OF_MERCURY: ClassVar[MeasureUnit]
    MILLIMOLE_PER_LITER: ClassVar[MeasureUnit]
    MILLISECOND: ClassVar[MeasureUnit]
    MILLIWATT: ClassVar[MeasureUnit]
    MINUTE: ClassVar["TimeUnit"]
    MONTH: ClassVar["TimeUnit"]
    NANOMETER: ClassVar[MeasureUnit]
    NANOSECOND: ClassVar[MeasureUnit]
    NAUTICAL_MILE: ClassVar[MeasureUnit]
    OHM: ClassVar[MeasureUnit]
    OUNCE: ClassVar[MeasureUnit]
    OUNCE_TROY: ClassVar[MeasureUnit]
    PARSEC: ClassVar[MeasureUnit]
    PART_PER_MILLION: ClassVar[MeasureUnit]
    PERCENT: ClassVar[MeasureUnit]
    PERMILLE: ClassVar[MeasureUnit]
    PETABYTE: ClassVar[MeasureUnit]
    PICOMETER: ClassVar[MeasureUnit]
    PINT: ClassVar[MeasureUnit]
    PINT_METRIC: ClassVar[MeasureUnit]
    PIXEL: ClassVar[MeasureUnit]
    PIXEL_PER_CENTIMETER: ClassVar[MeasureUnit]
    PIXEL_PER_INCH: ClassVar[MeasureUnit]
    POINT: ClassVar[MeasureUnit]
    POUND: ClassVar[MeasureUnit]
    POUND_PER_SQUARE_INCH: ClassVar[MeasureUnit]
    QUART: ClassVar[MeasureUnit]
    QUARTER: ClassVar[MeasureUnit]
    RADIAN: ClassVar[MeasureUnit]
    REVOLUTION_ANGLE: ClassVar[MeasureUnit]
    SECOND: ClassVar["TimeUnit"]
    SQUARE_CENTIMETER: ClassVar[MeasureUnit]
    SQUARE_FOOT: ClassVar[MeasureUnit]
    SQUARE_INCH: ClassVar[MeasureUnit]
    SQUARE_KILOMETER: ClassVar[MeasureUnit]
    SQUARE_METER: ClassVar[MeasureUnit]
    SQUARE_MILE: ClassVar[MeasureUnit]
    SQUARE_YARD: ClassVar[MeasureUnit]
    STONE: ClassVar[MeasureUnit]
    TABLESPOON: ClassVar[MeasureUnit]
    TEASPOON: ClassVar[MeasureUnit]
    TERABIT: ClassVar[MeasureUnit]
    TERABYTE: ClassVar[MeasureUnit]
    TON: ClassVar[MeasureUnit]
    TONNE: ClassVar[MeasureUnit]
    VOLT: ClassVar[MeasureUnit]
    WATT: ClassVar[MeasureUnit]
    WEEK: ClassVar["TimeUnit"]
    YARD: ClassVar[MeasureUnit]
    YEAR: ClassVar["TimeUnit"]
    @staticmethod
    def values() -> Any: ...

from typing import Any, ClassVar, overload
from android.icu.util.TimeZone import TimeZone
from android.icu.util.ULocale import ULocale
from java.util.Date import Date
from java.util.Locale import Locale

class BuddhistCalendar:
    BE: ClassVar[int]
    AD: ClassVar[int]
    BC: ClassVar[int]
    AM: ClassVar[int]
    AM_PM: ClassVar[int]
    APRIL: ClassVar[int]
    AUGUST: ClassVar[int]
    DATE: ClassVar[int]
    DAY_OF_MONTH: ClassVar[int]
    DAY_OF_WEEK: ClassVar[int]
    DAY_OF_WEEK_IN_MONTH: ClassVar[int]
    DAY_OF_YEAR: ClassVar[int]
    DECEMBER: ClassVar[int]
    DOW_LOCAL: ClassVar[int]
    DST_OFFSET: ClassVar[int]
    ERA: ClassVar[int]
    EXTENDED_YEAR: ClassVar[int]
    FEBRUARY: ClassVar[int]
    FRIDAY: ClassVar[int]
    HOUR: ClassVar[int]
    HOUR_OF_DAY: ClassVar[int]
    IS_LEAP_MONTH: ClassVar[int]
    JANUARY: ClassVar[int]
    JULIAN_DAY: ClassVar[int]
    JULY: ClassVar[int]
    JUNE: ClassVar[int]
    MARCH: ClassVar[int]
    MAY: ClassVar[int]
    MILLISECOND: ClassVar[int]
    MILLISECONDS_IN_DAY: ClassVar[int]
    MINUTE: ClassVar[int]
    MONDAY: ClassVar[int]
    MONTH: ClassVar[int]
    NOVEMBER: ClassVar[int]
    OCTOBER: ClassVar[int]
    ORDINAL_MONTH: ClassVar[int]
    PM: ClassVar[int]
    SATURDAY: ClassVar[int]
    SECOND: ClassVar[int]
    SEPTEMBER: ClassVar[int]
    SUNDAY: ClassVar[int]
    THURSDAY: ClassVar[int]
    TUESDAY: ClassVar[int]
    UNDECIMBER: ClassVar[int]
    WALLTIME_FIRST: ClassVar[int]
    WALLTIME_LAST: ClassVar[int]
    WALLTIME_NEXT_VALID: ClassVar[int]
    WEDNESDAY: ClassVar[int]
    WEEK_OF_MONTH: ClassVar[int]
    WEEK_OF_YEAR: ClassVar[int]
    YEAR: ClassVar[int]
    YEAR_WOY: ClassVar[int]
    ZONE_OFFSET: ClassVar[int]
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, p0: Locale) -> None: ...
    @overload
    def __init__(self, p0: Date) -> None: ...
    @overload
    def __init__(self, p0: ULocale) -> None: ...
    @overload
    def __init__(self, p0: TimeZone, p1: Locale) -> None: ...
    @overload
    def __init__(self, p0: TimeZone, p1: ULocale) -> None: ...
    @overload
    def __init__(self, p0: TimeZone) -> None: ...
    @overload
    def __init__(self, p0: int, p1: int, p2: int) -> None: ...
    @overload
    def __init__(self, p0: int, p1: int, p2: int, p3: int, p4: int, p5: int) -> None: ...
    def getType(self) -> str: ...

from typing import Any, ClassVar, overload
from android.icu.util.TimeZone import TimeZone
from android.icu.util.ULocale import ULocale
from java.util.Date import Date
from java.util.Locale import Locale

class IslamicCalendar:
    DHU_AL_HIJJAH: ClassVar[int]
    DHU_AL_QIDAH: ClassVar[int]
    JUMADA_1: ClassVar[int]
    JUMADA_2: ClassVar[int]
    MUHARRAM: ClassVar[int]
    RABI_1: ClassVar[int]
    RABI_2: ClassVar[int]
    RAJAB: ClassVar[int]
    RAMADAN: ClassVar[int]
    SAFAR: ClassVar[int]
    SHABAN: ClassVar[int]
    SHAWWAL: ClassVar[int]
    AM: ClassVar[int]
    AM_PM: ClassVar[int]
    APRIL: ClassVar[int]
    AUGUST: ClassVar[int]
    DATE: ClassVar[int]
    DAY_OF_MONTH: ClassVar[int]
    DAY_OF_WEEK: ClassVar[int]
    DAY_OF_WEEK_IN_MONTH: ClassVar[int]
    DAY_OF_YEAR: ClassVar[int]
    DECEMBER: ClassVar[int]
    DOW_LOCAL: ClassVar[int]
    DST_OFFSET: ClassVar[int]
    ERA: ClassVar[int]
    EXTENDED_YEAR: ClassVar[int]
    FEBRUARY: ClassVar[int]
    FRIDAY: ClassVar[int]
    HOUR: ClassVar[int]
    HOUR_OF_DAY: ClassVar[int]
    IS_LEAP_MONTH: ClassVar[int]
    JANUARY: ClassVar[int]
    JULIAN_DAY: ClassVar[int]
    JULY: ClassVar[int]
    JUNE: ClassVar[int]
    MARCH: ClassVar[int]
    MAY: ClassVar[int]
    MILLISECOND: ClassVar[int]
    MILLISECONDS_IN_DAY: ClassVar[int]
    MINUTE: ClassVar[int]
    MONDAY: ClassVar[int]
    MONTH: ClassVar[int]
    NOVEMBER: ClassVar[int]
    OCTOBER: ClassVar[int]
    ORDINAL_MONTH: ClassVar[int]
    PM: ClassVar[int]
    SATURDAY: ClassVar[int]
    SECOND: ClassVar[int]
    SEPTEMBER: ClassVar[int]
    SUNDAY: ClassVar[int]
    THURSDAY: ClassVar[int]
    TUESDAY: ClassVar[int]
    UNDECIMBER: ClassVar[int]
    WALLTIME_FIRST: ClassVar[int]
    WALLTIME_LAST: ClassVar[int]
    WALLTIME_NEXT_VALID: ClassVar[int]
    WEDNESDAY: ClassVar[int]
    WEEK_OF_MONTH: ClassVar[int]
    WEEK_OF_YEAR: ClassVar[int]
    YEAR: ClassVar[int]
    YEAR_WOY: ClassVar[int]
    ZONE_OFFSET: ClassVar[int]
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, p0: int, p1: int, p2: int) -> None: ...
    @overload
    def __init__(self, p0: ULocale) -> None: ...
    @overload
    def __init__(self, p0: TimeZone, p1: Locale) -> None: ...
    @overload
    def __init__(self, p0: TimeZone, p1: ULocale) -> None: ...
    @overload
    def __init__(self, p0: TimeZone) -> None: ...
    @overload
    def __init__(self, p0: Locale) -> None: ...
    @overload
    def __init__(self, p0: Date) -> None: ...
    @overload
    def __init__(self, p0: int, p1: int, p2: int, p3: int, p4: int, p5: int) -> None: ...
    def getCalculationType(self) -> Any: ...
    def setCalculationType(self, p0: Any) -> None: ...
    def inTemporalLeapYear(self) -> bool: ...
    def getType(self) -> str: ...

    class CalculationType:
        ISLAMIC: ClassVar["CalculationType"]
        ISLAMIC_CIVIL: ClassVar["CalculationType"]
        ISLAMIC_TBLA: ClassVar["CalculationType"]
        ISLAMIC_UMALQURA: ClassVar["CalculationType"]
        ISLAMIC: ClassVar[Any]
        ISLAMIC_CIVIL: ClassVar[Any]
        ISLAMIC_TBLA: ClassVar[Any]
        ISLAMIC_UMALQURA: ClassVar[Any]
        @staticmethod
        def values() -> Any: ...
        @staticmethod
        def valueOf(p0: str) -> Any: ...

from typing import Any, ClassVar, overload
from android.icu.util.ULocale import ULocale
from android.icu.util.VersionInfo import VersionInfo

class LocaleData:
    ALT_QUOTATION_END: ClassVar[int]
    ALT_QUOTATION_START: ClassVar[int]
    QUOTATION_END: ClassVar[int]
    QUOTATION_START: ClassVar[int]
    @staticmethod
    def getCLDRVersion() -> VersionInfo: ...
    def getDelimiter(self, p0: int) -> str: ...
    @staticmethod
    def getMeasurementSystem(p0: ULocale) -> Any: ...
    def getNoSubstitute(self) -> bool: ...
    @staticmethod
    def getPaperSize(p0: ULocale) -> Any: ...
    def setNoSubstitute(self, p0: bool) -> None: ...
    @overload
    @staticmethod
    def getInstance() -> "LocaleData": ...
    @overload
    @staticmethod
    def getInstance(p0: ULocale) -> "LocaleData": ...

    class PaperSize:
        def getHeight(self) -> int: ...
        def getWidth(self) -> int: ...

    class MeasurementSystem:
        SI: ClassVar[Any]
        UK: ClassVar[Any]
        US: ClassVar[Any]

from typing import Any, ClassVar, overload

class DateInterval:
    def __init__(self, p0: int, p1: int) -> None: ...
    def getToDate(self) -> int: ...
    def getFromDate(self) -> int: ...
    def equals(self, p0: Any) -> bool: ...
    def toString(self) -> str: ...
    def hashCode(self) -> int: ...

from typing import Any, ClassVar, overload
from android.icu.text.DateFormat import DateFormat
from android.icu.util.TimeZone import TimeZone
from android.icu.util.ULocale import ULocale
from java.util.Date import Date
from java.util.Locale import Locale

class Calendar:
    AM: ClassVar[int]
    AM_PM: ClassVar[int]
    APRIL: ClassVar[int]
    AUGUST: ClassVar[int]
    DATE: ClassVar[int]
    DAY_OF_MONTH: ClassVar[int]
    DAY_OF_WEEK: ClassVar[int]
    DAY_OF_WEEK_IN_MONTH: ClassVar[int]
    DAY_OF_YEAR: ClassVar[int]
    DECEMBER: ClassVar[int]
    DOW_LOCAL: ClassVar[int]
    DST_OFFSET: ClassVar[int]
    ERA: ClassVar[int]
    EXTENDED_YEAR: ClassVar[int]
    FEBRUARY: ClassVar[int]
    FRIDAY: ClassVar[int]
    HOUR: ClassVar[int]
    HOUR_OF_DAY: ClassVar[int]
    IS_LEAP_MONTH: ClassVar[int]
    JANUARY: ClassVar[int]
    JULIAN_DAY: ClassVar[int]
    JULY: ClassVar[int]
    JUNE: ClassVar[int]
    MARCH: ClassVar[int]
    MAY: ClassVar[int]
    MILLISECOND: ClassVar[int]
    MILLISECONDS_IN_DAY: ClassVar[int]
    MINUTE: ClassVar[int]
    MONDAY: ClassVar[int]
    MONTH: ClassVar[int]
    NOVEMBER: ClassVar[int]
    OCTOBER: ClassVar[int]
    ORDINAL_MONTH: ClassVar[int]
    PM: ClassVar[int]
    SATURDAY: ClassVar[int]
    SECOND: ClassVar[int]
    SEPTEMBER: ClassVar[int]
    SUNDAY: ClassVar[int]
    THURSDAY: ClassVar[int]
    TUESDAY: ClassVar[int]
    UNDECIMBER: ClassVar[int]
    WALLTIME_FIRST: ClassVar[int]
    WALLTIME_LAST: ClassVar[int]
    WALLTIME_NEXT_VALID: ClassVar[int]
    WEDNESDAY: ClassVar[int]
    WEEK_OF_MONTH: ClassVar[int]
    WEEK_OF_YEAR: ClassVar[int]
    YEAR: ClassVar[int]
    YEAR_WOY: ClassVar[int]
    ZONE_OFFSET: ClassVar[int]
    def isLenient(self) -> bool: ...
    def setLenient(self, p0: bool) -> None: ...
    def isEquivalentTo(self, p0: "Calendar") -> bool: ...
    def fieldDifference(self, p0: Date, p1: int) -> int: ...
    @overload
    def getDateTimeFormat(self, p0: int, p1: int, p2: ULocale) -> DateFormat: ...
    @overload
    def getDateTimeFormat(self, p0: int, p1: int, p2: Locale) -> DateFormat: ...
    def getFieldCount(self) -> int: ...
    @staticmethod
    def getKeywordValuesForLocale(p0: str, p1: ULocale, p2: bool) -> Any: ...
    def getRepeatedWallTimeOption(self) -> int: ...
    def getSkippedWallTimeOption(self) -> int: ...
    def getTemporalMonthCode(self) -> str: ...
    def getWeekData(self) -> Any: ...
    @staticmethod
    def getWeekDataForRegion(p0: str) -> Any: ...
    def inTemporalLeapYear(self) -> bool: ...
    @overload
    def isWeekend(self) -> bool: ...
    @overload
    def isWeekend(self, p0: Date) -> bool: ...
    def setRepeatedWallTimeOption(self, p0: int) -> None: ...
    def setSkippedWallTimeOption(self, p0: int) -> None: ...
    def setTemporalMonthCode(self, p0: str) -> None: ...
    def setWeekData(self, p0: Any) -> "Calendar": ...
    def setTime(self, p0: Date) -> None: ...
    def get(self, p0: int) -> int: ...
    def equals(self, p0: Any) -> bool: ...
    def toString(self) -> str: ...
    def hashCode(self) -> int: ...
    def clone(self) -> Any: ...
    @overload
    def compareTo(self, p0: Any) -> int: ...
    @overload
    def compareTo(self, p0: "Calendar") -> int: ...
    @overload
    def clear(self, p0: int) -> None: ...
    @overload
    def clear(self) -> None: ...
    def add(self, p0: int, p1: int) -> None: ...
    @overload
    @staticmethod
    def getInstance(p0: TimeZone, p1: ULocale) -> "Calendar": ...
    @overload
    @staticmethod
    def getInstance() -> "Calendar": ...
    @overload
    @staticmethod
    def getInstance(p0: TimeZone) -> "Calendar": ...
    @overload
    @staticmethod
    def getInstance(p0: ULocale) -> "Calendar": ...
    @overload
    @staticmethod
    def getInstance(p0: Locale) -> "Calendar": ...
    @overload
    @staticmethod
    def getInstance(p0: TimeZone, p1: Locale) -> "Calendar": ...
    @overload
    def set(self, p0: int, p1: int) -> None: ...
    @overload
    def set(self, p0: int, p1: int, p2: int, p3: int, p4: int, p5: int) -> None: ...
    @overload
    def set(self, p0: int, p1: int, p2: int, p3: int, p4: int) -> None: ...
    @overload
    def set(self, p0: int, p1: int, p2: int) -> None: ...
    def isSet(self, p0: int) -> bool: ...
    def getType(self) -> str: ...
    def getMinimalDaysInFirstWeek(self) -> int: ...
    def setFirstDayOfWeek(self, p0: int) -> None: ...
    def getFirstDayOfWeek(self) -> int: ...
    def getTimeZone(self) -> TimeZone: ...
    def setTimeZone(self, p0: TimeZone) -> None: ...
    def before(self, p0: Any) -> bool: ...
    def after(self, p0: Any) -> bool: ...
    @overload
    def getDisplayName(self, p0: Locale) -> str: ...
    @overload
    def getDisplayName(self, p0: ULocale) -> str: ...
    @staticmethod
    def getAvailableLocales() -> Any: ...
    def getTime(self) -> Date: ...
    def getTimeInMillis(self) -> int: ...
    def setTimeInMillis(self, p0: int) -> None: ...
    @overload
    def roll(self, p0: int, p1: int) -> None: ...
    @overload
    def roll(self, p0: int, p1: bool) -> None: ...
    def getGreatestMinimum(self, p0: int) -> int: ...
    def getMinimum(self, p0: int) -> int: ...
    def getLeastMaximum(self, p0: int) -> int: ...
    def getMaximum(self, p0: int) -> int: ...
    def setMinimalDaysInFirstWeek(self, p0: int) -> None: ...
    def getActualMinimum(self, p0: int) -> int: ...
    def getActualMaximum(self, p0: int) -> int: ...

    class WeekData:
        firstDayOfWeek: int
        minimalDaysInFirstWeek: int
        weekendCease: int
        weekendCeaseMillis: int
        weekendOnset: int
        weekendOnsetMillis: int
        def __init__(self, p0: int, p1: int, p2: int, p3: int, p4: int, p5: int) -> None: ...
        def equals(self, p0: Any) -> bool: ...
        def toString(self) -> str: ...
        def hashCode(self) -> int: ...

from typing import Any, ClassVar, overload

class RangeValueIterator:
    def reset(self) -> None: ...
    def next(self, p0: Any) -> bool: ...

    class Element:
        limit: int
        start: int
        value: int
        def __init__(self) -> None: ...

from typing import Any, ClassVar, overload
from android.icu.util.TimeZone import TimeZone
from android.icu.util.ULocale import ULocale
from java.util.Date import Date
from java.util.Locale import Locale

class CopticCalendar:
    AMSHIR: ClassVar[int]
    BABA: ClassVar[int]
    BARAMHAT: ClassVar[int]
    BARAMOUDA: ClassVar[int]
    BASHANS: ClassVar[int]
    EPEP: ClassVar[int]
    HATOR: ClassVar[int]
    KIAHK: ClassVar[int]
    MESRA: ClassVar[int]
    NASIE: ClassVar[int]
    PAONA: ClassVar[int]
    TOBA: ClassVar[int]
    TOUT: ClassVar[int]
    AM: ClassVar[int]
    AM_PM: ClassVar[int]
    APRIL: ClassVar[int]
    AUGUST: ClassVar[int]
    DATE: ClassVar[int]
    DAY_OF_MONTH: ClassVar[int]
    DAY_OF_WEEK: ClassVar[int]
    DAY_OF_WEEK_IN_MONTH: ClassVar[int]
    DAY_OF_YEAR: ClassVar[int]
    DECEMBER: ClassVar[int]
    DOW_LOCAL: ClassVar[int]
    DST_OFFSET: ClassVar[int]
    ERA: ClassVar[int]
    EXTENDED_YEAR: ClassVar[int]
    FEBRUARY: ClassVar[int]
    FRIDAY: ClassVar[int]
    HOUR: ClassVar[int]
    HOUR_OF_DAY: ClassVar[int]
    IS_LEAP_MONTH: ClassVar[int]
    JANUARY: ClassVar[int]
    JULIAN_DAY: ClassVar[int]
    JULY: ClassVar[int]
    JUNE: ClassVar[int]
    MARCH: ClassVar[int]
    MAY: ClassVar[int]
    MILLISECOND: ClassVar[int]
    MILLISECONDS_IN_DAY: ClassVar[int]
    MINUTE: ClassVar[int]
    MONDAY: ClassVar[int]
    MONTH: ClassVar[int]
    NOVEMBER: ClassVar[int]
    OCTOBER: ClassVar[int]
    ORDINAL_MONTH: ClassVar[int]
    PM: ClassVar[int]
    SATURDAY: ClassVar[int]
    SECOND: ClassVar[int]
    SEPTEMBER: ClassVar[int]
    SUNDAY: ClassVar[int]
    THURSDAY: ClassVar[int]
    TUESDAY: ClassVar[int]
    UNDECIMBER: ClassVar[int]
    WALLTIME_FIRST: ClassVar[int]
    WALLTIME_LAST: ClassVar[int]
    WALLTIME_NEXT_VALID: ClassVar[int]
    WEDNESDAY: ClassVar[int]
    WEEK_OF_MONTH: ClassVar[int]
    WEEK_OF_YEAR: ClassVar[int]
    YEAR: ClassVar[int]
    YEAR_WOY: ClassVar[int]
    ZONE_OFFSET: ClassVar[int]
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, p0: Locale) -> None: ...
    @overload
    def __init__(self, p0: ULocale) -> None: ...
    @overload
    def __init__(self, p0: TimeZone, p1: Locale) -> None: ...
    @overload
    def __init__(self, p0: TimeZone, p1: ULocale) -> None: ...
    @overload
    def __init__(self, p0: TimeZone) -> None: ...
    @overload
    def __init__(self, p0: Date) -> None: ...
    @overload
    def __init__(self, p0: int, p1: int, p2: int, p3: int, p4: int, p5: int) -> None: ...
    @overload
    def __init__(self, p0: int, p1: int, p2: int) -> None: ...
    def getTemporalMonthCode(self) -> str: ...
    def setTemporalMonthCode(self, p0: str) -> None: ...
    def getType(self) -> str: ...

from typing import Any, ClassVar, overload

class Freezable:
    def cloneAsThawed(self) -> Any: ...
    def freeze(self) -> Any: ...
    def isFrozen(self) -> bool: ...

from typing import Any, ClassVar, overload
from android.icu.util.TimeZone import TimeZone
from android.icu.util.ULocale import ULocale
from java.util.Date import Date
from java.util.Locale import Locale

class ChineseCalendar:
    AM: ClassVar[int]
    AM_PM: ClassVar[int]
    APRIL: ClassVar[int]
    AUGUST: ClassVar[int]
    DATE: ClassVar[int]
    DAY_OF_MONTH: ClassVar[int]
    DAY_OF_WEEK: ClassVar[int]
    DAY_OF_WEEK_IN_MONTH: ClassVar[int]
    DAY_OF_YEAR: ClassVar[int]
    DECEMBER: ClassVar[int]
    DOW_LOCAL: ClassVar[int]
    DST_OFFSET: ClassVar[int]
    ERA: ClassVar[int]
    EXTENDED_YEAR: ClassVar[int]
    FEBRUARY: ClassVar[int]
    FRIDAY: ClassVar[int]
    HOUR: ClassVar[int]
    HOUR_OF_DAY: ClassVar[int]
    IS_LEAP_MONTH: ClassVar[int]
    JANUARY: ClassVar[int]
    JULIAN_DAY: ClassVar[int]
    JULY: ClassVar[int]
    JUNE: ClassVar[int]
    MARCH: ClassVar[int]
    MAY: ClassVar[int]
    MILLISECOND: ClassVar[int]
    MILLISECONDS_IN_DAY: ClassVar[int]
    MINUTE: ClassVar[int]
    MONDAY: ClassVar[int]
    MONTH: ClassVar[int]
    NOVEMBER: ClassVar[int]
    OCTOBER: ClassVar[int]
    ORDINAL_MONTH: ClassVar[int]
    PM: ClassVar[int]
    SATURDAY: ClassVar[int]
    SECOND: ClassVar[int]
    SEPTEMBER: ClassVar[int]
    SUNDAY: ClassVar[int]
    THURSDAY: ClassVar[int]
    TUESDAY: ClassVar[int]
    UNDECIMBER: ClassVar[int]
    WALLTIME_FIRST: ClassVar[int]
    WALLTIME_LAST: ClassVar[int]
    WALLTIME_NEXT_VALID: ClassVar[int]
    WEDNESDAY: ClassVar[int]
    WEEK_OF_MONTH: ClassVar[int]
    WEEK_OF_YEAR: ClassVar[int]
    YEAR: ClassVar[int]
    YEAR_WOY: ClassVar[int]
    ZONE_OFFSET: ClassVar[int]
    @overload
    def __init__(self, p0: TimeZone, p1: Locale) -> None: ...
    @overload
    def __init__(self, p0: ULocale) -> None: ...
    @overload
    def __init__(self, p0: int, p1: int, p2: int, p3: int) -> None: ...
    @overload
    def __init__(self, p0: int, p1: int, p2: int, p3: int, p4: int) -> None: ...
    @overload
    def __init__(self, p0: TimeZone, p1: ULocale) -> None: ...
    @overload
    def __init__(self, p0: TimeZone) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, p0: Locale) -> None: ...
    @overload
    def __init__(self, p0: Date) -> None: ...
    @overload
    def __init__(self, p0: int, p1: int, p2: int, p3: int, p4: int, p5: int, p6: int, p7: int) -> None: ...
    @overload
    def __init__(self, p0: int, p1: int, p2: int, p3: int, p4: int, p5: int, p6: int) -> None: ...
    def getTemporalMonthCode(self) -> str: ...
    def inTemporalLeapYear(self) -> bool: ...
    def setTemporalMonthCode(self, p0: str) -> None: ...
    def add(self, p0: int, p1: int) -> None: ...
    def getType(self) -> str: ...
    def roll(self, p0: int, p1: int) -> None: ...

from typing import Any, ClassVar, overload
from android.icu.util.Currency import Currency
from java.util.Currency import Currency

class CurrencyAmount:
    @overload
    def __init__(self, p0: float, p1: Currency) -> None: ...
    @overload
    def __init__(self, p0: float, p1: Currency) -> None: ...
    @overload
    def __init__(self, p0: float, p1: Currency) -> None: ...
    @overload
    def __init__(self, p0: float, p1: Currency) -> None: ...
    def getCurrency(self) -> Currency: ...

from typing import Any, ClassVar, overload
from android.icu.util.TimeZone import TimeZone
from android.icu.util.ULocale import ULocale
from java.util.Date import Date
from java.util.Locale import Locale

class TaiwanCalendar:
    BEFORE_MINGUO: ClassVar[int]
    MINGUO: ClassVar[int]
    AD: ClassVar[int]
    BC: ClassVar[int]
    AM: ClassVar[int]
    AM_PM: ClassVar[int]
    APRIL: ClassVar[int]
    AUGUST: ClassVar[int]
    DATE: ClassVar[int]
    DAY_OF_MONTH: ClassVar[int]
    DAY_OF_WEEK: ClassVar[int]
    DAY_OF_WEEK_IN_MONTH: ClassVar[int]
    DAY_OF_YEAR: ClassVar[int]
    DECEMBER: ClassVar[int]
    DOW_LOCAL: ClassVar[int]
    DST_OFFSET: ClassVar[int]
    ERA: ClassVar[int]
    EXTENDED_YEAR: ClassVar[int]
    FEBRUARY: ClassVar[int]
    FRIDAY: ClassVar[int]
    HOUR: ClassVar[int]
    HOUR_OF_DAY: ClassVar[int]
    IS_LEAP_MONTH: ClassVar[int]
    JANUARY: ClassVar[int]
    JULIAN_DAY: ClassVar[int]
    JULY: ClassVar[int]
    JUNE: ClassVar[int]
    MARCH: ClassVar[int]
    MAY: ClassVar[int]
    MILLISECOND: ClassVar[int]
    MILLISECONDS_IN_DAY: ClassVar[int]
    MINUTE: ClassVar[int]
    MONDAY: ClassVar[int]
    MONTH: ClassVar[int]
    NOVEMBER: ClassVar[int]
    OCTOBER: ClassVar[int]
    ORDINAL_MONTH: ClassVar[int]
    PM: ClassVar[int]
    SATURDAY: ClassVar[int]
    SECOND: ClassVar[int]
    SEPTEMBER: ClassVar[int]
    SUNDAY: ClassVar[int]
    THURSDAY: ClassVar[int]
    TUESDAY: ClassVar[int]
    UNDECIMBER: ClassVar[int]
    WALLTIME_FIRST: ClassVar[int]
    WALLTIME_LAST: ClassVar[int]
    WALLTIME_NEXT_VALID: ClassVar[int]
    WEDNESDAY: ClassVar[int]
    WEEK_OF_MONTH: ClassVar[int]
    WEEK_OF_YEAR: ClassVar[int]
    YEAR: ClassVar[int]
    YEAR_WOY: ClassVar[int]
    ZONE_OFFSET: ClassVar[int]
    @overload
    def __init__(self, p0: int, p1: int, p2: int, p3: int, p4: int, p5: int) -> None: ...
    @overload
    def __init__(self, p0: Date) -> None: ...
    @overload
    def __init__(self, p0: Locale) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, p0: TimeZone) -> None: ...
    @overload
    def __init__(self, p0: TimeZone, p1: ULocale) -> None: ...
    @overload
    def __init__(self, p0: TimeZone, p1: Locale) -> None: ...
    @overload
    def __init__(self, p0: ULocale) -> None: ...
    @overload
    def __init__(self, p0: int, p1: int, p2: int) -> None: ...
    def getType(self) -> str: ...

from typing import Any, ClassVar, overload
from android.icu.util.MeasureUnit import MeasureUnit
from android.icu.util.TimeUnit import TimeUnit
from android.icu.util.ULocale import ULocale
from java.util.Date import Date
from java.util.Locale import Locale

class Currency:
    FORMAL_SYMBOL_NAME: ClassVar[int]
    LONG_NAME: ClassVar[int]
    NARROW_SYMBOL_NAME: ClassVar[int]
    PLURAL_LONG_NAME: ClassVar[int]
    SYMBOL_NAME: ClassVar[int]
    VARIANT_SYMBOL_NAME: ClassVar[int]
    ACRE: ClassVar[MeasureUnit]
    ACRE_FOOT: ClassVar[MeasureUnit]
    AMPERE: ClassVar[MeasureUnit]
    ARC_MINUTE: ClassVar[MeasureUnit]
    ARC_SECOND: ClassVar[MeasureUnit]
    ASTRONOMICAL_UNIT: ClassVar[MeasureUnit]
    ATMOSPHERE: ClassVar[MeasureUnit]
    BEAUFORT: ClassVar[MeasureUnit]
    BIT: ClassVar[MeasureUnit]
    BUSHEL: ClassVar[MeasureUnit]
    BYTE: ClassVar[MeasureUnit]
    CALORIE: ClassVar[MeasureUnit]
    CANDELA: ClassVar[MeasureUnit]
    CARAT: ClassVar[MeasureUnit]
    CELSIUS: ClassVar[MeasureUnit]
    CENTILITER: ClassVar[MeasureUnit]
    CENTIMETER: ClassVar[MeasureUnit]
    CENTURY: ClassVar[MeasureUnit]
    CUBIC_CENTIMETER: ClassVar[MeasureUnit]
    CUBIC_FOOT: ClassVar[MeasureUnit]
    CUBIC_INCH: ClassVar[MeasureUnit]
    CUBIC_KILOMETER: ClassVar[MeasureUnit]
    CUBIC_METER: ClassVar[MeasureUnit]
    CUBIC_MILE: ClassVar[MeasureUnit]
    CUBIC_YARD: ClassVar[MeasureUnit]
    CUP: ClassVar[MeasureUnit]
    CUP_METRIC: ClassVar[MeasureUnit]
    DAY: ClassVar[TimeUnit]
    DECADE: ClassVar[MeasureUnit]
    DECILITER: ClassVar[MeasureUnit]
    DECIMETER: ClassVar[MeasureUnit]
    DEGREE: ClassVar[MeasureUnit]
    DOT: ClassVar[MeasureUnit]
    DOT_PER_CENTIMETER: ClassVar[MeasureUnit]
    DOT_PER_INCH: ClassVar[MeasureUnit]
    EM: ClassVar[MeasureUnit]
    FAHRENHEIT: ClassVar[MeasureUnit]
    FATHOM: ClassVar[MeasureUnit]
    FLUID_OUNCE: ClassVar[MeasureUnit]
    FOODCALORIE: ClassVar[MeasureUnit]
    FOOT: ClassVar[MeasureUnit]
    FURLONG: ClassVar[MeasureUnit]
    GALLON: ClassVar[MeasureUnit]
    GALLON_IMPERIAL: ClassVar[MeasureUnit]
    GASOLINE_ENERGY_DENSITY: ClassVar[MeasureUnit]
    GENERIC_TEMPERATURE: ClassVar[MeasureUnit]
    GIGABIT: ClassVar[MeasureUnit]
    GIGABYTE: ClassVar[MeasureUnit]
    GIGAHERTZ: ClassVar[MeasureUnit]
    GIGAWATT: ClassVar[MeasureUnit]
    GRAM: ClassVar[MeasureUnit]
    G_FORCE: ClassVar[MeasureUnit]
    HECTARE: ClassVar[MeasureUnit]
    HECTOLITER: ClassVar[MeasureUnit]
    HECTOPASCAL: ClassVar[MeasureUnit]
    HERTZ: ClassVar[MeasureUnit]
    HORSEPOWER: ClassVar[MeasureUnit]
    HOUR: ClassVar[TimeUnit]
    INCH: ClassVar[MeasureUnit]
    INCH_HG: ClassVar[MeasureUnit]
    ITEM: ClassVar[MeasureUnit]
    JOULE: ClassVar[MeasureUnit]
    KARAT: ClassVar[MeasureUnit]
    KELVIN: ClassVar[MeasureUnit]
    KILOBIT: ClassVar[MeasureUnit]
    KILOBYTE: ClassVar[MeasureUnit]
    KILOCALORIE: ClassVar[MeasureUnit]
    KILOGRAM: ClassVar[MeasureUnit]
    KILOHERTZ: ClassVar[MeasureUnit]
    KILOJOULE: ClassVar[MeasureUnit]
    KILOMETER: ClassVar[MeasureUnit]
    KILOMETER_PER_HOUR: ClassVar[MeasureUnit]
    KILOWATT: ClassVar[MeasureUnit]
    KILOWATT_HOUR: ClassVar[MeasureUnit]
    KILOWATT_HOUR_PER_100_KILOMETER: ClassVar[MeasureUnit]
    KNOT: ClassVar[MeasureUnit]
    LIGHT_YEAR: ClassVar[MeasureUnit]
    LITER: ClassVar[MeasureUnit]
    LITER_PER_100KILOMETERS: ClassVar[MeasureUnit]
    LITER_PER_KILOMETER: ClassVar[MeasureUnit]
    LUMEN: ClassVar[MeasureUnit]
    LUX: ClassVar[MeasureUnit]
    MEGABIT: ClassVar[MeasureUnit]
    MEGABYTE: ClassVar[MeasureUnit]
    MEGAHERTZ: ClassVar[MeasureUnit]
    MEGALITER: ClassVar[MeasureUnit]
    MEGAPIXEL: ClassVar[MeasureUnit]
    MEGAWATT: ClassVar[MeasureUnit]
    METER: ClassVar[MeasureUnit]
    METER_PER_SECOND: ClassVar[MeasureUnit]
    METER_PER_SECOND_SQUARED: ClassVar[MeasureUnit]
    METRIC_TON: ClassVar[MeasureUnit]
    MICROGRAM: ClassVar[MeasureUnit]
    MICROMETER: ClassVar[MeasureUnit]
    MICROSECOND: ClassVar[MeasureUnit]
    MILE: ClassVar[MeasureUnit]
    MILE_PER_GALLON: ClassVar[MeasureUnit]
    MILE_PER_GALLON_IMPERIAL: ClassVar[MeasureUnit]
    MILE_PER_HOUR: ClassVar[MeasureUnit]
    MILE_SCANDINAVIAN: ClassVar[MeasureUnit]
    MILLIAMPERE: ClassVar[MeasureUnit]
    MILLIBAR: ClassVar[MeasureUnit]
    MILLIGRAM: ClassVar[MeasureUnit]
    MILLIGRAM_OFGLUCOSE_PER_DECILITER: ClassVar[MeasureUnit]
    MILLIGRAM_PER_DECILITER: ClassVar[MeasureUnit]
    MILLILITER: ClassVar[MeasureUnit]
    MILLIMETER: ClassVar[MeasureUnit]
    MILLIMETER_OF_MERCURY: ClassVar[MeasureUnit]
    MILLIMOLE_PER_LITER: ClassVar[MeasureUnit]
    MILLISECOND: ClassVar[MeasureUnit]
    MILLIWATT: ClassVar[MeasureUnit]
    MINUTE: ClassVar[TimeUnit]
    MONTH: ClassVar[TimeUnit]
    NANOMETER: ClassVar[MeasureUnit]
    NANOSECOND: ClassVar[MeasureUnit]
    NAUTICAL_MILE: ClassVar[MeasureUnit]
    OHM: ClassVar[MeasureUnit]
    OUNCE: ClassVar[MeasureUnit]
    OUNCE_TROY: ClassVar[MeasureUnit]
    PARSEC: ClassVar[MeasureUnit]
    PART_PER_MILLION: ClassVar[MeasureUnit]
    PERCENT: ClassVar[MeasureUnit]
    PERMILLE: ClassVar[MeasureUnit]
    PETABYTE: ClassVar[MeasureUnit]
    PICOMETER: ClassVar[MeasureUnit]
    PINT: ClassVar[MeasureUnit]
    PINT_METRIC: ClassVar[MeasureUnit]
    PIXEL: ClassVar[MeasureUnit]
    PIXEL_PER_CENTIMETER: ClassVar[MeasureUnit]
    PIXEL_PER_INCH: ClassVar[MeasureUnit]
    POINT: ClassVar[MeasureUnit]
    POUND: ClassVar[MeasureUnit]
    POUND_PER_SQUARE_INCH: ClassVar[MeasureUnit]
    QUART: ClassVar[MeasureUnit]
    QUARTER: ClassVar[MeasureUnit]
    RADIAN: ClassVar[MeasureUnit]
    REVOLUTION_ANGLE: ClassVar[MeasureUnit]
    SECOND: ClassVar[TimeUnit]
    SQUARE_CENTIMETER: ClassVar[MeasureUnit]
    SQUARE_FOOT: ClassVar[MeasureUnit]
    SQUARE_INCH: ClassVar[MeasureUnit]
    SQUARE_KILOMETER: ClassVar[MeasureUnit]
    SQUARE_METER: ClassVar[MeasureUnit]
    SQUARE_MILE: ClassVar[MeasureUnit]
    SQUARE_YARD: ClassVar[MeasureUnit]
    STONE: ClassVar[MeasureUnit]
    TABLESPOON: ClassVar[MeasureUnit]
    TEASPOON: ClassVar[MeasureUnit]
    TERABIT: ClassVar[MeasureUnit]
    TERABYTE: ClassVar[MeasureUnit]
    TON: ClassVar[MeasureUnit]
    TONNE: ClassVar[MeasureUnit]
    VOLT: ClassVar[MeasureUnit]
    WATT: ClassVar[MeasureUnit]
    WEEK: ClassVar[TimeUnit]
    YARD: ClassVar[MeasureUnit]
    YEAR: ClassVar[TimeUnit]
    @staticmethod
    def isAvailable(p0: str, p1: Date, p2: Date) -> bool: ...
    @staticmethod
    def getKeywordValuesForLocale(p0: str, p1: ULocale, p2: bool) -> Any: ...
    @overload
    def getSymbol(self, p0: ULocale) -> str: ...
    @overload
    def getSymbol(self) -> str: ...
    @overload
    def getSymbol(self, p0: Locale) -> str: ...
    @staticmethod
    def getAvailableCurrencies() -> set: ...
    def getCurrencyCode(self) -> str: ...
    @overload
    def getDefaultFractionDigits(self, p0: Any) -> int: ...
    @overload
    def getDefaultFractionDigits(self) -> int: ...
    def getNumericCode(self) -> int: ...
    @overload
    def getName(self, p0: ULocale, p1: int, p2: Any) -> str: ...
    @overload
    def getName(self, p0: ULocale, p1: int, p2: str, p3: Any) -> str: ...
    @overload
    def getName(self, p0: Locale, p1: int, p2: Any) -> str: ...
    @overload
    def getName(self, p0: Locale, p1: int, p2: str, p3: Any) -> str: ...
    def toString(self) -> str: ...
    @overload
    @staticmethod
    def getInstance(p0: Locale) -> "Currency": ...
    @overload
    @staticmethod
    def getInstance(p0: ULocale) -> "Currency": ...
    @overload
    @staticmethod
    def getInstance(p0: str) -> "Currency": ...
    @overload
    def getDisplayName(self, p0: Locale) -> str: ...
    @overload
    def getDisplayName(self) -> str: ...
    @staticmethod
    def getAvailableLocales() -> Any: ...
    @staticmethod
    def fromJavaCurrency(p0: "Currency") -> "Currency": ...
    @overload
    @staticmethod
    def getAvailableCurrencyCodes(p0: ULocale, p1: Date) -> Any: ...
    @overload
    @staticmethod
    def getAvailableCurrencyCodes(p0: Locale, p1: Date) -> Any: ...
    @staticmethod
    def getAvailableULocales() -> Any: ...
    @overload
    def getRoundingIncrement(self, p0: Any) -> float: ...
    @overload
    def getRoundingIncrement(self) -> float: ...
    def toJavaCurrency(self) -> "Currency": ...

    class CurrencyUsage:
        CASH: ClassVar["CurrencyUsage"]
        STANDARD: ClassVar["CurrencyUsage"]
        CASH: ClassVar[Any]
        STANDARD: ClassVar[Any]
        @staticmethod
        def values() -> Any: ...
        @staticmethod
        def valueOf(p0: str) -> Any: ...

from typing import Any, ClassVar, overload
from android.icu.util.TimeZone import TimeZone
from android.icu.util.ULocale import ULocale
from java.util.Date import Date
from java.util.Locale import Locale

class EthiopicCalendar:
    GENBOT: ClassVar[int]
    HAMLE: ClassVar[int]
    HEDAR: ClassVar[int]
    MEGABIT: ClassVar[int]
    MESKEREM: ClassVar[int]
    MIAZIA: ClassVar[int]
    NEHASSE: ClassVar[int]
    PAGUMEN: ClassVar[int]
    SENE: ClassVar[int]
    TAHSAS: ClassVar[int]
    TEKEMT: ClassVar[int]
    TER: ClassVar[int]
    YEKATIT: ClassVar[int]
    AM: ClassVar[int]
    AM_PM: ClassVar[int]
    APRIL: ClassVar[int]
    AUGUST: ClassVar[int]
    DATE: ClassVar[int]
    DAY_OF_MONTH: ClassVar[int]
    DAY_OF_WEEK: ClassVar[int]
    DAY_OF_WEEK_IN_MONTH: ClassVar[int]
    DAY_OF_YEAR: ClassVar[int]
    DECEMBER: ClassVar[int]
    DOW_LOCAL: ClassVar[int]
    DST_OFFSET: ClassVar[int]
    ERA: ClassVar[int]
    EXTENDED_YEAR: ClassVar[int]
    FEBRUARY: ClassVar[int]
    FRIDAY: ClassVar[int]
    HOUR: ClassVar[int]
    HOUR_OF_DAY: ClassVar[int]
    IS_LEAP_MONTH: ClassVar[int]
    JANUARY: ClassVar[int]
    JULIAN_DAY: ClassVar[int]
    JULY: ClassVar[int]
    JUNE: ClassVar[int]
    MARCH: ClassVar[int]
    MAY: ClassVar[int]
    MILLISECOND: ClassVar[int]
    MILLISECONDS_IN_DAY: ClassVar[int]
    MINUTE: ClassVar[int]
    MONDAY: ClassVar[int]
    MONTH: ClassVar[int]
    NOVEMBER: ClassVar[int]
    OCTOBER: ClassVar[int]
    ORDINAL_MONTH: ClassVar[int]
    PM: ClassVar[int]
    SATURDAY: ClassVar[int]
    SECOND: ClassVar[int]
    SEPTEMBER: ClassVar[int]
    SUNDAY: ClassVar[int]
    THURSDAY: ClassVar[int]
    TUESDAY: ClassVar[int]
    UNDECIMBER: ClassVar[int]
    WALLTIME_FIRST: ClassVar[int]
    WALLTIME_LAST: ClassVar[int]
    WALLTIME_NEXT_VALID: ClassVar[int]
    WEDNESDAY: ClassVar[int]
    WEEK_OF_MONTH: ClassVar[int]
    WEEK_OF_YEAR: ClassVar[int]
    YEAR: ClassVar[int]
    YEAR_WOY: ClassVar[int]
    ZONE_OFFSET: ClassVar[int]
    @overload
    def __init__(self, p0: TimeZone, p1: ULocale) -> None: ...
    @overload
    def __init__(self, p0: TimeZone, p1: Locale) -> None: ...
    @overload
    def __init__(self, p0: TimeZone) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, p0: int, p1: int, p2: int, p3: int, p4: int, p5: int) -> None: ...
    @overload
    def __init__(self, p0: Date) -> None: ...
    @overload
    def __init__(self, p0: Locale) -> None: ...
    @overload
    def __init__(self, p0: int, p1: int, p2: int) -> None: ...
    @overload
    def __init__(self, p0: ULocale) -> None: ...
    def getTemporalMonthCode(self) -> str: ...
    def setTemporalMonthCode(self, p0: str) -> None: ...
    def isAmeteAlemEra(self) -> bool: ...
    def setAmeteAlemEra(self, p0: bool) -> None: ...
    def getType(self) -> str: ...

from typing import Any, ClassVar, overload
from android.icu.util.Calendar import Calendar
from android.icu.util.TimeZone import TimeZone
from android.icu.util.ULocale import ULocale
from java.util.Date import Date
from java.util.Locale import Locale

class GregorianCalendar:
    AD: ClassVar[int]
    BC: ClassVar[int]
    AM: ClassVar[int]
    AM_PM: ClassVar[int]
    APRIL: ClassVar[int]
    AUGUST: ClassVar[int]
    DATE: ClassVar[int]
    DAY_OF_MONTH: ClassVar[int]
    DAY_OF_WEEK: ClassVar[int]
    DAY_OF_WEEK_IN_MONTH: ClassVar[int]
    DAY_OF_YEAR: ClassVar[int]
    DECEMBER: ClassVar[int]
    DOW_LOCAL: ClassVar[int]
    DST_OFFSET: ClassVar[int]
    ERA: ClassVar[int]
    EXTENDED_YEAR: ClassVar[int]
    FEBRUARY: ClassVar[int]
    FRIDAY: ClassVar[int]
    HOUR: ClassVar[int]
    HOUR_OF_DAY: ClassVar[int]
    IS_LEAP_MONTH: ClassVar[int]
    JANUARY: ClassVar[int]
    JULIAN_DAY: ClassVar[int]
    JULY: ClassVar[int]
    JUNE: ClassVar[int]
    MARCH: ClassVar[int]
    MAY: ClassVar[int]
    MILLISECOND: ClassVar[int]
    MILLISECONDS_IN_DAY: ClassVar[int]
    MINUTE: ClassVar[int]
    MONDAY: ClassVar[int]
    MONTH: ClassVar[int]
    NOVEMBER: ClassVar[int]
    OCTOBER: ClassVar[int]
    ORDINAL_MONTH: ClassVar[int]
    PM: ClassVar[int]
    SATURDAY: ClassVar[int]
    SECOND: ClassVar[int]
    SEPTEMBER: ClassVar[int]
    SUNDAY: ClassVar[int]
    THURSDAY: ClassVar[int]
    TUESDAY: ClassVar[int]
    UNDECIMBER: ClassVar[int]
    WALLTIME_FIRST: ClassVar[int]
    WALLTIME_LAST: ClassVar[int]
    WALLTIME_NEXT_VALID: ClassVar[int]
    WEDNESDAY: ClassVar[int]
    WEEK_OF_MONTH: ClassVar[int]
    WEEK_OF_YEAR: ClassVar[int]
    YEAR: ClassVar[int]
    YEAR_WOY: ClassVar[int]
    ZONE_OFFSET: ClassVar[int]
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, p0: int, p1: int, p2: int, p3: int, p4: int) -> None: ...
    @overload
    def __init__(self, p0: int, p1: int, p2: int) -> None: ...
    @overload
    def __init__(self, p0: ULocale) -> None: ...
    @overload
    def __init__(self, p0: TimeZone, p1: ULocale) -> None: ...
    @overload
    def __init__(self, p0: TimeZone, p1: Locale) -> None: ...
    @overload
    def __init__(self, p0: TimeZone) -> None: ...
    @overload
    def __init__(self, p0: Locale) -> None: ...
    @overload
    def __init__(self, p0: int, p1: int, p2: int, p3: int, p4: int, p5: int) -> None: ...
    def getGregorianChange(self) -> Date: ...
    def isEquivalentTo(self, p0: Calendar) -> bool: ...
    def setGregorianChange(self, p0: Date) -> None: ...
    def hashCode(self) -> int: ...
    def getType(self) -> str: ...
    def isLeapYear(self, p0: int) -> bool: ...
    def roll(self, p0: int, p1: int) -> None: ...
    def getActualMinimum(self, p0: int) -> int: ...
    def getActualMaximum(self, p0: int) -> int: ...

