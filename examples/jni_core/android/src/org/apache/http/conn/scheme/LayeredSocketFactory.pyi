from typing import Any, ClassVar, overload
from java.net.Socket import Socket

class LayeredSocketFactory:
    def createSocket(self, p0: Socket, p1: str, p2: int, p3: bool) -> Socket: ...
