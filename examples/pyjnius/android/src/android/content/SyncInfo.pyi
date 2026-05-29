from typing import Any, ClassVar, overload
from android.accounts.Account import Account
from android.os.Parcel import Parcel

class SyncInfo:
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    account: Account
    authority: str
    startTime: int
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...
    def describeContents(self) -> int: ...
