from typing import Any, ClassVar, overload
from javax.net.ssl.SSLSocket import SSLSocket

class SSLSockets:
    @staticmethod
    def isSupportedSocket(arg0: SSLSocket) -> bool: ...
    @staticmethod
    def setUseSessionTickets(arg0: SSLSocket, arg1: bool) -> None: ...
    @staticmethod
    def exportKeyingMaterial(arg0: SSLSocket, arg1: str, arg2: list[int], arg3: int) -> list[int]: ...
