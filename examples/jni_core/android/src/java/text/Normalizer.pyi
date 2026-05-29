from typing import Any, ClassVar, overload

class Normalizer:
    @staticmethod
    def isNormalized(p0: str, p1: Any) -> bool: ...
    @staticmethod
    def normalize(p0: str, p1: Any) -> str: ...

    class Form:
        NFD: ClassVar["Form"]
        NFC: ClassVar["Form"]
        NFKD: ClassVar["Form"]
        NFKC: ClassVar["Form"]
        NFD: ClassVar[Any]
        NFC: ClassVar[Any]
        NFKD: ClassVar[Any]
        NFKC: ClassVar[Any]
        @staticmethod
        def values() -> Any: ...
        @staticmethod
        def valueOf(p0: str) -> Any: ...
