from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel

class CallException:
    CODE_CALL_CANNOT_BE_SET_TO_ACTIVE: ClassVar[int]
    CODE_CALL_IS_NOT_BEING_TRACKED: ClassVar[int]
    CODE_CALL_NOT_PERMITTED_AT_PRESENT_TIME: ClassVar[int]
    CODE_CANNOT_HOLD_CURRENT_ACTIVE_CALL: ClassVar[int]
    CODE_ERROR_UNKNOWN: ClassVar[int]
    CODE_OPERATION_TIMED_OUT: ClassVar[int]
    CREATOR: ClassVar[Any]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    def __init__(self, p0: str, p1: int) -> None: ...
    def getCode(self) -> int: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...
