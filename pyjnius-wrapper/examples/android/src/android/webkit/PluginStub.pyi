from typing import Any, ClassVar, overload
from android.content.Context import Context
from android.view.View import View

class PluginStub:
    def getEmbeddedView(self, arg0: int, arg1: Context) -> View: ...
    def getFullScreenView(self, arg0: int, arg1: Context) -> View: ...
