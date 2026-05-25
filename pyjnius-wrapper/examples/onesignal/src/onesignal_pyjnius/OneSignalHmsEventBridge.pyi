from typing import Any, ClassVar, overload
from android.content.Context import Context
from android.os.Bundle import Bundle

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class RemoteMessage:
    """Forward declaration for ``com.huawei.hms.push.RemoteMessage``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('com.huawei.hms.push.RemoteMessage')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.
    """
    ...

class OneSignalHmsEventBridge:
    HMS_TTL_KEY: ClassVar[str]
    HMS_SENT_TIME_KEY: ClassVar[str]
    def __init__(self) -> None: ...
    @overload
    @staticmethod
    def onNewToken(arg0: Context, arg1: str, arg2: Bundle) -> None: ...
    @overload
    @staticmethod
    def onNewToken(arg0: Context, arg1: str) -> None: ...
    @staticmethod
    def onMessageReceived(arg0: Context, arg1: RemoteMessage) -> None: ...
