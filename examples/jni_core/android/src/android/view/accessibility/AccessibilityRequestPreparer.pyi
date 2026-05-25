from typing import Any, ClassVar, overload
from android.os.Bundle import Bundle
from android.os.Message import Message
from android.view.View import View

class AccessibilityRequestPreparer:
    REQUEST_TYPE_EXTRA_DATA: ClassVar[int]
    def __init__(self, p0: View, p1: int) -> None: ...
    def onPrepareExtraData(self, p0: int, p1: str, p2: Bundle, p3: Message) -> None: ...
    def getView(self) -> View: ...
