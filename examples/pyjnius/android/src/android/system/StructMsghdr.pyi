from typing import Any, ClassVar, overload
from java.net.SocketAddress import SocketAddress

class StructMsghdr:
    msg_control: Any
    msg_flags: int
    msg_iov: Any
    msg_name: SocketAddress
    def __init__(self, p0: SocketAddress, p1: Any, p2: Any, p3: int) -> None: ...
