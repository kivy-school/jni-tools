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
