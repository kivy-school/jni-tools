from typing import Any, ClassVar, overload
from android.gms.ads.AdError import AdError

class MediationAppOpenAdCallback:
    def onAdFailedToShow(self, arg0: AdError) -> None: ...
