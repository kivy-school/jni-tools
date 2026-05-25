from typing import Any, ClassVar, overload
from android.content.Context import Context
from android.gms.ads.AdSize import AdSize
from android.gms.ads.mediation.MediationAdRequest import MediationAdRequest
from android.gms.ads.mediation.customevent.CustomEventBannerListener import CustomEventBannerListener
from android.os.Bundle import Bundle

class CustomEventBanner:
    def requestBannerAd(self, arg0: Context, arg1: CustomEventBannerListener, arg2: str, arg3: AdSize, arg4: MediationAdRequest, arg5: Bundle) -> None: ...
