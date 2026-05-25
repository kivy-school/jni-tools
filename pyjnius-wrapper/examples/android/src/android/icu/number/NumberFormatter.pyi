from typing import Any, ClassVar, overload
from android.icu.number.LocalizedNumberFormatter import LocalizedNumberFormatter
from android.icu.number.UnlocalizedNumberFormatter import UnlocalizedNumberFormatter
from android.icu.util.ULocale import ULocale
from java.util.Locale import Locale

class NumberFormatter:
    @staticmethod
    def with_() -> UnlocalizedNumberFormatter: ...
    @overload
    @staticmethod
    def withLocale(arg0: Locale) -> LocalizedNumberFormatter: ...
    @overload
    @staticmethod
    def withLocale(arg0: ULocale) -> LocalizedNumberFormatter: ...

    class DecimalSeparatorDisplay:
        AUTO: ClassVar["DecimalSeparatorDisplay"]
        ALWAYS: ClassVar["DecimalSeparatorDisplay"]
        @staticmethod
        def values() -> list["DecimalSeparatorDisplay"]: ...
        @staticmethod
        def valueOf(arg0: str) -> "DecimalSeparatorDisplay": ...

    class GroupingStrategy:
        OFF: ClassVar["GroupingStrategy"]
        MIN2: ClassVar["GroupingStrategy"]
        AUTO: ClassVar["GroupingStrategy"]
        ON_ALIGNED: ClassVar["GroupingStrategy"]
        THOUSANDS: ClassVar["GroupingStrategy"]
        @staticmethod
        def values() -> list["GroupingStrategy"]: ...
        @staticmethod
        def valueOf(arg0: str) -> "GroupingStrategy": ...

    class RoundingPriority:
        RELAXED: ClassVar["RoundingPriority"]
        STRICT: ClassVar["RoundingPriority"]
        @staticmethod
        def values() -> list["RoundingPriority"]: ...
        @staticmethod
        def valueOf(arg0: str) -> "RoundingPriority": ...

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
        @staticmethod
        def values() -> list["SignDisplay"]: ...
        @staticmethod
        def valueOf(arg0: str) -> "SignDisplay": ...

    class TrailingZeroDisplay:
        AUTO: ClassVar["TrailingZeroDisplay"]
        HIDE_IF_WHOLE: ClassVar["TrailingZeroDisplay"]
        @staticmethod
        def values() -> list["TrailingZeroDisplay"]: ...
        @staticmethod
        def valueOf(arg0: str) -> "TrailingZeroDisplay": ...

    class UnitWidth:
        NARROW: ClassVar["UnitWidth"]
        SHORT: ClassVar["UnitWidth"]
        FULL_NAME: ClassVar["UnitWidth"]
        ISO_CODE: ClassVar["UnitWidth"]
        FORMAL: ClassVar["UnitWidth"]
        VARIANT: ClassVar["UnitWidth"]
        HIDDEN: ClassVar["UnitWidth"]
        @staticmethod
        def values() -> list["UnitWidth"]: ...
        @staticmethod
        def valueOf(arg0: str) -> "UnitWidth": ...
