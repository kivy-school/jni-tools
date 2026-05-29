from typing import Any, ClassVar, overload
from android.content.Context import Context
from android.content.pm.ApplicationInfo import ApplicationInfo

class ApplicationInfoHelper:
    Companion: ClassVar["Companion"]
    def __init__(self) -> None: ...

    class Companion:
        def getInfo(self, arg0: Context) -> ApplicationInfo: ...
