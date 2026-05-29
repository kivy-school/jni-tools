from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel
from android.os.Parcelable.Creator import Creator

class zzbsi:
    CREATOR: ClassVar[Creator]
    zza: int
    zzb: int
    zzc: str
    zzd: int
    def __init__(self, arg0: int, arg1: int, arg2: str, arg3: int) -> None: ...
    def writeToParcel(self, arg0: Parcel, arg1: int) -> None: ...
