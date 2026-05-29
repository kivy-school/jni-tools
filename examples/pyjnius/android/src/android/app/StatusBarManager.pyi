from typing import Any, ClassVar, overload
from android.app.Activity import Activity
from android.content.ComponentName import ComponentName
from android.graphics.drawable.Icon import Icon
from java.util.concurrent.Executor import Executor
from java.util.function.Consumer import Consumer

class StatusBarManager:
    TILE_ADD_REQUEST_ERROR_APP_NOT_IN_FOREGROUND: ClassVar[int]
    TILE_ADD_REQUEST_ERROR_BAD_COMPONENT: ClassVar[int]
    TILE_ADD_REQUEST_ERROR_MISMATCHED_PACKAGE: ClassVar[int]
    TILE_ADD_REQUEST_ERROR_NOT_CURRENT_USER: ClassVar[int]
    TILE_ADD_REQUEST_ERROR_NO_STATUS_BAR_SERVICE: ClassVar[int]
    TILE_ADD_REQUEST_ERROR_REQUEST_IN_PROGRESS: ClassVar[int]
    TILE_ADD_REQUEST_RESULT_TILE_ADDED: ClassVar[int]
    TILE_ADD_REQUEST_RESULT_TILE_ALREADY_ADDED: ClassVar[int]
    TILE_ADD_REQUEST_RESULT_TILE_NOT_ADDED: ClassVar[int]
    def canLaunchCaptureContentActivityForNote(self, p0: Activity) -> bool: ...
    def requestAddTileService(self, p0: ComponentName, p1: str, p2: Icon, p3: Executor, p4: Consumer) -> None: ...
