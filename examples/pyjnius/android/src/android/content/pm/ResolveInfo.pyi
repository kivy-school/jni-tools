from typing import Any, ClassVar, overload
from android.content.IntentFilter import IntentFilter
from android.content.pm.ActivityInfo import ActivityInfo
from android.content.pm.PackageManager import PackageManager
from android.content.pm.ProviderInfo import ProviderInfo
from android.content.pm.ServiceInfo import ServiceInfo
from android.graphics.drawable.Drawable import Drawable
from android.os.Parcel import Parcel
from android.util.Printer import Printer

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

class ResolveInfo:
    CREATOR: ClassVar[Creator]
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
    def __init__(self, arg0: "ResolveInfo") -> None: ...
    def loadLabel(self, arg0: PackageManager) -> str: ...
    def loadIcon(self, arg0: PackageManager) -> Drawable: ...
    def getIconResource(self) -> int: ...
    def dump(self, arg0: Printer, arg1: str) -> None: ...
    def isCrossProfileIntentForwarderActivity(self) -> bool: ...
    def toString(self) -> str: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, arg0: Parcel, arg1: int) -> None: ...

    class DisplayNameComparator:
        def __init__(self, arg0: PackageManager) -> None: ...
        def compare(self, arg0: "ResolveInfo", arg1: "ResolveInfo") -> int: ...
