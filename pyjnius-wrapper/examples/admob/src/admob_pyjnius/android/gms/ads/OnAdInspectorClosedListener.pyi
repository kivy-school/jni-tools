from typing import Any, ClassVar, overload
from android.gms.ads.AdInspectorError import AdInspectorError

class OnAdInspectorClosedListener:
    def onAdInspectorClosed(self, arg0: AdInspectorError) -> None: ...
