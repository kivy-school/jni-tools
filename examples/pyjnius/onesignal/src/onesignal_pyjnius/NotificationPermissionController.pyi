from typing import Any, ClassVar, overload

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class PromptForPushNotificationPermissionResponseHandler:
    """Forward declaration for ``com.onesignal.OneSignal.PromptForPushNotificationPermissionResponseHandler``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('com.onesignal.OneSignal.PromptForPushNotificationPermissionResponseHandler')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.
    """
    ...

class NotificationPermissionController:
    INSTANCE: ClassVar["NotificationPermissionController"]
    def prompt(self, arg0: bool, arg1: PromptForPushNotificationPermissionResponseHandler) -> None: ...
    def onAccept(self) -> None: ...
    def onReject(self, arg0: bool) -> None: ...
    def onAppForegrounded(self) -> None: ...
