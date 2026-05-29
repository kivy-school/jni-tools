from typing import Any, ClassVar, overload
from android.content.ComponentName import ComponentName
from android.content.Context import Context

class Badger:
    def executeBadge(self, arg0: Context, arg1: ComponentName, arg2: int) -> None: ...
    def getSupportLaunchers(self) -> list: ...
