from typing import Any, ClassVar, overload
from android.gms.ads.internal.client.zzc import zzc
from android.gms.ads.internal.client.zzft import zzft
from android.location.Location import Location
from android.os.Bundle import Bundle
from android.os.Parcel import Parcel
from android.os.Parcelable.Creator import Creator

class zzm:
    CREATOR: ClassVar[Creator]
    zza: int
    zzb: int
    zzc: Bundle
    zzd: int
    zze: list
    zzf: bool
    zzg: int
    zzh: bool
    zzi: str
    zzj: zzft
    zzk: Location
    zzl: str
    zzm: Bundle
    zzn: Bundle
    zzo: list
    zzp: str
    zzq: str
    zzr: bool
    zzs: zzc
    zzt: int
    zzu: str
    zzv: list
    zzw: int
    zzx: str
    zzy: int
    zzz: int
    zzA: int
    zzB: int
    zzC: Bundle
    def __init__(self, arg0: int, arg1: int, arg2: Bundle, arg3: int, arg4: list, arg5: bool, arg6: int, arg7: bool, arg8: str, arg9: zzft, arg10: Location, arg11: str, arg12: Bundle, arg13: Bundle, arg14: list, arg15: str, arg16: str, arg17: bool, arg18: zzc, arg19: int, arg20: str, arg21: list, arg22: int, arg23: str, arg24: int, arg25: int, arg26: int, arg27: int) -> None: ...
    def writeToParcel(self, arg0: Parcel, arg1: int) -> None: ...
    def equals(self, arg0: Any) -> bool: ...
    def zza(self, arg0: Any) -> bool: ...
    def hashCode(self) -> int: ...
    def zzb(self) -> bool: ...
    def zzc(self) -> bool: ...
    def zzd(self) -> bool: ...
