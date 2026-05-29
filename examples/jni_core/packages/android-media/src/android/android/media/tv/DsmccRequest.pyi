from typing import Any, ClassVar, overload
from android.net.Uri import Uri
from android.os.Parcel import Parcel

class DsmccRequest:
    CREATOR: ClassVar[Any]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    CREATOR: ClassVar[Any]
    REQUEST_OPTION_AUTO_UPDATE: ClassVar[int]
    REQUEST_OPTION_ONESHOT: ClassVar[int]
    REQUEST_OPTION_ONEWAY: ClassVar[int]
    REQUEST_OPTION_REPEAT: ClassVar[int]
    def __init__(self, p0: int, p1: int, p2: Uri) -> None: ...
    def getUri(self) -> Uri: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...
    def describeContents(self) -> int: ...
