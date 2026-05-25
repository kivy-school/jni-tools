from typing import Any, ClassVar, overload
from android.content.Context import Context
from android.content.Intent import Intent

class MbmsDownloadReceiver:
    def __init__(self) -> None: ...
    def onReceive(self, p0: Context, p1: Intent) -> None: ...
