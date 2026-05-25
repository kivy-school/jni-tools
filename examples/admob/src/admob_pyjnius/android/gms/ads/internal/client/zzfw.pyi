from typing import Any, ClassVar, overload
from android.gms.ads.VideoOptions import VideoOptions
from android.os.Parcel import Parcel
from android.os.Parcelable.Creator import Creator

class zzfw:
    CREATOR: ClassVar[Creator]
    zza: bool
    zzb: bool
    zzc: bool
    @overload
    def __init__(self, arg0: VideoOptions) -> None: ...
    @overload
    def __init__(self, arg0: bool, arg1: bool, arg2: bool) -> None: ...
    def writeToParcel(self, arg0: Parcel, arg1: int) -> None: ...
