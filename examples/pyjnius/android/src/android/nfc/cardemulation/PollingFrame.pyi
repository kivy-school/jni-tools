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

class PollingFrame:
    CREATOR: ClassVar[Creator]
    POLLING_LOOP_TYPE_A: ClassVar[int]
    POLLING_LOOP_TYPE_B: ClassVar[int]
    POLLING_LOOP_TYPE_F: ClassVar[int]
    POLLING_LOOP_TYPE_OFF: ClassVar[int]
    POLLING_LOOP_TYPE_ON: ClassVar[int]
    POLLING_LOOP_TYPE_UNKNOWN: ClassVar[int]
    def getType(self) -> int: ...
    def getData(self) -> list[int]: ...
    def getVendorSpecificGain(self) -> int: ...
    def getTimestamp(self) -> int: ...
    def getTriggeredAutoTransact(self) -> bool: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, arg0: Parcel, arg1: int) -> None: ...
    def toString(self) -> str: ...
