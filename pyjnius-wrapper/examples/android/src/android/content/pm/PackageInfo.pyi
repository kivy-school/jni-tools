from typing import Any, ClassVar, overload
from android.content.pm.ActivityInfo import ActivityInfo
from android.content.pm.ApplicationInfo import ApplicationInfo
from android.content.pm.Attribution import Attribution
from android.content.pm.ConfigurationInfo import ConfigurationInfo
from android.content.pm.FeatureGroupInfo import FeatureGroupInfo
from android.content.pm.FeatureInfo import FeatureInfo
from android.content.pm.InstrumentationInfo import InstrumentationInfo
from android.content.pm.PermissionInfo import PermissionInfo
from android.content.pm.ProviderInfo import ProviderInfo
from android.content.pm.ServiceInfo import ServiceInfo
from android.content.pm.Signature import Signature
from android.content.pm.SigningInfo import SigningInfo
from android.os.Parcel import Parcel

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

class PackageInfo:
    CREATOR: ClassVar[Creator]
    INSTALL_LOCATION_AUTO: ClassVar[int]
    INSTALL_LOCATION_INTERNAL_ONLY: ClassVar[int]
    INSTALL_LOCATION_PREFER_EXTERNAL: ClassVar[int]
    REQUESTED_PERMISSION_GRANTED: ClassVar[int]
    REQUESTED_PERMISSION_IMPLICIT: ClassVar[int]
    REQUESTED_PERMISSION_NEVER_FOR_LOCATION: ClassVar[int]
    activities: list[ActivityInfo]
    applicationInfo: ApplicationInfo
    attributions: list[Attribution]
    baseRevisionCode: int
    configPreferences: list[ConfigurationInfo]
    featureGroups: list[FeatureGroupInfo]
    firstInstallTime: int
    gids: list[int]
    installLocation: int
    instrumentation: list[InstrumentationInfo]
    isApex: bool
    lastUpdateTime: int
    packageName: str
    permissions: list[PermissionInfo]
    providers: list[ProviderInfo]
    receivers: list[ActivityInfo]
    reqFeatures: list[FeatureInfo]
    requestedPermissions: list[str]
    requestedPermissionsFlags: list[int]
    services: list[ServiceInfo]
    sharedUserId: str
    sharedUserLabel: int
    signatures: list[Signature]
    signingInfo: SigningInfo
    splitNames: list[str]
    splitRevisionCodes: list[int]
    versionCode: int
    versionName: str
    def __init__(self) -> None: ...
    def getLongVersionCode(self) -> int: ...
    def setLongVersionCode(self, arg0: int) -> None: ...
    def getArchiveTimeMillis(self) -> int: ...
    def getApexPackageName(self) -> str: ...
    def toString(self) -> str: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, arg0: Parcel, arg1: int) -> None: ...
