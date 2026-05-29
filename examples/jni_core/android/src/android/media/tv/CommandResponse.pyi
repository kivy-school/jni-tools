from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel

class CommandResponse:
    CREATOR: ClassVar[Any]
    RESPONSE_TYPE_JSON: ClassVar[str]
    RESPONSE_TYPE_XML: ClassVar[str]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    CREATOR: ClassVar[Any]
    RESPONSE_RESULT_CANCEL: ClassVar[int]
    RESPONSE_RESULT_ERROR: ClassVar[int]
    RESPONSE_RESULT_OK: ClassVar[int]
    def __init__(self, p0: int, p1: int, p2: int, p3: str, p4: str) -> None: ...
    def getResponse(self) -> str: ...
    def getResponseType(self) -> str: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...
    def describeContents(self) -> int: ...
