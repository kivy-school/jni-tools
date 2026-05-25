from typing import Any, ClassVar, overload
from android.gms.ads.initialization.InitializationStatus import InitializationStatus

class OnInitializationCompleteListener:
    def onInitializationComplete(self, arg0: InitializationStatus) -> None: ...
