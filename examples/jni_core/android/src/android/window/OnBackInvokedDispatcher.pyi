from typing import Any, ClassVar, overload
from android.window.OnBackInvokedCallback import OnBackInvokedCallback

class OnBackInvokedDispatcher:
    PRIORITY_DEFAULT: ClassVar[int]
    PRIORITY_OVERLAY: ClassVar[int]
    def registerOnBackInvokedCallback(self, p0: int, p1: OnBackInvokedCallback) -> None: ...
    def unregisterOnBackInvokedCallback(self, p0: OnBackInvokedCallback) -> None: ...
