from typing import Any, ClassVar, overload
from android.content.pm.ApplicationInfo import ApplicationInfo
from android.os.Bundle import Bundle
from android.os.Parcel import Parcel
from android.util.Printer import Printer

class ServiceInfo:
    CREATOR: ClassVar[Any]
    FLAG_ALLOW_SHARED_ISOLATED_PROCESS: ClassVar[int]
    FLAG_EXTERNAL_SERVICE: ClassVar[int]
    FLAG_ISOLATED_PROCESS: ClassVar[int]
    FLAG_SINGLE_USER: ClassVar[int]
    FLAG_STOP_WITH_TASK: ClassVar[int]
    FLAG_USE_APP_ZYGOTE: ClassVar[int]
    FOREGROUND_SERVICE_TYPE_CAMERA: ClassVar[int]
    FOREGROUND_SERVICE_TYPE_CONNECTED_DEVICE: ClassVar[int]
    FOREGROUND_SERVICE_TYPE_DATA_SYNC: ClassVar[int]
    FOREGROUND_SERVICE_TYPE_HEALTH: ClassVar[int]
    FOREGROUND_SERVICE_TYPE_LOCATION: ClassVar[int]
    FOREGROUND_SERVICE_TYPE_MANIFEST: ClassVar[int]
    FOREGROUND_SERVICE_TYPE_MEDIA_PLAYBACK: ClassVar[int]
    FOREGROUND_SERVICE_TYPE_MEDIA_PROCESSING: ClassVar[int]
    FOREGROUND_SERVICE_TYPE_MEDIA_PROJECTION: ClassVar[int]
    FOREGROUND_SERVICE_TYPE_MICROPHONE: ClassVar[int]
    FOREGROUND_SERVICE_TYPE_NONE: ClassVar[int]
    FOREGROUND_SERVICE_TYPE_PHONE_CALL: ClassVar[int]
    FOREGROUND_SERVICE_TYPE_REMOTE_MESSAGING: ClassVar[int]
    FOREGROUND_SERVICE_TYPE_SHORT_SERVICE: ClassVar[int]
    FOREGROUND_SERVICE_TYPE_SPECIAL_USE: ClassVar[int]
    FOREGROUND_SERVICE_TYPE_SYSTEM_EXEMPTED: ClassVar[int]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    flags: int
    permission: str
    applicationInfo: ApplicationInfo
    attributionTags: Any
    descriptionRes: int
    directBootAware: bool
    enabled: bool
    exported: bool
    processName: str
    splitName: str
    banner: int
    icon: int
    isArchived: bool
    labelRes: int
    logo: int
    metaData: Bundle
    name: str
    nonLocalizedLabel: str
    packageName: str
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, p0: "ServiceInfo") -> None: ...
    def toString(self) -> str: ...
    def dump(self, p0: Printer, p1: str) -> None: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...
    def describeContents(self) -> int: ...
    def getForegroundServiceType(self) -> int: ...
