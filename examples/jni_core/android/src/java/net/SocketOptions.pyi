from typing import Any, ClassVar, overload

class SocketOptions:
    TCP_NODELAY: ClassVar[int]
    SO_BINDADDR: ClassVar[int]
    SO_REUSEADDR: ClassVar[int]
    SO_REUSEPORT: ClassVar[int]
    SO_BROADCAST: ClassVar[int]
    IP_MULTICAST_IF: ClassVar[int]
    IP_MULTICAST_IF2: ClassVar[int]
    IP_MULTICAST_LOOP: ClassVar[int]
    IP_TOS: ClassVar[int]
    SO_LINGER: ClassVar[int]
    SO_TIMEOUT: ClassVar[int]
    SO_SNDBUF: ClassVar[int]
    SO_RCVBUF: ClassVar[int]
    SO_KEEPALIVE: ClassVar[int]
    SO_OOBINLINE: ClassVar[int]
    def setOption(self, p0: int, p1: Any) -> None: ...
    def getOption(self, p0: int) -> Any: ...
