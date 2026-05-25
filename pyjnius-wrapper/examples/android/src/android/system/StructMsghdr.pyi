from typing import Any, ClassVar, overload
from android.system.StructCmsghdr import StructCmsghdr
from java.net.SocketAddress import SocketAddress
from java.nio.ByteBuffer import ByteBuffer

class StructMsghdr:
    msg_control: list[StructCmsghdr]
    msg_flags: int
    msg_iov: list[ByteBuffer]
    msg_name: SocketAddress
    def __init__(self, arg0: SocketAddress, arg1: list[ByteBuffer], arg2: list[StructCmsghdr], arg3: int) -> None: ...
