from typing import Any, ClassVar, overload
from javax.net.ssl.SSLSocket import SSLSocket

class SSLSockets:
    @staticmethod
    def isSupportedSocket(p0: SSLSocket) -> bool: ...
    @staticmethod
    def setUseSessionTickets(p0: SSLSocket, p1: bool) -> None: ...
    @staticmethod
    def exportKeyingMaterial(p0: SSLSocket, p1: str, p2: Any, p3: int) -> Any: ...
