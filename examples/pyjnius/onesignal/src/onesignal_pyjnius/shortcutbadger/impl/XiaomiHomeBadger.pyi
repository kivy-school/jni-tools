from typing import Any, ClassVar, overload
from android.content.ComponentName import ComponentName
from android.content.Context import Context

class XiaomiHomeBadger:
    INTENT_ACTION: ClassVar[str]
    EXTRA_UPDATE_APP_COMPONENT_NAME: ClassVar[str]
    EXTRA_UPDATE_APP_MSG_TEXT: ClassVar[str]
    def __init__(self) -> None: ...
    def executeBadge(self, arg0: Context, arg1: ComponentName, arg2: int) -> None: ...
    def getSupportLaunchers(self) -> list: ...
