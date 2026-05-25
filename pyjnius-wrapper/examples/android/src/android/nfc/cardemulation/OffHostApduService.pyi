from typing import Any, ClassVar, overload
from android.content.Intent import Intent
from android.os.IBinder import IBinder

class OffHostApduService:
    SERVICE_INTERFACE: ClassVar[str]
    SERVICE_META_DATA: ClassVar[str]
    def __init__(self) -> None: ...
    def onBind(self, arg0: Intent) -> IBinder: ...
