from typing import Any, ClassVar, overload

class KeyRep:
    def __init__(self, p0: Any, p1: str, p2: str, p3: Any) -> None: ...

    class Type:
        SECRET: ClassVar["Type"]
        PUBLIC: ClassVar["Type"]
        PRIVATE: ClassVar["Type"]
        SECRET: ClassVar[Any]
        PUBLIC: ClassVar[Any]
        PRIVATE: ClassVar[Any]
        @staticmethod
        def values() -> Any: ...
        @staticmethod
        def valueOf(p0: str) -> Any: ...
