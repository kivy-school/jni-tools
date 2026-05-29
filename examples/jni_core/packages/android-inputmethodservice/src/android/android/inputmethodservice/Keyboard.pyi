from typing import Any, ClassVar, overload
from android.content.Context import Context
from android.content.res.Resources import Resources
from android.content.res.XmlResourceParser import XmlResourceParser
from android.graphics.drawable.Drawable import Drawable

class Keyboard:
    EDGE_BOTTOM: ClassVar[int]
    EDGE_LEFT: ClassVar[int]
    EDGE_RIGHT: ClassVar[int]
    EDGE_TOP: ClassVar[int]
    KEYCODE_ALT: ClassVar[int]
    KEYCODE_CANCEL: ClassVar[int]
    KEYCODE_DELETE: ClassVar[int]
    KEYCODE_DONE: ClassVar[int]
    KEYCODE_MODE_CHANGE: ClassVar[int]
    KEYCODE_SHIFT: ClassVar[int]
    @overload
    def __init__(self, p0: Context, p1: int, p2: str, p3: int, p4: int) -> None: ...
    @overload
    def __init__(self, p0: Context, p1: int, p2: int) -> None: ...
    @overload
    def __init__(self, p0: Context, p1: int, p2: int, p3: int, p4: int) -> None: ...
    @overload
    def __init__(self, p0: Context, p1: int) -> None: ...
    def getKeys(self) -> list: ...
    def getHeight(self) -> int: ...
    def getMinWidth(self) -> int: ...
    def getModifierKeys(self) -> list: ...
    def setShifted(self, p0: bool) -> bool: ...
    def isShifted(self) -> bool: ...
    def getShiftKeyIndex(self) -> int: ...
    def getNearestKeys(self, p0: int, p1: int) -> Any: ...

    class Row:
        defaultHeight: int
        defaultHorizontalGap: int
        defaultWidth: int
        mode: int
        rowEdgeFlags: int
        verticalGap: int
        @overload
        def __init__(self, p0: "Keyboard") -> None: ...
        @overload
        def __init__(self, p0: Resources, p1: "Keyboard", p2: XmlResourceParser) -> None: ...

    class Key:
        codes: Any
        edgeFlags: int
        gap: int
        height: int
        icon: Drawable
        iconPreview: Drawable
        label: str
        modifier: bool
        on: bool
        popupCharacters: str
        popupResId: int
        pressed: bool
        repeatable: bool
        sticky: bool
        text: str
        width: int
        x: int
        y: int
        @overload
        def __init__(self, p0: Any) -> None: ...
        @overload
        def __init__(self, p0: Resources, p1: Any, p2: int, p3: int, p4: XmlResourceParser) -> None: ...
        def getCurrentDrawableState(self) -> Any: ...
        def onPressed(self) -> None: ...
        def onReleased(self, p0: bool) -> None: ...
        def isInside(self, p0: int, p1: int) -> bool: ...
        def squaredDistanceFrom(self, p0: int, p1: int) -> int: ...
