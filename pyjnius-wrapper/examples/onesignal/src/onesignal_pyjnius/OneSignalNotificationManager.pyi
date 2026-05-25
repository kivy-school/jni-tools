from typing import Any, ClassVar, overload
from android.content.Context import Context

class OneSignalNotificationManager:
    def __init__(self) -> None: ...
    @staticmethod
    def areNotificationsEnabled(arg0: Context, arg1: str) -> bool: ...
