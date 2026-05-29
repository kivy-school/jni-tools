from typing import Any, ClassVar, overload
from android.content.pm.ApplicationInfo import ApplicationInfo
from android.os.Bundle import Bundle
from android.os.Parcel import Parcel

class ComponentInfo:
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
    def __init__(self, p0: "ComponentInfo") -> None: ...
    @overload
    def __init__(self) -> None: ...
    def isEnabled(self) -> bool: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...
    def getBannerResource(self) -> int: ...
    def getLogoResource(self) -> int: ...
    def getIconResource(self) -> int: ...
