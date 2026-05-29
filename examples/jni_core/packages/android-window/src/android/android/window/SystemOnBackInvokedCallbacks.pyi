from typing import Any, ClassVar, overload
from android.app.Activity import Activity
from android.window.OnBackInvokedCallback import OnBackInvokedCallback

class SystemOnBackInvokedCallbacks:
    @staticmethod
    def finishAndRemoveTaskCallback(p0: Activity) -> OnBackInvokedCallback: ...
    @staticmethod
    def moveTaskToBackCallback(p0: Activity) -> OnBackInvokedCallback: ...
