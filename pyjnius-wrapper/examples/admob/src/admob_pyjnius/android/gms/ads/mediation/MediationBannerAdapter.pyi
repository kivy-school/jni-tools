from typing import Any, ClassVar, overload
from android.content.Context import Context
from android.gms.ads.AdSize import AdSize
from android.gms.ads.mediation.MediationAdRequest import MediationAdRequest
from android.gms.ads.mediation.MediationBannerListener import MediationBannerListener
from android.os.Bundle import Bundle
from android.view.View import View

class MediationBannerAdapter:
    def requestBannerAd(self, arg0: Context, arg1: MediationBannerListener, arg2: Bundle, arg3: AdSize, arg4: MediationAdRequest, arg5: Bundle) -> None: ...
    def getBannerView(self) -> View: ...
