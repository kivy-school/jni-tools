from typing import Any, ClassVar, overload
from java.net.SocketOption import SocketOption

class StandardSocketOptions:
    SO_BROADCAST: ClassVar[SocketOption]
    SO_KEEPALIVE: ClassVar[SocketOption]
    SO_SNDBUF: ClassVar[SocketOption]
    SO_RCVBUF: ClassVar[SocketOption]
    SO_REUSEADDR: ClassVar[SocketOption]
    SO_REUSEPORT: ClassVar[SocketOption]
    SO_LINGER: ClassVar[SocketOption]
    IP_TOS: ClassVar[SocketOption]
    IP_MULTICAST_IF: ClassVar[SocketOption]
    IP_MULTICAST_TTL: ClassVar[SocketOption]
    IP_MULTICAST_LOOP: ClassVar[SocketOption]
    TCP_NODELAY: ClassVar[SocketOption]
