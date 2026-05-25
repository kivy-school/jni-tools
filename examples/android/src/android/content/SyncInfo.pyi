from typing import Any, ClassVar, overload
from android.accounts.Account import Account
from android.os.Parcel import Parcel

class SyncInfo:
    account: Account
    authority: str
    startTime: int
    def describeContents(self) -> int: ...
    def writeToParcel(self, arg0: Parcel, arg1: int) -> None: ...
