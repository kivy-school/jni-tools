from typing import Any, ClassVar, overload
from javax.net.ssl.SSLEngine import SSLEngine

class SSLEngines:
    @staticmethod
    def isSupportedEngine(p0: SSLEngine) -> bool: ...
    @staticmethod
    def setUseSessionTickets(p0: SSLEngine, p1: bool) -> None: ...
    @staticmethod
    def exportKeyingMaterial(p0: SSLEngine, p1: str, p2: Any, p3: int) -> Any: ...
