from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel

class WpsInfo:
    CREATOR: ClassVar[Any]
    DISPLAY: ClassVar[int]
    INVALID: ClassVar[int]
    KEYPAD: ClassVar[int]
    LABEL: ClassVar[int]
    PBC: ClassVar[int]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    BSSID: str
    pin: str
    setup: int
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, p0: "WpsInfo") -> None: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...
    def toString(self) -> str: ...
