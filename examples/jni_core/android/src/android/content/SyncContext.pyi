from typing import Any, ClassVar, overload
from android.content.SyncResult import SyncResult
from android.os.IBinder import IBinder

class SyncContext:
    def getSyncContextBinder(self) -> IBinder: ...
    def onFinished(self, p0: SyncResult) -> None: ...
