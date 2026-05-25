from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel
from android.os.Parcelable.Creator import Creator

class zza:
    CREATOR: ClassVar[Creator]
    zza: str
    zzb: str
    zzc: str
    def __init__(self, arg0: str, arg1: str, arg2: str) -> None: ...
    def writeToParcel(self, arg0: Parcel, arg1: int) -> None: ...
