from typing import Any, ClassVar, overload
from android.gesture.Gesture import Gesture
from android.gesture.GestureStroke import GestureStroke
from android.gesture.OrientedBoundingBox import OrientedBoundingBox

class GestureUtils:
    @overload
    @staticmethod
    def spatialSampling(arg0: Gesture, arg1: int) -> list[float]: ...
    @overload
    @staticmethod
    def spatialSampling(arg0: Gesture, arg1: int, arg2: bool) -> list[float]: ...
    @staticmethod
    def temporalSampling(arg0: GestureStroke, arg1: int) -> list[float]: ...
    @overload
    @staticmethod
    def computeOrientedBoundingBox(arg0: list) -> OrientedBoundingBox: ...
    @overload
    @staticmethod
    def computeOrientedBoundingBox(arg0: list[float]) -> OrientedBoundingBox: ...
