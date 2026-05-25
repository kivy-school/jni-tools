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

class CallException:
    CODE_CALL_CANNOT_BE_SET_TO_ACTIVE: ClassVar[int]
    CODE_CALL_IS_NOT_BEING_TRACKED: ClassVar[int]
    CODE_CALL_NOT_PERMITTED_AT_PRESENT_TIME: ClassVar[int]
    CODE_CANNOT_HOLD_CURRENT_ACTIVE_CALL: ClassVar[int]
    CODE_ERROR_UNKNOWN: ClassVar[int]
    CODE_OPERATION_TIMED_OUT: ClassVar[int]
    CREATOR: ClassVar[Creator]
    def __init__(self, arg0: str, arg1: int) -> None: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, arg0: Parcel, arg1: int) -> None: ...
    def getCode(self) -> int: ...
