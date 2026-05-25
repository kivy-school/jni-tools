from typing import Any, ClassVar, overload

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Creator:
    """Forward declaration for ``android.os.Parcelable.Creator``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.os.Parcelable.Creator')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/os/Parcelable/Creator
    """
    ...

class VibrationEffect:
    CREATOR: ClassVar[Creator]
    DEFAULT_AMPLITUDE: ClassVar[int]
    EFFECT_CLICK: ClassVar[int]
    EFFECT_DOUBLE_CLICK: ClassVar[int]
    EFFECT_HEAVY_CLICK: ClassVar[int]
    EFFECT_TICK: ClassVar[int]
    @staticmethod
    def createOneShot(arg0: int, arg1: int) -> "VibrationEffect": ...
    @overload
    @staticmethod
    def createWaveform(arg0: list[int], arg1: int) -> "VibrationEffect": ...
    @overload
    @staticmethod
    def createWaveform(arg0: list[int], arg1: list[int], arg2: int) -> "VibrationEffect": ...
    @staticmethod
    def createPredefined(arg0: int) -> "VibrationEffect": ...
    @staticmethod
    def startComposition() -> "Composition": ...
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
        def addPrimitive(self, arg0: int) -> "Composition": ...
        @overload
        def addPrimitive(self, arg0: int, arg1: float) -> "Composition": ...
        @overload
        def addPrimitive(self, arg0: int, arg1: float, arg2: int) -> "Composition": ...
        def compose(self) -> "VibrationEffect": ...
