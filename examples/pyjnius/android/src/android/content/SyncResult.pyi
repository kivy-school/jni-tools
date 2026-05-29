from typing import Any, ClassVar, overload
from android.content.SyncStats import SyncStats
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

class SyncResult:
    ALREADY_IN_PROGRESS: ClassVar["SyncResult"]
    CREATOR: ClassVar[Creator]
    databaseError: bool
    delayUntil: int
    fullSyncRequested: bool
    moreRecordsToGet: bool
    partialSyncUnavailable: bool
    stats: SyncStats
    syncAlreadyInProgress: bool
    tooManyDeletions: bool
    tooManyRetries: bool
    def __init__(self) -> None: ...
    def hasHardError(self) -> bool: ...
    def hasSoftError(self) -> bool: ...
    def hasError(self) -> bool: ...
    def madeSomeProgress(self) -> bool: ...
    def clear(self) -> None: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, arg0: Parcel, arg1: int) -> None: ...
    def toString(self) -> str: ...
    def toDebugString(self) -> str: ...
