from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel

class ExtractedTextRequest:
    CREATOR: ClassVar[Any]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    flags: int
    hintMaxChars: int
    hintMaxLines: int
    token: int
    def __init__(self) -> None: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...
    def describeContents(self) -> int: ...
