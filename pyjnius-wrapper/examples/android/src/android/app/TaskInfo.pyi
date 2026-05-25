from typing import Any, ClassVar, overload
from android.content.ComponentName import ComponentName
from android.content.Intent import Intent

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class TaskDescription:
    """Forward declaration for ``android.app.ActivityManager.TaskDescription``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.app.ActivityManager.TaskDescription')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/app/ActivityManager/TaskDescription
    """
    ...

class TaskInfo:
    baseActivity: ComponentName
    baseIntent: Intent
    isRunning: bool
    numActivities: int
    origActivity: ComponentName
    taskDescription: TaskDescription
    taskId: int
    topActivity: ComponentName
    def isVisible(self) -> bool: ...
    def toString(self) -> str: ...
