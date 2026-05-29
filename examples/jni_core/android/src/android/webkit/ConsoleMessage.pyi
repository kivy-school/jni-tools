from typing import Any, ClassVar, overload

class ConsoleMessage:
    def __init__(self, p0: str, p1: str, p2: int, p3: Any) -> None: ...
    def sourceId(self) -> str: ...
    def messageLevel(self) -> Any: ...
    def lineNumber(self) -> int: ...
    def message(self) -> str: ...

    class MessageLevel:
        DEBUG: ClassVar["MessageLevel"]
        ERROR: ClassVar["MessageLevel"]
        LOG: ClassVar["MessageLevel"]
        TIP: ClassVar["MessageLevel"]
        WARNING: ClassVar["MessageLevel"]
        DEBUG: ClassVar[Any]
        ERROR: ClassVar[Any]
        LOG: ClassVar[Any]
        TIP: ClassVar[Any]
        WARNING: ClassVar[Any]
        @staticmethod
        def values() -> Any: ...
        @staticmethod
        def valueOf(p0: str) -> Any: ...
