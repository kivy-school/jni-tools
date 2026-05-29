from typing import Any, ClassVar, overload
from java.net.InetAddress import InetAddress

class IkeTrafficSelector:
    endPort: int
    endingAddress: InetAddress
    startPort: int
    startingAddress: InetAddress
    def __init__(self, p0: int, p1: int, p2: InetAddress, p3: InetAddress) -> None: ...
    def equals(self, p0: Any) -> bool: ...
    def hashCode(self) -> int: ...
