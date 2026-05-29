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
