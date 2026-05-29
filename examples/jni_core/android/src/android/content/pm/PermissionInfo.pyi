from typing import Any, ClassVar, overload
from android.content.pm.PackageManager import PackageManager
from android.os.Bundle import Bundle
from android.os.Parcel import Parcel

class PermissionInfo:
    CREATOR: ClassVar[Any]
    FLAG_COSTS_MONEY: ClassVar[int]
    FLAG_HARD_RESTRICTED: ClassVar[int]
    FLAG_IMMUTABLY_RESTRICTED: ClassVar[int]
    FLAG_INSTALLED: ClassVar[int]
    FLAG_SOFT_RESTRICTED: ClassVar[int]
    PROTECTION_DANGEROUS: ClassVar[int]
    PROTECTION_FLAG_APPOP: ClassVar[int]
    PROTECTION_FLAG_DEVELOPMENT: ClassVar[int]
    PROTECTION_FLAG_INSTALLER: ClassVar[int]
    PROTECTION_FLAG_INSTANT: ClassVar[int]
    PROTECTION_FLAG_PRE23: ClassVar[int]
    PROTECTION_FLAG_PREINSTALLED: ClassVar[int]
    PROTECTION_FLAG_PRIVILEGED: ClassVar[int]
    PROTECTION_FLAG_RUNTIME_ONLY: ClassVar[int]
    PROTECTION_FLAG_SETUP: ClassVar[int]
    PROTECTION_FLAG_SYSTEM: ClassVar[int]
    PROTECTION_FLAG_VERIFIER: ClassVar[int]
    PROTECTION_INTERNAL: ClassVar[int]
    PROTECTION_MASK_BASE: ClassVar[int]
    PROTECTION_MASK_FLAGS: ClassVar[int]
    PROTECTION_NORMAL: ClassVar[int]
    PROTECTION_SIGNATURE: ClassVar[int]
    PROTECTION_SIGNATURE_OR_SYSTEM: ClassVar[int]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    descriptionRes: int
    flags: int
    group: str
    nonLocalizedDescription: str
    protectionLevel: int
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
    def __init__(self, p0: "PermissionInfo") -> None: ...
    def toString(self) -> str: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...
    def describeContents(self) -> int: ...
    def loadDescription(self, p0: PackageManager) -> str: ...
    def getProtectionFlags(self) -> int: ...
    def getProtection(self) -> int: ...
