from typing import Any, ClassVar, overload
from android.content.ComponentName import ComponentName
from android.content.Context import Context

class NewHtcHomeBadger:
    INTENT_UPDATE_SHORTCUT: ClassVar[str]
    INTENT_SET_NOTIFICATION: ClassVar[str]
    PACKAGENAME: ClassVar[str]
    COUNT: ClassVar[str]
    EXTRA_COMPONENT: ClassVar[str]
    EXTRA_COUNT: ClassVar[str]
    def __init__(self) -> None: ...
    def executeBadge(self, arg0: Context, arg1: ComponentName, arg2: int) -> None: ...
    def getSupportLaunchers(self) -> list: ...
