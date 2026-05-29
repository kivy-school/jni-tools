from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel
from java.lang.Throwable import Throwable

class QueryLocationException:
    CREATOR: ClassVar[Any]
    ERROR_NOT_ALLOWED_FOR_NON_EMERGENCY_CONNECTIONS: ClassVar[int]
    ERROR_NOT_PERMITTED: ClassVar[int]
    ERROR_PREVIOUS_REQUEST_EXISTS: ClassVar[int]
    ERROR_REQUEST_TIME_OUT: ClassVar[int]
    ERROR_SERVICE_UNAVAILABLE: ClassVar[int]
    ERROR_UNSPECIFIED: ClassVar[int]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    @overload
    def __init__(self, p0: str, p1: int, p2: Throwable) -> None: ...
    @overload
    def __init__(self, p0: str, p1: int) -> None: ...
    @overload
    def __init__(self, p0: str) -> None: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...
    def describeContents(self) -> int: ...
    def getCode(self) -> int: ...
