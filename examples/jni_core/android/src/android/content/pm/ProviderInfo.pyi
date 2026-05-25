from typing import Any, ClassVar, overload
from android.content.pm.ApplicationInfo import ApplicationInfo
from android.os.Bundle import Bundle
from android.os.Parcel import Parcel
from android.util.Printer import Printer

class ProviderInfo:
    CREATOR: ClassVar[Any]
    FLAG_SINGLE_USER: ClassVar[int]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    authority: str
    flags: int
    forceUriPermissions: bool
    grantUriPermissions: bool
    initOrder: int
    isSyncable: bool
    multiprocess: bool
    pathPermissions: Any
    readPermission: str
    uriPermissionPatterns: Any
    writePermission: str
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
    def __init__(self, p0: "ProviderInfo") -> None: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...
    def dump(self, p0: Printer, p1: str) -> None: ...
    def toString(self) -> str: ...
