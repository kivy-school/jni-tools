from typing import Any, ClassVar, overload
from java.net.InetAddress import InetAddress

class IkeTrafficSelector:
    endPort: int
    endingAddress: InetAddress
    startPort: int
    startingAddress: InetAddress
    def __init__(self, arg0: int, arg1: int, arg2: InetAddress, arg3: InetAddress) -> None: ...
    def hashCode(self) -> int: ...
    def equals(self, arg0: Any) -> bool: ...
