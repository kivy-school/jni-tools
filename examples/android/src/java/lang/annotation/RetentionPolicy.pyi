from typing import Any, ClassVar, overload

class RetentionPolicy:
    SOURCE: ClassVar["RetentionPolicy"]
    CLASS: ClassVar["RetentionPolicy"]
    RUNTIME: ClassVar["RetentionPolicy"]
    @staticmethod
    def values() -> list["RetentionPolicy"]: ...
    @staticmethod
    def valueOf(arg0: str) -> "RetentionPolicy": ...
