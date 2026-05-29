from typing import Any, ClassVar, overload
from android.content.Context import Context
from android.gms.ads.mediation.NativeMediationAdRequest import NativeMediationAdRequest
from android.gms.ads.mediation.customevent.CustomEventNativeListener import CustomEventNativeListener
from android.os.Bundle import Bundle

class CustomEventNative:
    def requestNativeAd(self, arg0: Context, arg1: CustomEventNativeListener, arg2: str, arg3: NativeMediationAdRequest, arg4: Bundle) -> None: ...
