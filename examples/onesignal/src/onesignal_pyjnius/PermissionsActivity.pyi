from typing import Any, ClassVar, overload
from android.content.Intent import Intent
from android.os.Bundle import Bundle

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class PermissionCallback:
    """Forward declaration for ``com.onesignal.PermissionsActivity.PermissionCallback``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('com.onesignal.PermissionsActivity.PermissionCallback')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.
    """
    ...

class PermissionsActivity:
    def __init__(self) -> None: ...
    @staticmethod
    def registerAsCallback(arg0: str, arg1: PermissionCallback) -> None: ...
    def onCreate(self, arg0: Bundle) -> None: ...
    def onNewIntent(self, arg0: Intent) -> None: ...
    def onRequestPermissionsResult(self, arg0: int, arg1: list[str], arg2: list[int]) -> None: ...
