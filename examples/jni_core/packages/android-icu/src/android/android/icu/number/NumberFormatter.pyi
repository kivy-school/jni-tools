from typing import Any, ClassVar, overload
from android.icu.number.LocalizedNumberFormatter import LocalizedNumberFormatter
from android.icu.number.UnlocalizedNumberFormatter import UnlocalizedNumberFormatter
from android.icu.util.ULocale import ULocale
from java.util.Locale import Locale

class NumberFormatter:
    @overload
    @staticmethod
    def withLocale(p0: Locale) -> LocalizedNumberFormatter: ...
    @overload
    @staticmethod
    def withLocale(p0: ULocale) -> LocalizedNumberFormatter: ...
    @staticmethod
    def with_() -> UnlocalizedNumberFormatter: ...

    class UnitWidth:
        FORMAL: ClassVar["UnitWidth"]
        FULL_NAME: ClassVar["UnitWidth"]
        HIDDEN: ClassVar["UnitWidth"]
        ISO_CODE: ClassVar["UnitWidth"]
        NARROW: ClassVar["UnitWidth"]
        SHORT: ClassVar["UnitWidth"]
        VARIANT: ClassVar["UnitWidth"]
        FORMAL: ClassVar[Any]
        FULL_NAME: ClassVar[Any]
        HIDDEN: ClassVar[Any]
        ISO_CODE: ClassVar[Any]
        NARROW: ClassVar[Any]
        SHORT: ClassVar[Any]
        VARIANT: ClassVar[Any]
        @staticmethod
        def values() -> Any: ...
        @staticmethod
        def valueOf(p0: str) -> Any: ...

    class TrailingZeroDisplay:
        AUTO: ClassVar["TrailingZeroDisplay"]
        HIDE_IF_WHOLE: ClassVar["TrailingZeroDisplay"]
        AUTO: ClassVar[Any]
        HIDE_IF_WHOLE: ClassVar[Any]
        @staticmethod
        def values() -> Any: ...
        @staticmethod
        def valueOf(p0: str) -> Any: ...

    class SignDisplay:
        ACCOUNTING: ClassVar["SignDisplay"]
        ACCOUNTING_ALWAYS: ClassVar["SignDisplay"]
        ACCOUNTING_EXCEPT_ZERO: ClassVar["SignDisplay"]
        ACCOUNTING_NEGATIVE: ClassVar["SignDisplay"]
        ALWAYS: ClassVar["SignDisplay"]
        AUTO: ClassVar["SignDisplay"]
        EXCEPT_ZERO: ClassVar["SignDisplay"]
        NEGATIVE: ClassVar["SignDisplay"]
        NEVER: ClassVar["SignDisplay"]
        ACCOUNTING: ClassVar[Any]
        ACCOUNTING_ALWAYS: ClassVar[Any]
        ACCOUNTING_EXCEPT_ZERO: ClassVar[Any]
        ACCOUNTING_NEGATIVE: ClassVar[Any]
        ALWAYS: ClassVar[Any]
        AUTO: ClassVar[Any]
        EXCEPT_ZERO: ClassVar[Any]
        NEGATIVE: ClassVar[Any]
        NEVER: ClassVar[Any]
        @staticmethod
        def values() -> Any: ...
        @staticmethod
        def valueOf(p0: str) -> Any: ...

    class RoundingPriority:
        RELAXED: ClassVar["RoundingPriority"]
        STRICT: ClassVar["RoundingPriority"]
        RELAXED: ClassVar[Any]
        STRICT: ClassVar[Any]
        @staticmethod
        def values() -> Any: ...
        @staticmethod
        def valueOf(p0: str) -> Any: ...

    class GroupingStrategy:
        AUTO: ClassVar["GroupingStrategy"]
        MIN2: ClassVar["GroupingStrategy"]
        OFF: ClassVar["GroupingStrategy"]
        ON_ALIGNED: ClassVar["GroupingStrategy"]
        THOUSANDS: ClassVar["GroupingStrategy"]
        AUTO: ClassVar[Any]
        MIN2: ClassVar[Any]
        OFF: ClassVar[Any]
        ON_ALIGNED: ClassVar[Any]
        THOUSANDS: ClassVar[Any]
        @staticmethod
        def values() -> Any: ...
        @staticmethod
        def valueOf(p0: str) -> Any: ...

    class DecimalSeparatorDisplay:
        ALWAYS: ClassVar["DecimalSeparatorDisplay"]
        AUTO: ClassVar["DecimalSeparatorDisplay"]
        ALWAYS: ClassVar[Any]
        AUTO: ClassVar[Any]
        @staticmethod
        def values() -> Any: ...
        @staticmethod
        def valueOf(p0: str) -> Any: ...
