from typing import Any, ClassVar, overload

class CoreConnectionPNames:
    CONNECTION_TIMEOUT: ClassVar[str]
    MAX_HEADER_COUNT: ClassVar[str]
    MAX_LINE_LENGTH: ClassVar[str]
    SOCKET_BUFFER_SIZE: ClassVar[str]
    SO_LINGER: ClassVar[str]
    SO_TIMEOUT: ClassVar[str]
    STALE_CONNECTION_CHECK: ClassVar[str]
    TCP_NODELAY: ClassVar[str]
