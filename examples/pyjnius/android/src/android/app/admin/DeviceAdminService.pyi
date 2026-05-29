from typing import Any, ClassVar, overload
from android.content.Intent import Intent
from android.os.IBinder import IBinder

class DeviceAdminService:
    def __init__(self) -> None: ...
    def onBind(self, arg0: Intent) -> IBinder: ...
