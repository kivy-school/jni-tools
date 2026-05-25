from typing import Any, ClassVar, overload
from android.content.Context import Context

class OnContextChangedListener:
    def onContextChanged(self, arg0: Context) -> None: ...
