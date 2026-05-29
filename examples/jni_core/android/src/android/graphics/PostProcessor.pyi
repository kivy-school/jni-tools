from typing import Any, ClassVar, overload
from android.graphics.Canvas import Canvas

class PostProcessor:
    def onPostProcess(self, p0: Canvas) -> int: ...
