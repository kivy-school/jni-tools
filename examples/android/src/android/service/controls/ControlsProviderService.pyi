from typing import Any, ClassVar, overload
from android.content.ComponentName import ComponentName
from android.content.Context import Context
from android.content.Intent import Intent
from android.os.IBinder import IBinder
from android.service.controls.Control import Control
from android.service.controls.actions.ControlAction import ControlAction
from java.util.function.Consumer import Consumer

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Publisher:
    """Forward declaration for ``java.util.concurrent.Flow.Publisher``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('java.util.concurrent.Flow.Publisher')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Flow/Publisher.html
    """
    ...

class ControlsProviderService:
    CONTROLS_SURFACE_ACTIVITY_PANEL: ClassVar[int]
    CONTROLS_SURFACE_DREAM: ClassVar[int]
    EXTRA_CONTROLS_SURFACE: ClassVar[str]
    EXTRA_LOCKSCREEN_ALLOW_TRIVIAL_CONTROLS: ClassVar[str]
    META_DATA_PANEL_ACTIVITY: ClassVar[str]
    SERVICE_CONTROLS: ClassVar[str]
    TAG: ClassVar[str]
    def __init__(self) -> None: ...
    def createPublisherForAllAvailable(self) -> Publisher: ...
    def createPublisherForSuggested(self) -> Publisher: ...
    def createPublisherFor(self, arg0: list) -> Publisher: ...
    def performControlAction(self, arg0: str, arg1: ControlAction, arg2: Consumer) -> None: ...
    def onBind(self, arg0: Intent) -> IBinder: ...
    def onUnbind(self, arg0: Intent) -> bool: ...
    @staticmethod
    def requestAddControl(arg0: Context, arg1: ComponentName, arg2: Control) -> None: ...
