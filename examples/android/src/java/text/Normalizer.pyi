from typing import Any, ClassVar, overload

class Normalizer:
    @staticmethod
    def normalize(arg0: str, arg1: "Form") -> str: ...
    @staticmethod
    def isNormalized(arg0: str, arg1: "Form") -> bool: ...

    class Form:
        NFD: ClassVar["Form"]
        NFC: ClassVar["Form"]
        NFKD: ClassVar["Form"]
        NFKC: ClassVar["Form"]
        @staticmethod
        def values() -> list["Form"]: ...
        @staticmethod
        def valueOf(arg0: str) -> "Form": ...
