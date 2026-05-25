from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel
from java.time.Duration import Duration

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

class SyncFence:
    CREATOR: ClassVar[Creator]
    SIGNAL_TIME_INVALID: ClassVar[int]
    SIGNAL_TIME_PENDING: ClassVar[int]
    def __init__(self, arg0: "SyncFence") -> None: ...
    def isValid(self) -> bool: ...
    def await_(self, arg0: Duration) -> bool: ...
    def awaitForever(self) -> bool: ...
    def getSignalTime(self) -> int: ...
    def close(self) -> None: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, arg0: Parcel, arg1: int) -> None: ...
