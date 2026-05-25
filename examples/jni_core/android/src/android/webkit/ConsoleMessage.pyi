from typing import Any, ClassVar, overload

class ConsoleMessage:
    def __init__(self, p0: str, p1: str, p2: int, p3: Any) -> None: ...
    def sourceId(self) -> str: ...
    def messageLevel(self) -> Any: ...
    def lineNumber(self) -> int: ...
    def message(self) -> str: ...

    class MessageLevel:
        TIP: ClassVar["MessageLevel"]
        LOG: ClassVar["MessageLevel"]
        WARNING: ClassVar["MessageLevel"]
        ERROR: ClassVar["MessageLevel"]
        DEBUG: ClassVar["MessageLevel"]
        TIP: ClassVar[Any]
        LOG: ClassVar[Any]
        WARNING: ClassVar[Any]
        ERROR: ClassVar[Any]
        DEBUG: ClassVar[Any]
        @staticmethod
        def values() -> Any: ...
        @staticmethod
        def valueOf(p0: str) -> Any: ...
