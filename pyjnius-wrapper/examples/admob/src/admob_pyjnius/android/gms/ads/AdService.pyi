from typing import Any, ClassVar, overload
from android.content.Intent import Intent

class AdService:
    CLASS_NAME: ClassVar[str]
    def __init__(self) -> None: ...
    def onHandleIntent(self, arg0: Intent) -> None: ...
