from typing import Any, ClassVar, overload

class SSLEngineResult:
    @overload
    def __init__(self, p0: Any, p1: Any, p2: int, p3: int) -> None: ...
    @overload
    def __init__(self, p0: Any, p1: Any, p2: int, p3: int, p4: int) -> None: ...
    def sequenceNumber(self) -> int: ...
    def getStatus(self) -> Any: ...
    def toString(self) -> str: ...
    def getHandshakeStatus(self) -> Any: ...
    def bytesConsumed(self) -> int: ...
    def bytesProduced(self) -> int: ...

    class Status:
        BUFFER_UNDERFLOW: ClassVar["Status"]
        BUFFER_OVERFLOW: ClassVar["Status"]
        OK: ClassVar["Status"]
        CLOSED: ClassVar["Status"]
        BUFFER_UNDERFLOW: ClassVar[Any]
        BUFFER_OVERFLOW: ClassVar[Any]
        OK: ClassVar[Any]
        CLOSED: ClassVar[Any]
        @staticmethod
        def values() -> Any: ...
        @staticmethod
        def valueOf(p0: str) -> Any: ...

    class HandshakeStatus:
        NOT_HANDSHAKING: ClassVar["HandshakeStatus"]
        FINISHED: ClassVar["HandshakeStatus"]
        NEED_TASK: ClassVar["HandshakeStatus"]
        NEED_WRAP: ClassVar["HandshakeStatus"]
        NEED_UNWRAP: ClassVar["HandshakeStatus"]
        NEED_UNWRAP_AGAIN: ClassVar["HandshakeStatus"]
        NOT_HANDSHAKING: ClassVar[Any]
        FINISHED: ClassVar[Any]
        NEED_TASK: ClassVar[Any]
        NEED_WRAP: ClassVar[Any]
        NEED_UNWRAP: ClassVar[Any]
        NEED_UNWRAP_AGAIN: ClassVar[Any]
        @staticmethod
        def values() -> Any: ...
        @staticmethod
        def valueOf(p0: str) -> Any: ...
