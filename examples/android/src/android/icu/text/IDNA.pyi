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
    def getUTS46Instance(arg0: int) -> "IDNA": ...
    def labelToASCII(self, arg0: str, arg1: StringBuilder, arg2: "Info") -> StringBuilder: ...
    def labelToUnicode(self, arg0: str, arg1: StringBuilder, arg2: "Info") -> StringBuilder: ...
    def nameToASCII(self, arg0: str, arg1: StringBuilder, arg2: "Info") -> StringBuilder: ...
    def nameToUnicode(self, arg0: str, arg1: StringBuilder, arg2: "Info") -> StringBuilder: ...

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
        @staticmethod
        def values() -> list["Error"]: ...
        @staticmethod
        def valueOf(arg0: str) -> "Error": ...

    class Info:
        def __init__(self) -> None: ...
        def hasErrors(self) -> bool: ...
        def getErrors(self) -> set: ...
        def isTransitionalDifferent(self) -> bool: ...
