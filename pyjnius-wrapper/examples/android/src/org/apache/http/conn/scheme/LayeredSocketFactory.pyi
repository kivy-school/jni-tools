from typing import Any, ClassVar, overload
from java.net.Socket import Socket

class LayeredSocketFactory:
    def createSocket(self, arg0: Socket, arg1: str, arg2: int, arg3: bool) -> Socket: ...
