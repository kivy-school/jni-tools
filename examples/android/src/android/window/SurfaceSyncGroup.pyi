from typing import Any, ClassVar, overload
from android.view.AttachedSurfaceControl import AttachedSurfaceControl
from java.lang.Runnable import Runnable

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class SurfacePackage:
    """Forward declaration for ``android.view.SurfaceControlViewHost.SurfacePackage``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.view.SurfaceControlViewHost.SurfacePackage')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/view/SurfaceControlViewHost/SurfacePackage
    """
    ...
class Transaction:
    """Forward declaration for ``android.view.SurfaceControl.Transaction``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.view.SurfaceControl.Transaction')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/view/SurfaceControl/Transaction
    """
    ...

class SurfaceSyncGroup:
    def __init__(self, arg0: str) -> None: ...
    def markSyncReady(self) -> None: ...
    @overload
    def add(self, arg0: AttachedSurfaceControl, arg1: Runnable) -> bool: ...
    @overload
    def add(self, arg0: SurfacePackage, arg1: Runnable) -> bool: ...
    def addTransaction(self, arg0: Transaction) -> None: ...
