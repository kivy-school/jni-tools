from typing import Any, ClassVar, overload

class AppEventListener:
    def onAppEvent(self, arg0: str, arg1: str) -> None: ...
