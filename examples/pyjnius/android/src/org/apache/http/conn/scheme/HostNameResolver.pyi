from typing import Any, ClassVar, overload
from java.net.InetAddress import InetAddress

class HostNameResolver:
    def resolve(self, arg0: str) -> InetAddress: ...
