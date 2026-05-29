from typing import Any, ClassVar, overload

class SipErrorCode:
    CLIENT_ERROR: ClassVar[int]
    CROSS_DOMAIN_AUTHENTICATION: ClassVar[int]
    DATA_CONNECTION_LOST: ClassVar[int]
    INVALID_CREDENTIALS: ClassVar[int]
    INVALID_REMOTE_URI: ClassVar[int]
    IN_PROGRESS: ClassVar[int]
    NO_ERROR: ClassVar[int]
    PEER_NOT_REACHABLE: ClassVar[int]
    SERVER_ERROR: ClassVar[int]
    SERVER_UNREACHABLE: ClassVar[int]
    SOCKET_ERROR: ClassVar[int]
    TIME_OUT: ClassVar[int]
    TRANSACTION_TERMINTED: ClassVar[int]
    @staticmethod
    def toString(p0: int) -> str: ...
