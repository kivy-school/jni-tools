from typing import Any, ClassVar, overload
from java.net.SocketImpl import SocketImpl

class SocketImplFactory:
    def createSocketImpl(self) -> SocketImpl: ...
