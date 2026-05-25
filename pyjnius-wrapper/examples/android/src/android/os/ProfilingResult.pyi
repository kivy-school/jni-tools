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

class ProfilingResult:
    CREATOR: ClassVar[Creator]
    ERROR_FAILED_EXECUTING: ClassVar[int]
    ERROR_FAILED_INVALID_REQUEST: ClassVar[int]
    ERROR_FAILED_NO_DISK_SPACE: ClassVar[int]
    ERROR_FAILED_POST_PROCESSING: ClassVar[int]
    ERROR_FAILED_PROFILING_IN_PROGRESS: ClassVar[int]
    ERROR_FAILED_RATE_LIMIT_PROCESS: ClassVar[int]
    ERROR_FAILED_RATE_LIMIT_SYSTEM: ClassVar[int]
    ERROR_NONE: ClassVar[int]
    ERROR_UNKNOWN: ClassVar[int]
    def writeToParcel(self, arg0: Parcel, arg1: int) -> None: ...
    def describeContents(self) -> int: ...
    def getErrorCode(self) -> int: ...
    def getResultFilePath(self) -> str: ...
    def getTag(self) -> str: ...
    def getErrorMessage(self) -> str: ...
