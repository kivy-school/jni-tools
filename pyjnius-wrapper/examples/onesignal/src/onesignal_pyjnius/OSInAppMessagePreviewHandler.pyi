from typing import Any, ClassVar, overload
from android.app.Activity import Activity
from android.content.Context import Context
from android.os.Bundle import Bundle

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class JSONObject:
    """Forward declaration for ``org.json.JSONObject``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('org.json.JSONObject')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.
    """
    ...

class OSInAppMessagePreviewHandler:
    INSTANCE: ClassVar["OSInAppMessagePreviewHandler"]
    @staticmethod
    def notificationReceived(arg0: Context, arg1: Bundle) -> bool: ...
    @staticmethod
    def notificationOpened(arg0: Activity, arg1: JSONObject) -> bool: ...
    @staticmethod
    def inAppPreviewPushUUID(arg0: JSONObject) -> str: ...
