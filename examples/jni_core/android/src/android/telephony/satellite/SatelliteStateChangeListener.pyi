from typing import Any, ClassVar, overload

class SatelliteStateChangeListener:
    def onEnabledStateChanged(self, p0: bool) -> None: ...
