from typing import Any, ClassVar, overload
from android.content.pm.ApplicationInfo import ApplicationInfo

class ZygotePreload:
    def doPreload(self, arg0: ApplicationInfo) -> None: ...
