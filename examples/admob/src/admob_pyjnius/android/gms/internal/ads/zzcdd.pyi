from typing import Any, ClassVar, overload
from android.gms.ads.rewarded.ServerSideVerificationOptions import ServerSideVerificationOptions
from android.os.Parcel import Parcel
from android.os.Parcelable.Creator import Creator

class zzcdd:
    CREATOR: ClassVar[Creator]
    zza: str
    zzb: str
    @overload
    def __init__(self, arg0: ServerSideVerificationOptions) -> None: ...
    @overload
    def __init__(self, arg0: str, arg1: str) -> None: ...
    def writeToParcel(self, arg0: Parcel, arg1: int) -> None: ...
