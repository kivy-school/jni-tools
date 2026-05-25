from typing import Any, ClassVar, overload
from android.content.Context import Context
from android.gms.ads.mediation.MediationNativeListener import MediationNativeListener
from android.gms.ads.mediation.NativeMediationAdRequest import NativeMediationAdRequest
from android.os.Bundle import Bundle

class MediationNativeAdapter:
    def requestNativeAd(self, arg0: Context, arg1: MediationNativeListener, arg2: Bundle, arg3: NativeMediationAdRequest, arg4: Bundle) -> None: ...
