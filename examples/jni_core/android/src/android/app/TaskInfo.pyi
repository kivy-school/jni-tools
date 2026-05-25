from typing import Any, ClassVar, overload
from android.content.ComponentName import ComponentName
from android.content.Intent import Intent

class TaskInfo:
    baseActivity: ComponentName
    baseIntent: Intent
    isRunning: bool
    numActivities: int
    origActivity: ComponentName
    taskDescription: Any
    taskId: int
    topActivity: ComponentName
    def isVisible(self) -> bool: ...
    def toString(self) -> str: ...
