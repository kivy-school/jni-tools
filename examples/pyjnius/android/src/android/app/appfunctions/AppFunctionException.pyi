from typing import Any, ClassVar, overload
from android.os.Bundle import Bundle
from android.os.Parcel import Parcel

class AppFunctionException:
    CREATOR: ClassVar[Any]
    ERROR_APP_UNKNOWN_ERROR: ClassVar[int]
    ERROR_CANCELLED: ClassVar[int]
    ERROR_CATEGORY_APP: ClassVar[int]
    ERROR_CATEGORY_REQUEST_ERROR: ClassVar[int]
    ERROR_CATEGORY_SYSTEM: ClassVar[int]
    ERROR_CATEGORY_UNKNOWN: ClassVar[int]
    ERROR_DENIED: ClassVar[int]
    ERROR_DISABLED: ClassVar[int]
    ERROR_ENTERPRISE_POLICY_DISALLOWED: ClassVar[int]
    ERROR_FUNCTION_NOT_FOUND: ClassVar[int]
    ERROR_INVALID_ARGUMENT: ClassVar[int]
    ERROR_SYSTEM_ERROR: ClassVar[int]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    @overload
    def __init__(self, p0: int, p1: str) -> None: ...
    @overload
    def __init__(self, p0: int, p1: str, p2: Bundle) -> None: ...
    def getErrorMessage(self) -> str: ...
    def getErrorCategory(self) -> int: ...
    def getExtras(self) -> Bundle: ...
    def getErrorCode(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...
    def describeContents(self) -> int: ...
