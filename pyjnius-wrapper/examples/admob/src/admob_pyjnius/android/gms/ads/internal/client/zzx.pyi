from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel
from android.os.Parcelable.Creator import Creator

class zzx:
    CREATOR: ClassVar[Creator]
    zza: int
    def __init__(self, arg0: int) -> None: ...
    def writeToParcel(self, arg0: Parcel, arg1: int) -> None: ...
