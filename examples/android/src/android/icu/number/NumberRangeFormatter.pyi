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
    def withLocale(arg0: Locale) -> LocalizedNumberRangeFormatter: ...
    @overload
    @staticmethod
    def withLocale(arg0: ULocale) -> LocalizedNumberRangeFormatter: ...

    class RangeCollapse:
        AUTO: ClassVar["RangeCollapse"]
        NONE: ClassVar["RangeCollapse"]
        UNIT: ClassVar["RangeCollapse"]
        ALL: ClassVar["RangeCollapse"]
        @staticmethod
        def values() -> list["RangeCollapse"]: ...
        @staticmethod
        def valueOf(arg0: str) -> "RangeCollapse": ...

    class RangeIdentityFallback:
        SINGLE_VALUE: ClassVar["RangeIdentityFallback"]
        APPROXIMATELY_OR_SINGLE_VALUE: ClassVar["RangeIdentityFallback"]
        APPROXIMATELY: ClassVar["RangeIdentityFallback"]
        RANGE: ClassVar["RangeIdentityFallback"]
        @staticmethod
        def values() -> list["RangeIdentityFallback"]: ...
        @staticmethod
        def valueOf(arg0: str) -> "RangeIdentityFallback": ...

    class RangeIdentityResult:
        EQUAL_BEFORE_ROUNDING: ClassVar["RangeIdentityResult"]
        EQUAL_AFTER_ROUNDING: ClassVar["RangeIdentityResult"]
        NOT_EQUAL: ClassVar["RangeIdentityResult"]
        @staticmethod
        def values() -> list["RangeIdentityResult"]: ...
        @staticmethod
        def valueOf(arg0: str) -> "RangeIdentityResult": ...
