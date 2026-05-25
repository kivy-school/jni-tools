from typing import Any, ClassVar, overload
from android.content.ClipData import ClipData
from android.content.ClipDescription import ClipDescription
from android.os.Parcel import Parcel

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

class DragEvent:
    ACTION_DRAG_ENDED: ClassVar[int]
    ACTION_DRAG_ENTERED: ClassVar[int]
    ACTION_DRAG_EXITED: ClassVar[int]
    ACTION_DRAG_LOCATION: ClassVar[int]
    ACTION_DRAG_STARTED: ClassVar[int]
    ACTION_DROP: ClassVar[int]
    CREATOR: ClassVar[Creator]
    def getAction(self) -> int: ...
    def getX(self) -> float: ...
    def getY(self) -> float: ...
    def getClipData(self) -> ClipData: ...
    def getClipDescription(self) -> ClipDescription: ...
    def getLocalState(self) -> Any: ...
    def getResult(self) -> bool: ...
    def toString(self) -> str: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, arg0: Parcel, arg1: int) -> None: ...
