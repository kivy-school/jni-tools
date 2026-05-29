from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel

class ProfilingResult:
    CREATOR: ClassVar[Any]
    ERROR_FAILED_EXECUTING: ClassVar[int]
    ERROR_FAILED_INVALID_REQUEST: ClassVar[int]
    ERROR_FAILED_NO_DISK_SPACE: ClassVar[int]
    ERROR_FAILED_POST_PROCESSING: ClassVar[int]
    ERROR_FAILED_PROFILING_IN_PROGRESS: ClassVar[int]
    ERROR_FAILED_RATE_LIMIT_PROCESS: ClassVar[int]
    ERROR_FAILED_RATE_LIMIT_SYSTEM: ClassVar[int]
    ERROR_NONE: ClassVar[int]
    ERROR_UNKNOWN: ClassVar[int]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    def getResultFilePath(self) -> str: ...
    def getErrorMessage(self) -> str: ...
    def getTag(self) -> str: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...
    def getErrorCode(self) -> int: ...
