from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel

class CallEndpointException:
    CREATOR: ClassVar[Any]
    ERROR_ANOTHER_REQUEST: ClassVar[int]
    ERROR_ENDPOINT_DOES_NOT_EXIST: ClassVar[int]
    ERROR_REQUEST_TIME_OUT: ClassVar[int]
    ERROR_UNSPECIFIED: ClassVar[int]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    def __init__(self, p0: str, p1: int) -> None: ...
    def getCode(self) -> int: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...
