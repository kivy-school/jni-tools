from typing import Any, ClassVar, overload
from android.os.Bundle import Bundle
from java.util.concurrent.Executor import Executor

class TvAdManager:
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
    INTENT_KEY_AD_SERVICE_ID: ClassVar[str]
    INTENT_KEY_CHANNEL_URI: ClassVar[str]
    INTENT_KEY_COMMAND_TYPE: ClassVar[str]
    INTENT_KEY_TV_INPUT_ID: ClassVar[str]
    SESSION_DATA_KEY_AD_BUFFER: ClassVar[str]
    SESSION_DATA_KEY_AD_REQUEST: ClassVar[str]
    SESSION_DATA_KEY_BROADCAST_INFO_REQUEST: ClassVar[str]
    SESSION_DATA_KEY_REQUEST_ID: ClassVar[str]
    SESSION_DATA_TYPE_AD_BUFFER_READY: ClassVar[str]
    SESSION_DATA_TYPE_AD_REQUEST: ClassVar[str]
    SESSION_DATA_TYPE_BROADCAST_INFO_REQUEST: ClassVar[str]
    SESSION_DATA_TYPE_REMOVE_BROADCAST_INFO_REQUEST: ClassVar[str]
    SESSION_STATE_ERROR: ClassVar[int]
    SESSION_STATE_RUNNING: ClassVar[int]
    SESSION_STATE_STOPPED: ClassVar[int]
    def registerCallback(self, p0: Executor, p1: Any) -> None: ...
    def unregisterCallback(self, p0: Any) -> None: ...
    def getTvAdServiceList(self) -> list: ...
    def sendAppLinkCommand(self, p0: str, p1: Bundle) -> None: ...

    class TvAdServiceCallback:
        def __init__(self) -> None: ...
        def onAdServiceUpdated(self, p0: str) -> None: ...
        def onAdServiceAdded(self, p0: str) -> None: ...
        def onAdServiceRemoved(self, p0: str) -> None: ...
