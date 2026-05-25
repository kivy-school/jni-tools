from typing import Any, ClassVar, overload
from android.icu.number.LocalizedNumberFormatter import LocalizedNumberFormatter
from android.icu.number.UnlocalizedNumberFormatter import UnlocalizedNumberFormatter
from android.icu.util.ULocale import ULocale
from java.util.Locale import Locale

class NumberFormatter:
    @overload
    @staticmethod
    def withLocale(p0: ULocale) -> LocalizedNumberFormatter: ...
    @overload
    @staticmethod
    def withLocale(p0: Locale) -> LocalizedNumberFormatter: ...
    @staticmethod
    def with_() -> UnlocalizedNumberFormatter: ...

    class UnitWidth:
        NARROW: ClassVar["UnitWidth"]
        SHORT: ClassVar["UnitWidth"]
        FULL_NAME: ClassVar["UnitWidth"]
        ISO_CODE: ClassVar["UnitWidth"]
        FORMAL: ClassVar["UnitWidth"]
        VARIANT: ClassVar["UnitWidth"]
        HIDDEN: ClassVar["UnitWidth"]
        NARROW: ClassVar[Any]
        SHORT: ClassVar[Any]
        FULL_NAME: ClassVar[Any]
        ISO_CODE: ClassVar[Any]
        FORMAL: ClassVar[Any]
        VARIANT: ClassVar[Any]
        HIDDEN: ClassVar[Any]
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
        AUTO: ClassVar["SignDisplay"]
        ALWAYS: ClassVar["SignDisplay"]
        NEVER: ClassVar["SignDisplay"]
        ACCOUNTING: ClassVar["SignDisplay"]
        ACCOUNTING_ALWAYS: ClassVar["SignDisplay"]
        EXCEPT_ZERO: ClassVar["SignDisplay"]
        ACCOUNTING_EXCEPT_ZERO: ClassVar["SignDisplay"]
        NEGATIVE: ClassVar["SignDisplay"]
        ACCOUNTING_NEGATIVE: ClassVar["SignDisplay"]
        AUTO: ClassVar[Any]
        ALWAYS: ClassVar[Any]
        NEVER: ClassVar[Any]
        ACCOUNTING: ClassVar[Any]
        ACCOUNTING_ALWAYS: ClassVar[Any]
        EXCEPT_ZERO: ClassVar[Any]
        ACCOUNTING_EXCEPT_ZERO: ClassVar[Any]
        NEGATIVE: ClassVar[Any]
        ACCOUNTING_NEGATIVE: ClassVar[Any]
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
        OFF: ClassVar["GroupingStrategy"]
        MIN2: ClassVar["GroupingStrategy"]
        AUTO: ClassVar["GroupingStrategy"]
        ON_ALIGNED: ClassVar["GroupingStrategy"]
        THOUSANDS: ClassVar["GroupingStrategy"]
        OFF: ClassVar[Any]
        MIN2: ClassVar[Any]
        AUTO: ClassVar[Any]
        ON_ALIGNED: ClassVar[Any]
        THOUSANDS: ClassVar[Any]
        @staticmethod
        def values() -> Any: ...
        @staticmethod
        def valueOf(p0: str) -> Any: ...

    class DecimalSeparatorDisplay:
        AUTO: ClassVar["DecimalSeparatorDisplay"]
        ALWAYS: ClassVar["DecimalSeparatorDisplay"]
        AUTO: ClassVar[Any]
        ALWAYS: ClassVar[Any]
        @staticmethod
        def values() -> Any: ...
        @staticmethod
        def valueOf(p0: str) -> Any: ...
