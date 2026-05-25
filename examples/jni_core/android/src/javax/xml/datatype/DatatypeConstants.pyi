from typing import Any, ClassVar, overload
from javax.xml.namespace.QName import QName

class DatatypeConstants:
    JANUARY: ClassVar[int]
    FEBRUARY: ClassVar[int]
    MARCH: ClassVar[int]
    APRIL: ClassVar[int]
    MAY: ClassVar[int]
    JUNE: ClassVar[int]
    JULY: ClassVar[int]
    AUGUST: ClassVar[int]
    SEPTEMBER: ClassVar[int]
    OCTOBER: ClassVar[int]
    NOVEMBER: ClassVar[int]
    DECEMBER: ClassVar[int]
    LESSER: ClassVar[int]
    EQUAL: ClassVar[int]
    GREATER: ClassVar[int]
    INDETERMINATE: ClassVar[int]
    FIELD_UNDEFINED: ClassVar[int]
    YEARS: ClassVar[Any]
    MONTHS: ClassVar[Any]
    DAYS: ClassVar[Any]
    HOURS: ClassVar[Any]
    MINUTES: ClassVar[Any]
    SECONDS: ClassVar[Any]
    DATETIME: ClassVar[QName]
    TIME: ClassVar[QName]
    DATE: ClassVar[QName]
    GYEARMONTH: ClassVar[QName]
    GMONTHDAY: ClassVar[QName]
    GYEAR: ClassVar[QName]
    GMONTH: ClassVar[QName]
    GDAY: ClassVar[QName]
    DURATION: ClassVar[QName]
    DURATION_DAYTIME: ClassVar[QName]
    DURATION_YEARMONTH: ClassVar[QName]
    MAX_TIMEZONE_OFFSET: ClassVar[int]
    MIN_TIMEZONE_OFFSET: ClassVar[int]

    class Field:
        def toString(self) -> str: ...
        def getId(self) -> int: ...
