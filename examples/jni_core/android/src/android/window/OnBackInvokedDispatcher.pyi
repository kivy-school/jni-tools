from typing import Any, ClassVar, overload
from android.window.OnBackInvokedCallback import OnBackInvokedCallback

class OnBackInvokedDispatcher:
    PRIORITY_DEFAULT: ClassVar[int]
    PRIORITY_OVERLAY: ClassVar[int]
    PRIORITY_SYSTEM_NAVIGATION_OBSERVER: ClassVar[int]
    def unregisterOnBackInvokedCallback(self, p0: OnBackInvokedCallback) -> None: ...
    def registerOnBackInvokedCallback(self, p0: int, p1: OnBackInvokedCallback) -> None: ...
