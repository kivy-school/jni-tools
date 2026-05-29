from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel

class AudioTimestamp:
    CREATOR: ClassVar[Any]
    TIMEBASE_BOOTTIME: ClassVar[int]
    TIMEBASE_MONOTONIC: ClassVar[int]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    framePosition: int
    nanoTime: int
    def __init__(self) -> None: ...
    def toString(self) -> str: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...
