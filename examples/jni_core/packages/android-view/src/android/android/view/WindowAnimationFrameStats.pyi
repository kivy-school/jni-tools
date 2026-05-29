from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel

class WindowAnimationFrameStats:
    CREATOR: ClassVar[Any]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    UNDEFINED_TIME_NANO: ClassVar[int]
    def toString(self) -> str: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...
