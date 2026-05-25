from typing import Any, ClassVar, overload

class OnNmeaMessageListener:
    def onNmeaMessage(self, arg0: str, arg1: int) -> None: ...
