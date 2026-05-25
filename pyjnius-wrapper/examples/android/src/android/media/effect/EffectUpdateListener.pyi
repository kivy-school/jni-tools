from typing import Any, ClassVar, overload
from android.media.effect.Effect import Effect

class EffectUpdateListener:
    def onEffectUpdated(self, arg0: Effect, arg1: Any) -> None: ...
