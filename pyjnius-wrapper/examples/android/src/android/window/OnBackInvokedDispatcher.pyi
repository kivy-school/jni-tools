from typing import Any, ClassVar, overload
from android.window.OnBackInvokedCallback import OnBackInvokedCallback

class OnBackInvokedDispatcher:
    PRIORITY_DEFAULT: ClassVar[int]
    PRIORITY_OVERLAY: ClassVar[int]
    def registerOnBackInvokedCallback(self, arg0: int, arg1: OnBackInvokedCallback) -> None: ...
    def unregisterOnBackInvokedCallback(self, arg0: OnBackInvokedCallback) -> None: ...
