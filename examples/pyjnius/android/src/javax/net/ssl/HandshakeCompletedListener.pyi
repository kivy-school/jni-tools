from typing import Any, ClassVar, overload
from javax.net.ssl.HandshakeCompletedEvent import HandshakeCompletedEvent

class HandshakeCompletedListener:
    def handshakeCompleted(self, p0: HandshakeCompletedEvent) -> None: ...
