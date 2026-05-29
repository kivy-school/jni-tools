from typing import Any, ClassVar, overload
from android.gms.ads.AdValue import AdValue

class OnPaidEventListener:
    def onPaidEvent(self, arg0: AdValue) -> None: ...
