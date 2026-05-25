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

class WifiAvailableChannel:
    CREATOR: ClassVar[Creator]
    OP_MODE_SAP: ClassVar[int]
    OP_MODE_STA: ClassVar[int]
    OP_MODE_TDLS: ClassVar[int]
    OP_MODE_WIFI_AWARE: ClassVar[int]
    OP_MODE_WIFI_DIRECT_CLI: ClassVar[int]
    OP_MODE_WIFI_DIRECT_GO: ClassVar[int]
    def __init__(self, arg0: int, arg1: int) -> None: ...
    def getFrequencyMhz(self) -> int: ...
    def getOperationalModes(self) -> int: ...
    def describeContents(self) -> int: ...
    def equals(self, arg0: Any) -> bool: ...
    def hashCode(self) -> int: ...
    def toString(self) -> str: ...
    def writeToParcel(self, arg0: Parcel, arg1: int) -> None: ...
