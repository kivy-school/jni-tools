from typing import Any, ClassVar, overload

class QuoteMode:
    ALL: ClassVar["QuoteMode"]
    ALL_NON_NULL: ClassVar["QuoteMode"]
    MINIMAL: ClassVar["QuoteMode"]
    NON_NUMERIC: ClassVar["QuoteMode"]
    NONE: ClassVar["QuoteMode"]
    ALL: ClassVar["QuoteMode"]
    ALL_NON_NULL: ClassVar["QuoteMode"]
    MINIMAL: ClassVar["QuoteMode"]
    NON_NUMERIC: ClassVar["QuoteMode"]
    NONE: ClassVar["QuoteMode"]
    @staticmethod
    def values() -> Any: ...
    @staticmethod
    def valueOf(p0: str) -> "QuoteMode": ...
