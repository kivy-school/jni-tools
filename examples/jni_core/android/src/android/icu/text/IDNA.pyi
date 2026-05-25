from typing import Any, ClassVar, overload
from java.lang.StringBuilder import StringBuilder

class IDNA:
    CHECK_BIDI: ClassVar[int]
    CHECK_CONTEXTJ: ClassVar[int]
    CHECK_CONTEXTO: ClassVar[int]
    DEFAULT: ClassVar[int]
    NONTRANSITIONAL_TO_ASCII: ClassVar[int]
    NONTRANSITIONAL_TO_UNICODE: ClassVar[int]
    USE_STD3_RULES: ClassVar[int]
    @staticmethod
    def getUTS46Instance(p0: int) -> "IDNA": ...
    def labelToASCII(self, p0: str, p1: StringBuilder, p2: Any) -> StringBuilder: ...
    def labelToUnicode(self, p0: str, p1: StringBuilder, p2: Any) -> StringBuilder: ...
    def nameToASCII(self, p0: str, p1: StringBuilder, p2: Any) -> StringBuilder: ...
    def nameToUnicode(self, p0: str, p1: StringBuilder, p2: Any) -> StringBuilder: ...

    class Info:
        def __init__(self) -> None: ...
        def hasErrors(self) -> bool: ...
        def isTransitionalDifferent(self) -> bool: ...
        def getErrors(self) -> set: ...

    class Error:
        EMPTY_LABEL: ClassVar["Error"]
        LABEL_TOO_LONG: ClassVar["Error"]
        DOMAIN_NAME_TOO_LONG: ClassVar["Error"]
        LEADING_HYPHEN: ClassVar["Error"]
        TRAILING_HYPHEN: ClassVar["Error"]
        HYPHEN_3_4: ClassVar["Error"]
        LEADING_COMBINING_MARK: ClassVar["Error"]
        DISALLOWED: ClassVar["Error"]
        PUNYCODE: ClassVar["Error"]
        LABEL_HAS_DOT: ClassVar["Error"]
        INVALID_ACE_LABEL: ClassVar["Error"]
        BIDI: ClassVar["Error"]
        CONTEXTJ: ClassVar["Error"]
        CONTEXTO_PUNCTUATION: ClassVar["Error"]
        CONTEXTO_DIGITS: ClassVar["Error"]
        EMPTY_LABEL: ClassVar[Any]
        LABEL_TOO_LONG: ClassVar[Any]
        DOMAIN_NAME_TOO_LONG: ClassVar[Any]
        LEADING_HYPHEN: ClassVar[Any]
        TRAILING_HYPHEN: ClassVar[Any]
        HYPHEN_3_4: ClassVar[Any]
        LEADING_COMBINING_MARK: ClassVar[Any]
        DISALLOWED: ClassVar[Any]
        PUNYCODE: ClassVar[Any]
        LABEL_HAS_DOT: ClassVar[Any]
        INVALID_ACE_LABEL: ClassVar[Any]
        BIDI: ClassVar[Any]
        CONTEXTJ: ClassVar[Any]
        CONTEXTO_PUNCTUATION: ClassVar[Any]
        CONTEXTO_DIGITS: ClassVar[Any]
        @staticmethod
        def values() -> Any: ...
        @staticmethod
        def valueOf(p0: str) -> Any: ...
