from typing import Any, ClassVar, overload
from android.content.Context import Context
from android.gms.ads.mediation.MediationAdRequest import MediationAdRequest
from android.gms.ads.mediation.MediationInterstitialListener import MediationInterstitialListener
from android.os.Bundle import Bundle

class MediationInterstitialAdapter:
    def requestInterstitialAd(self, arg0: Context, arg1: MediationInterstitialListener, arg2: Bundle, arg3: MediationAdRequest, arg4: Bundle) -> None: ...
    def showInterstitial(self) -> None: ...
