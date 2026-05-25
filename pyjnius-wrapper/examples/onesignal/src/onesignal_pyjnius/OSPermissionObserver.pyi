from typing import Any, ClassVar, overload
from OSPermissionStateChanges import OSPermissionStateChanges

class OSPermissionObserver:
    def onOSPermissionChanged(self, arg0: OSPermissionStateChanges) -> None: ...
