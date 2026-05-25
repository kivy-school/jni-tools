from typing import Any, ClassVar, overload
from android.content.ComponentName import ComponentName
from android.content.Intent import Intent
from android.content.IntentFilter import IntentFilter
from android.os.IBinder import IBinder

class ChooserTargetService:
    BIND_PERMISSION: ClassVar[str]
    META_DATA_NAME: ClassVar[str]
    SERVICE_INTERFACE: ClassVar[str]
    def __init__(self) -> None: ...
    def onGetChooserTargets(self, arg0: ComponentName, arg1: IntentFilter) -> list: ...
    def onBind(self, arg0: Intent) -> IBinder: ...
