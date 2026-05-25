from typing import Any, ClassVar, overload
from android.os.Bundle import Bundle
from android.os.Parcel import Parcel
from android.os.Parcelable.Creator import Creator

class zzbsg:
    CREATOR: ClassVar[Creator]
    zza: str
    zzb: Bundle
    def __init__(self, arg0: str, arg1: Bundle) -> None: ...
    def writeToParcel(self, arg0: Parcel, arg1: int) -> None: ...
