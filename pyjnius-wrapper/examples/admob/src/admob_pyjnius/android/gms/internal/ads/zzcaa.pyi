from typing import Any, ClassVar, overload
from android.os.IBinder import IBinder
from android.os.Parcel import Parcel
from android.os.Parcelable.Creator import Creator
from android.view.View import View

class zzcaa:
    CREATOR: ClassVar[Creator]
    zza: View
    zzb: dict
    def __init__(self, arg0: IBinder, arg1: IBinder) -> None: ...
    def writeToParcel(self, arg0: Parcel, arg1: int) -> None: ...
