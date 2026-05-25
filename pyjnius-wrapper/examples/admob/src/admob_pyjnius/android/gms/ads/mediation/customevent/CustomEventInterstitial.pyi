from typing import Any, ClassVar, overload
from android.content.Context import Context
from android.gms.ads.mediation.MediationAdRequest import MediationAdRequest
from android.gms.ads.mediation.customevent.CustomEventInterstitialListener import CustomEventInterstitialListener
from android.os.Bundle import Bundle

class CustomEventInterstitial:
    def requestInterstitialAd(self, arg0: Context, arg1: CustomEventInterstitialListener, arg2: str, arg3: MediationAdRequest, arg4: Bundle) -> None: ...
    def showInterstitial(self) -> None: ...
