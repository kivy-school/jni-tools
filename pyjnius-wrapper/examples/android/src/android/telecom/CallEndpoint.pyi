from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel
from android.os.ParcelUuid import ParcelUuid

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

class CallEndpoint:
    CREATOR: ClassVar[Creator]
    TYPE_BLUETOOTH: ClassVar[int]
    TYPE_EARPIECE: ClassVar[int]
    TYPE_SPEAKER: ClassVar[int]
    TYPE_STREAMING: ClassVar[int]
    TYPE_UNKNOWN: ClassVar[int]
    TYPE_WIRED_HEADSET: ClassVar[int]
    def __init__(self, arg0: str, arg1: int, arg2: ParcelUuid) -> None: ...
    def equals(self, arg0: Any) -> bool: ...
    def hashCode(self) -> int: ...
    def toString(self) -> str: ...
    def getEndpointName(self) -> str: ...
    def getEndpointType(self) -> int: ...
    def getIdentifier(self) -> ParcelUuid: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, arg0: Parcel, arg1: int) -> None: ...
