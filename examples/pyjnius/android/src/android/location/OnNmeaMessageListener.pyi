from typing import Any, ClassVar, overload

class OnNmeaMessageListener:
    def onNmeaMessage(self, p0: str, p1: int) -> None: ...
