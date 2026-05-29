from typing import Any, ClassVar, overload
from android.content.Context import Context
from android.gms.ads.nativead.NativeAdOptions import NativeAdOptions
from android.gms.internal.ads.zzbma import zzbma
from android.location.Location import Location
from android.os.Bundle import Bundle

class MediationNativeAdConfiguration:
    def __init__(self, arg0: Context, arg1: str, arg2: Bundle, arg3: Bundle, arg4: bool, arg5: Location, arg6: int, arg7: int, arg8: str, arg9: str, arg10: zzbma) -> None: ...
    def getNativeAdOptions(self) -> NativeAdOptions: ...
