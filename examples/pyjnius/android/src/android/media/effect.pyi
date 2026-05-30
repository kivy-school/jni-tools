from typing import Any, ClassVar, overload
from android.media.effect.Effect import Effect

class EffectUpdateListener:
    def onEffectUpdated(self, p0: Effect, p1: Any) -> None: ...

from typing import Any, ClassVar, overload
from android.media.effect.Effect import Effect

class EffectFactory:
    EFFECT_AUTOFIX: ClassVar[str]
    EFFECT_BACKDROPPER: ClassVar[str]
    EFFECT_BITMAPOVERLAY: ClassVar[str]
    EFFECT_BLACKWHITE: ClassVar[str]
    EFFECT_BRIGHTNESS: ClassVar[str]
    EFFECT_CONTRAST: ClassVar[str]
    EFFECT_CROP: ClassVar[str]
    EFFECT_CROSSPROCESS: ClassVar[str]
    EFFECT_DOCUMENTARY: ClassVar[str]
    EFFECT_DUOTONE: ClassVar[str]
    EFFECT_FILLLIGHT: ClassVar[str]
    EFFECT_FISHEYE: ClassVar[str]
    EFFECT_FLIP: ClassVar[str]
    EFFECT_GRAIN: ClassVar[str]
    EFFECT_GRAYSCALE: ClassVar[str]
    EFFECT_LOMOISH: ClassVar[str]
    EFFECT_NEGATIVE: ClassVar[str]
    EFFECT_POSTERIZE: ClassVar[str]
    EFFECT_REDEYE: ClassVar[str]
    EFFECT_ROTATE: ClassVar[str]
    EFFECT_SATURATE: ClassVar[str]
    EFFECT_SEPIA: ClassVar[str]
    EFFECT_SHARPEN: ClassVar[str]
    EFFECT_STRAIGHTEN: ClassVar[str]
    EFFECT_TEMPERATURE: ClassVar[str]
    EFFECT_TINT: ClassVar[str]
    EFFECT_VIGNETTE: ClassVar[str]
    def createEffect(self, p0: str) -> Effect: ...
    @staticmethod
    def isEffectSupported(p0: str) -> bool: ...

from typing import Any, ClassVar, overload
from android.media.effect.EffectFactory import EffectFactory

class EffectContext:
    @staticmethod
    def createWithCurrentGlContext() -> "EffectContext": ...
    def getFactory(self) -> EffectFactory: ...
    def release(self) -> None: ...

from typing import Any, ClassVar, overload
from android.media.effect.EffectUpdateListener import EffectUpdateListener

class Effect:
    def __init__(self) -> None: ...
    def setUpdateListener(self, p0: EffectUpdateListener) -> None: ...
    def setParameter(self, p0: str, p1: Any) -> None: ...
    def getName(self) -> str: ...
    def apply(self, p0: int, p1: int, p2: int, p3: int) -> None: ...
    def release(self) -> None: ...

