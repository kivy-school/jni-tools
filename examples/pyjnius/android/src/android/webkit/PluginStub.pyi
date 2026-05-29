from typing import Any, ClassVar, overload
from android.content.Context import Context
from android.view.View import View

class PluginStub:
    def getFullScreenView(self, p0: int, p1: Context) -> View: ...
    def getEmbeddedView(self, p0: int, p1: Context) -> View: ...
