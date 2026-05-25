from typing import Any, ClassVar, overload
from android.content.Context import Context
from android.content.Intent import Intent

class FCMIntentJobService:
    BUNDLE_EXTRA: ClassVar[str]
    def __init__(self) -> None: ...
    def onHandleWork(self, arg0: Intent) -> None: ...
    @staticmethod
    def enqueueWork(arg0: Context, arg1: Intent) -> None: ...
