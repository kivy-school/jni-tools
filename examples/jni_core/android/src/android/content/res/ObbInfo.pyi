from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel

class ObbInfo:
    CREATOR: ClassVar[Any]
    OBB_OVERLAY: ClassVar[int]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    filename: str
    flags: int
    packageName: str
    version: int
    def toString(self) -> str: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...
    def describeContents(self) -> int: ...
