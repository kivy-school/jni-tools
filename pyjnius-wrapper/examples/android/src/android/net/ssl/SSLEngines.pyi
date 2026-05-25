from typing import Any, ClassVar, overload
from javax.net.ssl.SSLEngine import SSLEngine

class SSLEngines:
    @staticmethod
    def isSupportedEngine(arg0: SSLEngine) -> bool: ...
    @staticmethod
    def setUseSessionTickets(arg0: SSLEngine, arg1: bool) -> None: ...
    @staticmethod
    def exportKeyingMaterial(arg0: SSLEngine, arg1: str, arg2: list[int], arg3: int) -> list[int]: ...
