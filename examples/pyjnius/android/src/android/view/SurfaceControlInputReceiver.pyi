from typing import Any, ClassVar, overload
from android.view.InputEvent import InputEvent

class SurfaceControlInputReceiver:
    def onInputEvent(self, arg0: InputEvent) -> bool: ...
