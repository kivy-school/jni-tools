from typing import Any, ClassVar, overload
from android.media.tv.interactive.AppLinkInfo import AppLinkInfo
from android.os.Bundle import Bundle
from java.util.concurrent.Executor import Executor

class TvInteractiveAppManager:
    ACTION_APP_LINK_COMMAND: ClassVar[str]
    APP_LINK_KEY_BACK_URI: ClassVar[str]
    APP_LINK_KEY_CLASS_NAME: ClassVar[str]
    APP_LINK_KEY_COMMAND_TYPE: ClassVar[str]
    APP_LINK_KEY_PACKAGE_NAME: ClassVar[str]
    APP_LINK_KEY_SERVICE_ID: ClassVar[str]
    ERROR_BLOCKED: ClassVar[int]
    ERROR_ENCRYPTED: ClassVar[int]
    ERROR_NONE: ClassVar[int]
    ERROR_NOT_SUPPORTED: ClassVar[int]
    ERROR_RESOURCE_UNAVAILABLE: ClassVar[int]
    ERROR_UNKNOWN: ClassVar[int]
    ERROR_UNKNOWN_CHANNEL: ClassVar[int]
    ERROR_WEAK_SIGNAL: ClassVar[int]
    INTENT_KEY_BI_INTERACTIVE_APP_TYPE: ClassVar[str]
    INTENT_KEY_BI_INTERACTIVE_APP_URI: ClassVar[str]
    INTENT_KEY_CHANNEL_URI: ClassVar[str]
    INTENT_KEY_COMMAND_TYPE: ClassVar[str]
    INTENT_KEY_INTERACTIVE_APP_SERVICE_ID: ClassVar[str]
    INTENT_KEY_TV_INPUT_ID: ClassVar[str]
    INTERACTIVE_APP_STATE_ERROR: ClassVar[int]
    INTERACTIVE_APP_STATE_RUNNING: ClassVar[int]
    INTERACTIVE_APP_STATE_STOPPED: ClassVar[int]
    SERVICE_STATE_ERROR: ClassVar[int]
    SERVICE_STATE_PREPARING: ClassVar[int]
    SERVICE_STATE_READY: ClassVar[int]
    SERVICE_STATE_UNREALIZED: ClassVar[int]
    TELETEXT_APP_STATE_ERROR: ClassVar[int]
    TELETEXT_APP_STATE_HIDE: ClassVar[int]
    TELETEXT_APP_STATE_SHOW: ClassVar[int]
    def getTvInteractiveAppServiceList(self) -> list: ...
    def getAppLinkInfoList(self) -> list: ...
    def registerAppLinkInfo(self, arg0: str, arg1: AppLinkInfo) -> None: ...
    def unregisterAppLinkInfo(self, arg0: str, arg1: AppLinkInfo) -> None: ...
    def sendAppLinkCommand(self, arg0: str, arg1: Bundle) -> None: ...
    def registerCallback(self, arg0: Executor, arg1: "TvInteractiveAppCallback") -> None: ...
    def unregisterCallback(self, arg0: "TvInteractiveAppCallback") -> None: ...

    class TvInteractiveAppCallback:
        def __init__(self) -> None: ...
        def onInteractiveAppServiceAdded(self, arg0: str) -> None: ...
        def onInteractiveAppServiceRemoved(self, arg0: str) -> None: ...
        def onInteractiveAppServiceUpdated(self, arg0: str) -> None: ...
        def onTvInteractiveAppServiceStateChanged(self, arg0: str, arg1: int, arg2: int, arg3: int) -> None: ...
