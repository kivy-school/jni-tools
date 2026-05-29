from typing import Any, ClassVar, overload
from android.content.Context import Context
from android.content.res.Resources import Resources
from android.graphics.Bitmap import Bitmap
from android.os.Parcel import Parcel

class PointerIcon:
    CREATOR: ClassVar[Any]
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
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    def equals(self, p0: Any) -> bool: ...
    def toString(self) -> str: ...
    @staticmethod
    def load(p0: Resources, p1: int) -> "PointerIcon": ...
    @staticmethod
    def create(p0: Bitmap, p1: float, p2: float) -> "PointerIcon": ...
    @staticmethod
    def getSystemIcon(p0: Context, p1: int) -> "PointerIcon": ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...
