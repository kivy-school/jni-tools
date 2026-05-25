from typing import Any, ClassVar, overload
from android.content.res.Configuration import Configuration
from android.os.Parcel import Parcel
from android.os.PersistableBundle import PersistableBundle

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Creator:
    """Forward declaration for ``android.os.Parcelable.Creator``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.os.Parcelable.Creator')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/os/Parcelable/Creator
    """
    ...

class UsageEvents:
    CREATOR: ClassVar[Creator]
    def hasNextEvent(self) -> bool: ...
    def getNextEvent(self, arg0: "Event") -> bool: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, arg0: Parcel, arg1: int) -> None: ...

    class Event:
        ACTIVITY_PAUSED: ClassVar[int]
        ACTIVITY_RESUMED: ClassVar[int]
        ACTIVITY_STOPPED: ClassVar[int]
        CONFIGURATION_CHANGE: ClassVar[int]
        DEVICE_SHUTDOWN: ClassVar[int]
        DEVICE_STARTUP: ClassVar[int]
        FOREGROUND_SERVICE_START: ClassVar[int]
        FOREGROUND_SERVICE_STOP: ClassVar[int]
        KEYGUARD_HIDDEN: ClassVar[int]
        KEYGUARD_SHOWN: ClassVar[int]
        MOVE_TO_BACKGROUND: ClassVar[int]
        MOVE_TO_FOREGROUND: ClassVar[int]
        NONE: ClassVar[int]
        SCREEN_INTERACTIVE: ClassVar[int]
        SCREEN_NON_INTERACTIVE: ClassVar[int]
        SHORTCUT_INVOCATION: ClassVar[int]
        STANDBY_BUCKET_CHANGED: ClassVar[int]
        USER_INTERACTION: ClassVar[int]
        def __init__(self) -> None: ...
        def getPackageName(self) -> str: ...
        def getClassName(self) -> str: ...
        def getTimeStamp(self) -> int: ...
        def getEventType(self) -> int: ...
        def getExtras(self) -> PersistableBundle: ...
        def getConfiguration(self) -> Configuration: ...
        def getShortcutId(self) -> str: ...
        def getAppStandbyBucket(self) -> int: ...
