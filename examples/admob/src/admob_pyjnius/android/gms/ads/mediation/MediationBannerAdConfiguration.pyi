from typing import Any, ClassVar, overload
from android.content.Context import Context
from android.gms.ads.AdSize import AdSize
from android.location.Location import Location
from android.os.Bundle import Bundle

class MediationBannerAdConfiguration:
    def __init__(self, arg0: Context, arg1: str, arg2: Bundle, arg3: Bundle, arg4: bool, arg5: Location, arg6: int, arg7: int, arg8: str, arg9: AdSize, arg10: str) -> None: ...
    def getAdSize(self) -> AdSize: ...
