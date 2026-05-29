from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel

class ExtractedText:
    CREATOR: ClassVar[Any]
    FLAG_SELECTING: ClassVar[int]
    FLAG_SINGLE_LINE: ClassVar[int]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    flags: int
    hint: str
    partialEndOffset: int
    partialStartOffset: int
    selectionEnd: int
    selectionStart: int
    startOffset: int
    text: str
    def __init__(self) -> None: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...
