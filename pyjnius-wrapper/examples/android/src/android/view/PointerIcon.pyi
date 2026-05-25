from typing import Any, ClassVar, overload
from android.content.Context import Context
from android.content.res.Resources import Resources
from android.graphics.Bitmap import Bitmap
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

class PointerIcon:
    CREATOR: ClassVar[Creator]
    TYPE_ALIAS: ClassVar[int]
    TYPE_ALL_SCROLL: ClassVar[int]
    TYPE_ARROW: ClassVar[int]
    TYPE_CELL: ClassVar[int]
    TYPE_CONTEXT_MENU: ClassVar[int]
    TYPE_COPY: ClassVar[int]
    TYPE_CROSSHAIR: ClassVar[int]
    TYPE_DEFAULT: ClassVar[int]
    TYPE_GRAB: ClassVar[int]
    TYPE_GRABBING: ClassVar[int]
    TYPE_HAND: ClassVar[int]
    TYPE_HANDWRITING: ClassVar[int]
    TYPE_HELP: ClassVar[int]
    TYPE_HORIZONTAL_DOUBLE_ARROW: ClassVar[int]
    TYPE_NO_DROP: ClassVar[int]
    TYPE_NULL: ClassVar[int]
    TYPE_TEXT: ClassVar[int]
    TYPE_TOP_LEFT_DIAGONAL_DOUBLE_ARROW: ClassVar[int]
    TYPE_TOP_RIGHT_DIAGONAL_DOUBLE_ARROW: ClassVar[int]
    TYPE_VERTICAL_DOUBLE_ARROW: ClassVar[int]
    TYPE_VERTICAL_TEXT: ClassVar[int]
    TYPE_WAIT: ClassVar[int]
    TYPE_ZOOM_IN: ClassVar[int]
    TYPE_ZOOM_OUT: ClassVar[int]
    @staticmethod
    def getSystemIcon(arg0: Context, arg1: int) -> "PointerIcon": ...
    @staticmethod
    def create(arg0: Bitmap, arg1: float, arg2: float) -> "PointerIcon": ...
    @staticmethod
    def load(arg0: Resources, arg1: int) -> "PointerIcon": ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, arg0: Parcel, arg1: int) -> None: ...
    def equals(self, arg0: Any) -> bool: ...
    def toString(self) -> str: ...
