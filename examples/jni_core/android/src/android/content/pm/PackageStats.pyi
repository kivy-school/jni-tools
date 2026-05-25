from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel

class PackageStats:
    CREATOR: ClassVar[Any]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    cacheSize: int
    codeSize: int
    dataSize: int
    externalCacheSize: int
    externalCodeSize: int
    externalDataSize: int
    externalMediaSize: int
    externalObbSize: int
    packageName: str
    @overload
    def __init__(self, p0: str) -> None: ...
    @overload
    def __init__(self, p0: Parcel) -> None: ...
    @overload
    def __init__(self, p0: "PackageStats") -> None: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...
    def equals(self, p0: Any) -> bool: ...
    def toString(self) -> str: ...
    def hashCode(self) -> int: ...
