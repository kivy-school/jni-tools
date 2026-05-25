from typing import Any, ClassVar, overload

class VibrationEffect:
    CREATOR: ClassVar[Any]
    DEFAULT_AMPLITUDE: ClassVar[int]
    EFFECT_CLICK: ClassVar[int]
    EFFECT_DOUBLE_CLICK: ClassVar[int]
    EFFECT_HEAVY_CLICK: ClassVar[int]
    EFFECT_TICK: ClassVar[int]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    @staticmethod
    def createOneShot(p0: int, p1: int) -> "VibrationEffect": ...
    @overload
    @staticmethod
    def createWaveform(p0: Any, p1: int) -> "VibrationEffect": ...
    @overload
    @staticmethod
    def createWaveform(p0: Any, p1: Any, p2: int) -> "VibrationEffect": ...
    @staticmethod
    def createPredefined(p0: int) -> "VibrationEffect": ...
    @staticmethod
    def startComposition() -> Any: ...
    def describeContents(self) -> int: ...

    class Composition:
        PRIMITIVE_CLICK: ClassVar[int]
        PRIMITIVE_LOW_TICK: ClassVar[int]
        PRIMITIVE_QUICK_FALL: ClassVar[int]
        PRIMITIVE_QUICK_RISE: ClassVar[int]
        PRIMITIVE_SLOW_RISE: ClassVar[int]
        PRIMITIVE_SPIN: ClassVar[int]
        PRIMITIVE_THUD: ClassVar[int]
        PRIMITIVE_TICK: ClassVar[int]
        @overload
        def addPrimitive(self, p0: int, p1: float) -> Any: ...
        @overload
        def addPrimitive(self, p0: int) -> Any: ...
        @overload
        def addPrimitive(self, p0: int, p1: float, p2: int) -> Any: ...
        def compose(self) -> "VibrationEffect": ...
