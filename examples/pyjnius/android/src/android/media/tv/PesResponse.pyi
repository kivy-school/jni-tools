from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel

class PesResponse:
    CREATOR: ClassVar[Any]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    CREATOR: ClassVar[Any]
    RESPONSE_RESULT_CANCEL: ClassVar[int]
    RESPONSE_RESULT_ERROR: ClassVar[int]
    RESPONSE_RESULT_OK: ClassVar[int]
    def __init__(self, p0: int, p1: int, p2: int, p3: str) -> None: ...
    def getSharedFilterToken(self) -> str: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...
    def describeContents(self) -> int: ...
