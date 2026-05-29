from typing import Any, ClassVar, overload

class RetentionPolicy:
    SOURCE: ClassVar["RetentionPolicy"]
    CLASS: ClassVar["RetentionPolicy"]
    RUNTIME: ClassVar["RetentionPolicy"]
    SOURCE: ClassVar["RetentionPolicy"]
    CLASS: ClassVar["RetentionPolicy"]
    RUNTIME: ClassVar["RetentionPolicy"]
    @staticmethod
    def values() -> Any: ...
    @staticmethod
    def valueOf(p0: str) -> "RetentionPolicy": ...
