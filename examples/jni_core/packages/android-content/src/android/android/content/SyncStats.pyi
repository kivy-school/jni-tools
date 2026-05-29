from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel

class SyncStats:
    CREATOR: ClassVar[Any]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    numAuthExceptions: int
    numConflictDetectedExceptions: int
    numDeletes: int
    numEntries: int
    numInserts: int
    numIoExceptions: int
    numParseExceptions: int
    numSkippedEntries: int
    numUpdates: int
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, p0: Parcel) -> None: ...
    def toString(self) -> str: ...
    def clear(self) -> None: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...
