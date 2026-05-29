from typing import Any, ClassVar, overload
from java.net.InetAddress import InetAddress

class HostNameResolver:
    def resolve(self, p0: str) -> InetAddress: ...
