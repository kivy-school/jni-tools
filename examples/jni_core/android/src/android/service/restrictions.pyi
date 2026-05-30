from typing import Any, ClassVar, overload
from android.content.Context import Context
from android.content.Intent import Intent
from android.os.PersistableBundle import PersistableBundle

class RestrictionsReceiver:
    def __init__(self) -> None: ...
    def onRequestPermission(self, p0: Context, p1: str, p2: str, p3: str, p4: PersistableBundle) -> None: ...
    def onReceive(self, p0: Context, p1: Intent) -> None: ...

