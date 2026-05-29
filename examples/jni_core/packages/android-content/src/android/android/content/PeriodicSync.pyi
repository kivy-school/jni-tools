from typing import Any, ClassVar, overload
from android.accounts.Account import Account
from android.os.Bundle import Bundle
from android.os.Parcel import Parcel

class PeriodicSync:
    CREATOR: ClassVar[Any]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    account: Account
    authority: str
    extras: Bundle
    period: int
    def __init__(self, p0: Account, p1: str, p2: Bundle, p3: int) -> None: ...
    def equals(self, p0: Any) -> bool: ...
    def toString(self) -> str: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...
