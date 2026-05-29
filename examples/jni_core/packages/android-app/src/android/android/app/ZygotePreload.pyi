from typing import Any, ClassVar, overload
from android.content.pm.ApplicationInfo import ApplicationInfo

class ZygotePreload:
    def doPreload(self, p0: ApplicationInfo) -> None: ...
