from typing import Any, ClassVar, overload

class QuicException:
    ERROR_ADDRESS_UNREACHABLE: ClassVar[int]
    ERROR_CONNECTION_CLOSED: ClassVar[int]
    ERROR_CONNECTION_REFUSED: ClassVar[int]
    ERROR_CONNECTION_RESET: ClassVar[int]
    ERROR_CONNECTION_TIMED_OUT: ClassVar[int]
    ERROR_HOSTNAME_NOT_RESOLVED: ClassVar[int]
    ERROR_INTERNET_DISCONNECTED: ClassVar[int]
    ERROR_NETWORK_CHANGED: ClassVar[int]
    ERROR_OTHER: ClassVar[int]
    ERROR_QUIC_PROTOCOL_FAILED: ClassVar[int]
    ERROR_TIMED_OUT: ClassVar[int]
