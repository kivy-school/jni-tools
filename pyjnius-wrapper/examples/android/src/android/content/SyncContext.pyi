from typing import Any, ClassVar, overload
from android.content.SyncResult import SyncResult
from android.os.IBinder import IBinder

class SyncContext:
    def onFinished(self, arg0: SyncResult) -> None: ...
    def getSyncContextBinder(self) -> IBinder: ...
