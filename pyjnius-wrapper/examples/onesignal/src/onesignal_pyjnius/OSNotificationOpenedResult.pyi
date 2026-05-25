from typing import Any, ClassVar, overload
from OSNotification import OSNotification
from OSNotificationAction import OSNotificationAction

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class AppEntryAction:
    """Forward declaration for ``com.onesignal.OneSignal.AppEntryAction``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('com.onesignal.OneSignal.AppEntryAction')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.
    """
    ...
class JSONObject:
    """Forward declaration for ``org.json.JSONObject``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('org.json.JSONObject')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.
    """
    ...

class OSNotificationOpenedResult:
    def __init__(self, arg0: OSNotification, arg1: OSNotificationAction) -> None: ...
    def onEntryStateChange(self, arg0: AppEntryAction) -> None: ...
    def stringify(self) -> str: ...
    def toJSONObject(self) -> JSONObject: ...
    def getNotification(self) -> OSNotification: ...
    def getAction(self) -> OSNotificationAction: ...
    def toString(self) -> str: ...
