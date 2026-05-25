from typing import Any, ClassVar, overload
from android.content.Intent import Intent
from android.os.Parcel import Parcel

class ApplicationStartInfo:
    CREATOR: ClassVar[Any]
    LAUNCH_MODE_SINGLE_INSTANCE: ClassVar[int]
    LAUNCH_MODE_SINGLE_INSTANCE_PER_TASK: ClassVar[int]
    LAUNCH_MODE_SINGLE_TASK: ClassVar[int]
    LAUNCH_MODE_SINGLE_TOP: ClassVar[int]
    LAUNCH_MODE_STANDARD: ClassVar[int]
    STARTUP_STATE_ERROR: ClassVar[int]
    STARTUP_STATE_FIRST_FRAME_DRAWN: ClassVar[int]
    STARTUP_STATE_STARTED: ClassVar[int]
    START_REASON_ALARM: ClassVar[int]
    START_REASON_BACKUP: ClassVar[int]
    START_REASON_BOOT_COMPLETE: ClassVar[int]
    START_REASON_BROADCAST: ClassVar[int]
    START_REASON_CONTENT_PROVIDER: ClassVar[int]
    START_REASON_JOB: ClassVar[int]
    START_REASON_LAUNCHER: ClassVar[int]
    START_REASON_LAUNCHER_RECENTS: ClassVar[int]
    START_REASON_OTHER: ClassVar[int]
    START_REASON_PUSH: ClassVar[int]
    START_REASON_SERVICE: ClassVar[int]
    START_REASON_START_ACTIVITY: ClassVar[int]
    START_TIMESTAMP_APPLICATION_ONCREATE: ClassVar[int]
    START_TIMESTAMP_BIND_APPLICATION: ClassVar[int]
    START_TIMESTAMP_FIRST_FRAME: ClassVar[int]
    START_TIMESTAMP_FORK: ClassVar[int]
    START_TIMESTAMP_FULLY_DRAWN: ClassVar[int]
    START_TIMESTAMP_INITIAL_RENDERTHREAD_FRAME: ClassVar[int]
    START_TIMESTAMP_LAUNCH: ClassVar[int]
    START_TIMESTAMP_RESERVED_RANGE_DEVELOPER: ClassVar[int]
    START_TIMESTAMP_RESERVED_RANGE_DEVELOPER_START: ClassVar[int]
    START_TIMESTAMP_RESERVED_RANGE_SYSTEM: ClassVar[int]
    START_TIMESTAMP_SURFACEFLINGER_COMPOSITION_COMPLETE: ClassVar[int]
    START_TYPE_COLD: ClassVar[int]
    START_TYPE_HOT: ClassVar[int]
    START_TYPE_UNSET: ClassVar[int]
    START_TYPE_WARM: ClassVar[int]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    def getProcessName(self) -> str: ...
    def getStartupState(self) -> int: ...
    def getRealUid(self) -> int: ...
    def getDefiningUid(self) -> int: ...
    def getStartupTimestamps(self) -> dict: ...
    def getStartType(self) -> int: ...
    def getLaunchMode(self) -> int: ...
    def wasForceStopped(self) -> bool: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...
    def getPackageUid(self) -> int: ...
    def getIntent(self) -> Intent: ...
    def getPid(self) -> int: ...
    def getReason(self) -> int: ...
    def equals(self, p0: Any) -> bool: ...
    def hashCode(self) -> int: ...
