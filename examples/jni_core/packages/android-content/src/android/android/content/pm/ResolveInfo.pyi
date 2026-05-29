from typing import Any, ClassVar, overload
from android.content.IntentFilter import IntentFilter
from android.content.pm.ActivityInfo import ActivityInfo
from android.content.pm.PackageManager import PackageManager
from android.content.pm.ProviderInfo import ProviderInfo
from android.content.pm.ServiceInfo import ServiceInfo
from android.graphics.drawable.Drawable import Drawable
from android.os.Parcel import Parcel
from android.util.Printer import Printer

class ResolveInfo:
    CREATOR: ClassVar[Any]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    activityInfo: ActivityInfo
    filter: IntentFilter
    icon: int
    isDefault: bool
    isInstantAppAvailable: bool
    labelRes: int
    match_: int
    nonLocalizedLabel: str
    preferredOrder: int
    priority: int
    providerInfo: ProviderInfo
    resolvePackageName: str
    serviceInfo: ServiceInfo
    specificIndex: int
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, p0: "ResolveInfo") -> None: ...
    def toString(self) -> str: ...
    def dump(self, p0: Printer, p1: str) -> None: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...
    def describeContents(self) -> int: ...
    def loadIcon(self, p0: PackageManager) -> Drawable: ...
    def loadLabel(self, p0: PackageManager) -> str: ...
    def isCrossProfileIntentForwarderActivity(self) -> bool: ...
    def getIconResource(self) -> int: ...

    class DisplayNameComparator:
        def __init__(self, p0: PackageManager) -> None: ...
        @overload
        def compare(self, p0: "ResolveInfo", p1: "ResolveInfo") -> int: ...
        @overload
        def compare(self, p0: Any, p1: Any) -> int: ...
