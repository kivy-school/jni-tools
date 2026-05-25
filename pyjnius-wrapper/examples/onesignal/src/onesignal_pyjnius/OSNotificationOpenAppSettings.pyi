from typing import Any, ClassVar, overload
from android.content.Context import Context

class OSNotificationOpenAppSettings:
    INSTANCE: ClassVar["OSNotificationOpenAppSettings"]
    def getShouldOpenActivity(self, arg0: Context) -> bool: ...
    def getSuppressLaunchURL(self, arg0: Context) -> bool: ...
