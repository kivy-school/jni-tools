from typing import Any, ClassVar, overload
from android.content.Context import Context
from android.content.Intent import Intent

class BootUpReceiver:
    def __init__(self) -> None: ...
    def onReceive(self, arg0: Context, arg1: Intent) -> None: ...
