from typing import Any, ClassVar, overload
from android.content.pm.VersionedPackage import VersionedPackage
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

class SharedLibraryInfo:
    CREATOR: ClassVar[Creator]
    TYPE_BUILTIN: ClassVar[int]
    TYPE_DYNAMIC: ClassVar[int]
    TYPE_SDK_PACKAGE: ClassVar[int]
    TYPE_STATIC: ClassVar[int]
    VERSION_UNDEFINED: ClassVar[int]
    def getType(self) -> int: ...
    def getName(self) -> str: ...
    def getVersion(self) -> int: ...
    def getLongVersion(self) -> int: ...
    def getDeclaringPackage(self) -> VersionedPackage: ...
    def getDependentPackages(self) -> list: ...
    def describeContents(self) -> int: ...
    def toString(self) -> str: ...
    def writeToParcel(self, arg0: Parcel, arg1: int) -> None: ...
