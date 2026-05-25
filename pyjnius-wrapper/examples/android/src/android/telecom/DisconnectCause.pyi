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

class DisconnectCause:
    ANSWERED_ELSEWHERE: ClassVar[int]
    BUSY: ClassVar[int]
    CALL_PULLED: ClassVar[int]
    CANCELED: ClassVar[int]
    CONNECTION_MANAGER_NOT_SUPPORTED: ClassVar[int]
    CREATOR: ClassVar[Creator]
    ERROR: ClassVar[int]
    LOCAL: ClassVar[int]
    MISSED: ClassVar[int]
    OTHER: ClassVar[int]
    REASON_EMERGENCY_CALL_PLACED: ClassVar[str]
    REASON_EMULATING_SINGLE_CALL: ClassVar[str]
    REASON_IMS_ACCESS_BLOCKED: ClassVar[str]
    REASON_WIFI_ON_BUT_WFC_OFF: ClassVar[str]
    REJECTED: ClassVar[int]
    REMOTE: ClassVar[int]
    RESTRICTED: ClassVar[int]
    UNKNOWN: ClassVar[int]
    @overload
    def __init__(self, arg0: int) -> None: ...
    @overload
    def __init__(self, arg0: int, arg1: str) -> None: ...
    @overload
    def __init__(self, arg0: int, arg1: str, arg2: str, arg3: str) -> None: ...
    @overload
    def __init__(self, arg0: int, arg1: str, arg2: str, arg3: str, arg4: int) -> None: ...
    def getCode(self) -> int: ...
    def getLabel(self) -> str: ...
    def getDescription(self) -> str: ...
    def getReason(self) -> str: ...
    def getTone(self) -> int: ...
    def writeToParcel(self, arg0: Parcel, arg1: int) -> None: ...
    def describeContents(self) -> int: ...
    def hashCode(self) -> int: ...
    def equals(self, arg0: Any) -> bool: ...
    def toString(self) -> str: ...
