from typing import Any, ClassVar, overload
from android.icu.number.LocalizedNumberRangeFormatter import LocalizedNumberRangeFormatter
from android.icu.number.UnlocalizedNumberRangeFormatter import UnlocalizedNumberRangeFormatter
from android.icu.util.ULocale import ULocale
from java.util.Locale import Locale

class NumberRangeFormatter:
    @staticmethod
    def with_() -> UnlocalizedNumberRangeFormatter: ...
    @overload
    @staticmethod
    def withLocale(p0: Locale) -> LocalizedNumberRangeFormatter: ...
    @overload
    @staticmethod
    def withLocale(p0: ULocale) -> LocalizedNumberRangeFormatter: ...

    class RangeIdentityResult:
        EQUAL_AFTER_ROUNDING: ClassVar["RangeIdentityResult"]
        EQUAL_BEFORE_ROUNDING: ClassVar["RangeIdentityResult"]
        NOT_EQUAL: ClassVar["RangeIdentityResult"]
        EQUAL_AFTER_ROUNDING: ClassVar[Any]
        EQUAL_BEFORE_ROUNDING: ClassVar[Any]
        NOT_EQUAL: ClassVar[Any]
        @staticmethod
        def values() -> Any: ...
        @staticmethod
        def valueOf(p0: str) -> Any: ...

    class RangeIdentityFallback:
        APPROXIMATELY: ClassVar["RangeIdentityFallback"]
        APPROXIMATELY_OR_SINGLE_VALUE: ClassVar["RangeIdentityFallback"]
        RANGE: ClassVar["RangeIdentityFallback"]
        SINGLE_VALUE: ClassVar["RangeIdentityFallback"]
        APPROXIMATELY: ClassVar[Any]
        APPROXIMATELY_OR_SINGLE_VALUE: ClassVar[Any]
        RANGE: ClassVar[Any]
        SINGLE_VALUE: ClassVar[Any]
        @staticmethod
        def values() -> Any: ...
        @staticmethod
        def valueOf(p0: str) -> Any: ...

    class RangeCollapse:
        ALL: ClassVar["RangeCollapse"]
        AUTO: ClassVar["RangeCollapse"]
        NONE: ClassVar["RangeCollapse"]
        UNIT: ClassVar["RangeCollapse"]
        ALL: ClassVar[Any]
        AUTO: ClassVar[Any]
        NONE: ClassVar[Any]
        UNIT: ClassVar[Any]
        @staticmethod
        def values() -> Any: ...
        @staticmethod
        def valueOf(p0: str) -> Any: ...
