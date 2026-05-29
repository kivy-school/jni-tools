from typing import Any, ClassVar, overload
from java.net.InetAddress import InetAddress
from java.net.NetworkInterface import NetworkInterface
from java.nio.channels.MembershipKey import MembershipKey

class MulticastChannel:
    @overload
    def join(self, p0: InetAddress, p1: NetworkInterface) -> MembershipKey: ...
    @overload
    def join(self, p0: InetAddress, p1: NetworkInterface, p2: InetAddress) -> MembershipKey: ...
    def close(self) -> None: ...
