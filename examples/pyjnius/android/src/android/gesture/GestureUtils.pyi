from typing import Any, ClassVar, overload
from android.gesture.Gesture import Gesture
from android.gesture.GestureStroke import GestureStroke
from android.gesture.OrientedBoundingBox import OrientedBoundingBox

class GestureUtils:
    @overload
    @staticmethod
    def spatialSampling(p0: Gesture, p1: int) -> Any: ...
    @overload
    @staticmethod
    def spatialSampling(p0: Gesture, p1: int, p2: bool) -> Any: ...
    @staticmethod
    def temporalSampling(p0: GestureStroke, p1: int) -> Any: ...
    @overload
    @staticmethod
    def computeOrientedBoundingBox(p0: list) -> OrientedBoundingBox: ...
    @overload
    @staticmethod
    def computeOrientedBoundingBox(p0: Any) -> OrientedBoundingBox: ...
