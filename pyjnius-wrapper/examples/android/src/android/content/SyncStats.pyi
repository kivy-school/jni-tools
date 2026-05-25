from typing import Any, ClassVar, overload
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

class SyncStats:
    CREATOR: ClassVar[Creator]
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
    def __init__(self, arg0: Parcel) -> None: ...
    def toString(self) -> str: ...
    def clear(self) -> None: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, arg0: Parcel, arg1: int) -> None: ...
