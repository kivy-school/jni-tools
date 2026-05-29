from typing import Any, ClassVar, overload
from android.media.effect.Effect import Effect

class EffectUpdateListener:
    def onEffectUpdated(self, p0: Effect, p1: Any) -> None: ...
