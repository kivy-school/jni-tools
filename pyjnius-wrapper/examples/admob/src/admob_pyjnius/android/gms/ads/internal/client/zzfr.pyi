from typing import Any, ClassVar, overload
from android.gms.ads.RequestConfiguration import RequestConfiguration
from android.os.Parcel import Parcel
from android.os.Parcelable.Creator import Creator

class zzfr:
    CREATOR: ClassVar[Creator]
    zza: int
    zzb: int
    @overload
    def __init__(self, arg0: int, arg1: int) -> None: ...
    @overload
    def __init__(self, arg0: RequestConfiguration) -> None: ...
    def writeToParcel(self, arg0: Parcel, arg1: int) -> None: ...
