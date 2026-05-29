from typing import Any, ClassVar, overload

class SyncStatusObserver:
    def onStatusChanged(self, p0: int) -> None: ...
