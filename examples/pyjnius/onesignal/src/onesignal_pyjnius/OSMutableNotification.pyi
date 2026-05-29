from typing import Any, ClassVar, overload

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Extender:
    """Forward declaration for ``androidx.core.app.NotificationCompat.Extender``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('androidx.core.app.NotificationCompat.Extender')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/androidx/core/app/NotificationCompat/Extender
    """
    ...

class OSMutableNotification:
    def setExtender(self, arg0: Extender) -> None: ...
    def setAndroidNotificationId(self, arg0: int) -> None: ...
