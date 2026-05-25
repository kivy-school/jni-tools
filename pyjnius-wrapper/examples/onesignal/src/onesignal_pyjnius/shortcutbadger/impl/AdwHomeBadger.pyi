from typing import Any, ClassVar, overload
from android.content.ComponentName import ComponentName
from android.content.Context import Context

class AdwHomeBadger:
    INTENT_UPDATE_COUNTER: ClassVar[str]
    PACKAGENAME: ClassVar[str]
    CLASSNAME: ClassVar[str]
    COUNT: ClassVar[str]
    def __init__(self) -> None: ...
    def executeBadge(self, arg0: Context, arg1: ComponentName, arg2: int) -> None: ...
    def getSupportLaunchers(self) -> list: ...
