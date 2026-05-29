from typing import Any, ClassVar, overload
from android.content.pm.ApplicationInfo import ApplicationInfo
from android.content.pm.SigningInfo import SigningInfo
from android.os.Parcel import Parcel

class PackageInfo:
    CREATOR: ClassVar[Any]
    INSTALL_LOCATION_AUTO: ClassVar[int]
    INSTALL_LOCATION_INTERNAL_ONLY: ClassVar[int]
    INSTALL_LOCATION_PREFER_EXTERNAL: ClassVar[int]
    REQUESTED_PERMISSION_GRANTED: ClassVar[int]
    REQUESTED_PERMISSION_IMPLICIT: ClassVar[int]
    REQUESTED_PERMISSION_NEVER_FOR_LOCATION: ClassVar[int]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    activities: Any
    applicationInfo: ApplicationInfo
    attributions: Any
    baseRevisionCode: int
    configPreferences: Any
    featureGroups: Any
    firstInstallTime: int
    gids: Any
    installLocation: int
    instrumentation: Any
    isApex: bool
    lastUpdateTime: int
    packageName: str
    permissions: Any
    providers: Any
    receivers: Any
    reqFeatures: Any
    requestedPermissions: Any
    requestedPermissionsFlags: Any
    services: Any
    sharedUserId: str
    sharedUserLabel: int
    signatures: Any
    signingInfo: SigningInfo
    splitNames: Any
    splitRevisionCodes: Any
    versionCode: int
    versionName: str
    def __init__(self) -> None: ...
    def toString(self) -> str: ...
    def getLongVersionCode(self) -> int: ...
    def setLongVersionCode(self, p0: int) -> None: ...
    def getArchiveTimeMillis(self) -> int: ...
    def getApexPackageName(self) -> str: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...
