from typing import Any, ClassVar, overload
from java.util.UUID import UUID

class BassBoost:
    PARAM_STRENGTH: ClassVar[int]
    PARAM_STRENGTH_SUPPORTED: ClassVar[int]
    ACTION_CLOSE_AUDIO_EFFECT_CONTROL_SESSION: ClassVar[str]
    ACTION_DISPLAY_AUDIO_EFFECT_CONTROL_PANEL: ClassVar[str]
    ACTION_OPEN_AUDIO_EFFECT_CONTROL_SESSION: ClassVar[str]
    ALREADY_EXISTS: ClassVar[int]
    CONTENT_TYPE_GAME: ClassVar[int]
    CONTENT_TYPE_MOVIE: ClassVar[int]
    CONTENT_TYPE_MUSIC: ClassVar[int]
    CONTENT_TYPE_VOICE: ClassVar[int]
    EFFECT_AUXILIARY: ClassVar[str]
    EFFECT_INSERT: ClassVar[str]
    EFFECT_POST_PROCESSING: ClassVar[str]
    EFFECT_PRE_PROCESSING: ClassVar[str]
    EFFECT_TYPE_AEC: ClassVar[UUID]
    EFFECT_TYPE_AGC: ClassVar[UUID]
    EFFECT_TYPE_BASS_BOOST: ClassVar[UUID]
    EFFECT_TYPE_DYNAMICS_PROCESSING: ClassVar[UUID]
    EFFECT_TYPE_ENV_REVERB: ClassVar[UUID]
    EFFECT_TYPE_EQUALIZER: ClassVar[UUID]
    EFFECT_TYPE_HAPTIC_GENERATOR: ClassVar[UUID]
    EFFECT_TYPE_LOUDNESS_ENHANCER: ClassVar[UUID]
    EFFECT_TYPE_NS: ClassVar[UUID]
    EFFECT_TYPE_PRESET_REVERB: ClassVar[UUID]
    EFFECT_TYPE_VIRTUALIZER: ClassVar[UUID]
    ERROR: ClassVar[int]
    ERROR_BAD_VALUE: ClassVar[int]
    ERROR_DEAD_OBJECT: ClassVar[int]
    ERROR_INVALID_OPERATION: ClassVar[int]
    ERROR_NO_INIT: ClassVar[int]
    ERROR_NO_MEMORY: ClassVar[int]
    EXTRA_AUDIO_SESSION: ClassVar[str]
    EXTRA_CONTENT_TYPE: ClassVar[str]
    EXTRA_PACKAGE_NAME: ClassVar[str]
    SUCCESS: ClassVar[int]
    def __init__(self, p0: int, p1: int) -> None: ...
    def setStrength(self, p0: int) -> None: ...
    def getRoundedStrength(self) -> int: ...
    def getStrengthSupported(self) -> bool: ...
    def setParameterListener(self, p0: Any) -> None: ...
    def getProperties(self) -> Any: ...
    def setProperties(self, p0: Any) -> None: ...

    class Settings:
        strength: int
        @overload
        def __init__(self) -> None: ...
        @overload
        def __init__(self, p0: str) -> None: ...
        def toString(self) -> str: ...

    class OnParameterChangeListener:
        def onParameterChange(self, p0: "BassBoost", p1: int, p2: int, p3: int) -> None: ...
