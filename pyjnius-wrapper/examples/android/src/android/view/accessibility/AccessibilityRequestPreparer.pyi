from typing import Any, ClassVar, overload
from android.os.Bundle import Bundle
from android.os.Message import Message
from android.view.View import View

class AccessibilityRequestPreparer:
    REQUEST_TYPE_EXTRA_DATA: ClassVar[int]
    def __init__(self, arg0: View, arg1: int) -> None: ...
    def onPrepareExtraData(self, arg0: int, arg1: str, arg2: Bundle, arg3: Message) -> None: ...
    def getView(self) -> View: ...
