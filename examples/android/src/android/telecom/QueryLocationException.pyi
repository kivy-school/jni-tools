from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel
from java.lang.Throwable import Throwable

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

class QueryLocationException:
    CREATOR: ClassVar[Creator]
    ERROR_NOT_ALLOWED_FOR_NON_EMERGENCY_CONNECTIONS: ClassVar[int]
    ERROR_NOT_PERMITTED: ClassVar[int]
    ERROR_PREVIOUS_REQUEST_EXISTS: ClassVar[int]
    ERROR_REQUEST_TIME_OUT: ClassVar[int]
    ERROR_SERVICE_UNAVAILABLE: ClassVar[int]
    ERROR_UNSPECIFIED: ClassVar[int]
    @overload
    def __init__(self, arg0: str) -> None: ...
    @overload
    def __init__(self, arg0: str, arg1: int) -> None: ...
    @overload
    def __init__(self, arg0: str, arg1: int, arg2: Throwable) -> None: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, arg0: Parcel, arg1: int) -> None: ...
    def getCode(self) -> int: ...
