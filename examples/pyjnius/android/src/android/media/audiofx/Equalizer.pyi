from typing import Any, ClassVar, overload
from java.util.UUID import UUID

class Equalizer:
    PARAM_BAND_FREQ_RANGE: ClassVar[int]
    PARAM_BAND_LEVEL: ClassVar[int]
    PARAM_CENTER_FREQ: ClassVar[int]
    PARAM_CURRENT_PRESET: ClassVar[int]
    PARAM_GET_BAND: ClassVar[int]
    PARAM_GET_NUM_OF_PRESETS: ClassVar[int]
    PARAM_GET_PRESET_NAME: ClassVar[int]
    PARAM_LEVEL_RANGE: ClassVar[int]
    PARAM_NUM_BANDS: ClassVar[int]
    PARAM_STRING_SIZE_MAX: ClassVar[int]
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
    def getBand(self, p0: int) -> int: ...
    def getBandFreqRange(self, p0: int) -> Any: ...
    def getBandLevel(self, p0: int) -> int: ...
    def getBandLevelRange(self) -> Any: ...
    def getCenterFreq(self, p0: int) -> int: ...
    def getCurrentPreset(self) -> int: ...
    def getNumberOfBands(self) -> int: ...
    def getNumberOfPresets(self) -> int: ...
    def getPresetName(self, p0: int) -> str: ...
    def setBandLevel(self, p0: int, p1: int) -> None: ...
    def usePreset(self, p0: int) -> None: ...
    def setParameterListener(self, p0: Any) -> None: ...
    def getProperties(self) -> Any: ...
    def setProperties(self, p0: Any) -> None: ...

    class Settings:
        bandLevels: Any
        curPreset: int
        numBands: int
        @overload
        def __init__(self) -> None: ...
        @overload
        def __init__(self, p0: str) -> None: ...
        def toString(self) -> str: ...

    class OnParameterChangeListener:
        def onParameterChange(self, p0: "Equalizer", p1: int, p2: int, p3: int, p4: int) -> None: ...
