from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel
from android.os.Parcelable.Creator import Creator

class zzc:
    CREATOR: ClassVar[Creator]
    zza: str
    zzb: str
    def __init__(self, arg0: str, arg1: str) -> None: ...
    def writeToParcel(self, arg0: Parcel, arg1: int) -> None: ...
