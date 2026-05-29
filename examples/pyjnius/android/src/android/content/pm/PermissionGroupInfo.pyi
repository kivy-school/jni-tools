from typing import Any, ClassVar, overload
from android.content.pm.PackageManager import PackageManager
from android.os.Bundle import Bundle
from android.os.Parcel import Parcel

class PermissionGroupInfo:
    CREATOR: ClassVar[Any]
    FLAG_PERSONAL_INFO: ClassVar[int]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    descriptionRes: int
    flags: int
    nonLocalizedDescription: str
    priority: int
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
    def __init__(self, p0: "PermissionGroupInfo") -> None: ...
    def toString(self) -> str: ...
    def loadDescription(self, p0: PackageManager) -> str: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...
    def describeContents(self) -> int: ...
