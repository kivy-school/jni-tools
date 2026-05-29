from typing import Any, ClassVar, overload
from javax.xml.namespace.QName import QName

class DatatypeConstants:
    APRIL: ClassVar[int]
    AUGUST: ClassVar[int]
    DATE: ClassVar[QName]
    DATETIME: ClassVar[QName]
    DAYS: ClassVar["Field"]
    DECEMBER: ClassVar[int]
    DURATION: ClassVar[QName]
    DURATION_DAYTIME: ClassVar[QName]
    DURATION_YEARMONTH: ClassVar[QName]
    EQUAL: ClassVar[int]
    FEBRUARY: ClassVar[int]
    FIELD_UNDEFINED: ClassVar[int]
    GDAY: ClassVar[QName]
    GMONTH: ClassVar[QName]
    GMONTHDAY: ClassVar[QName]
    GREATER: ClassVar[int]
    GYEAR: ClassVar[QName]
    GYEARMONTH: ClassVar[QName]
    HOURS: ClassVar["Field"]
    INDETERMINATE: ClassVar[int]
    JANUARY: ClassVar[int]
    JULY: ClassVar[int]
    JUNE: ClassVar[int]
    LESSER: ClassVar[int]
    MARCH: ClassVar[int]
    MAX_TIMEZONE_OFFSET: ClassVar[int]
    MAY: ClassVar[int]
    MINUTES: ClassVar["Field"]
    MIN_TIMEZONE_OFFSET: ClassVar[int]
    MONTHS: ClassVar["Field"]
    NOVEMBER: ClassVar[int]
    OCTOBER: ClassVar[int]
    SECONDS: ClassVar["Field"]
    SEPTEMBER: ClassVar[int]
    TIME: ClassVar[QName]
    YEARS: ClassVar["Field"]

    class Field:
        def toString(self) -> str: ...
        def getId(self) -> int: ...
