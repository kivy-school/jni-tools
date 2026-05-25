from typing import Any, ClassVar, overload
from android.content.pm.PackageManager import PackageManager
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

class PermissionInfo:
    CREATOR: ClassVar[Creator]
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
    descriptionRes: int
    flags: int
    group: str
    nonLocalizedDescription: str
    protectionLevel: int
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, arg0: "PermissionInfo") -> None: ...
    def loadDescription(self, arg0: PackageManager) -> str: ...
    def getProtection(self) -> int: ...
    def getProtectionFlags(self) -> int: ...
    def toString(self) -> str: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, arg0: Parcel, arg1: int) -> None: ...
