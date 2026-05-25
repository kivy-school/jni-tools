from typing import Any, ClassVar, overload
from android.gms.ads.formats.NativeAdOptions import NativeAdOptions
from android.gms.ads.internal.client.zzfw import zzfw
from android.gms.ads.nativead.NativeAdOptions import NativeAdOptions
from android.os.Parcel import Parcel
from android.os.Parcelable.Creator import Creator

class zzbma:
    CREATOR: ClassVar[Creator]
    zza: int
    zzb: bool
    zzc: int
    zzd: bool
    zze: int
    zzf: zzfw
    zzg: bool
    zzh: int
    zzi: int
    zzj: bool
    zzk: int
    @overload
    def __init__(self, arg0: NativeAdOptions) -> None: ...
    @overload
    def __init__(self, arg0: int, arg1: bool, arg2: int, arg3: bool, arg4: int, arg5: zzfw, arg6: bool, arg7: int, arg8: int, arg9: bool, arg10: int) -> None: ...
    def writeToParcel(self, arg0: Parcel, arg1: int) -> None: ...
    @staticmethod
    def zza(arg0: "zzbma") -> NativeAdOptions: ...
