from typing import Any, ClassVar, overload
from java.net.InetAddress import InetAddress
from java.net.NetworkInterface import NetworkInterface
from java.nio.channels.MembershipKey import MembershipKey

class MulticastChannel:
    def close(self) -> None: ...
    @overload
    def join(self, arg0: InetAddress, arg1: NetworkInterface) -> MembershipKey: ...
    @overload
    def join(self, arg0: InetAddress, arg1: NetworkInterface, arg2: InetAddress) -> MembershipKey: ...
