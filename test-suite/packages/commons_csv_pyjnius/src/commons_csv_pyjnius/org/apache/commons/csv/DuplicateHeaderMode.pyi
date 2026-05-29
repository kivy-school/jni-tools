from typing import Any, ClassVar, overload

class DuplicateHeaderMode:
    ALLOW_ALL: ClassVar["DuplicateHeaderMode"]
    ALLOW_EMPTY: ClassVar["DuplicateHeaderMode"]
    DISALLOW: ClassVar["DuplicateHeaderMode"]
    ALLOW_ALL: ClassVar["DuplicateHeaderMode"]
    ALLOW_EMPTY: ClassVar["DuplicateHeaderMode"]
    DISALLOW: ClassVar["DuplicateHeaderMode"]
    @staticmethod
    def values() -> Any: ...
    @staticmethod
    def valueOf(p0: str) -> "DuplicateHeaderMode": ...
