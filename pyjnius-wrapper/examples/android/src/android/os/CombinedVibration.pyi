from typing import Any, ClassVar, overload
from android.os.VibrationEffect import VibrationEffect

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

class CombinedVibration:
    CREATOR: ClassVar[Creator]
    @staticmethod
    def createParallel(arg0: VibrationEffect) -> "CombinedVibration": ...
    @staticmethod
    def startParallel() -> "ParallelCombination": ...
    def describeContents(self) -> int: ...

    class ParallelCombination:
        def addVibrator(self, arg0: int, arg1: VibrationEffect) -> "ParallelCombination": ...
        def combine(self) -> "CombinedVibration": ...
