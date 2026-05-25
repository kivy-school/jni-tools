from typing import Any, ClassVar, overload
from android.app.PendingIntent import PendingIntent
from android.app.RemoteInput import RemoteInput
from android.app.slice.SliceSpec import SliceSpec
from android.graphics.drawable.Icon import Icon
from android.net.Uri import Uri
from android.os.Bundle import Bundle
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

class Slice:
    CREATOR: ClassVar[Creator]
    EXTRA_RANGE_VALUE: ClassVar[str]
    EXTRA_TOGGLE_STATE: ClassVar[str]
    HINT_ACTIONS: ClassVar[str]
    HINT_ERROR: ClassVar[str]
    HINT_HORIZONTAL: ClassVar[str]
    HINT_KEYWORDS: ClassVar[str]
    HINT_LARGE: ClassVar[str]
    HINT_LAST_UPDATED: ClassVar[str]
    HINT_LIST: ClassVar[str]
    HINT_LIST_ITEM: ClassVar[str]
    HINT_NO_TINT: ClassVar[str]
    HINT_PARTIAL: ClassVar[str]
    HINT_PERMISSION_REQUEST: ClassVar[str]
    HINT_SEE_MORE: ClassVar[str]
    HINT_SELECTED: ClassVar[str]
    HINT_SHORTCUT: ClassVar[str]
    HINT_SUMMARY: ClassVar[str]
    HINT_TITLE: ClassVar[str]
    HINT_TTL: ClassVar[str]
    SUBTYPE_COLOR: ClassVar[str]
    SUBTYPE_CONTENT_DESCRIPTION: ClassVar[str]
    SUBTYPE_LAYOUT_DIRECTION: ClassVar[str]
    SUBTYPE_MAX: ClassVar[str]
    SUBTYPE_MESSAGE: ClassVar[str]
    SUBTYPE_MILLIS: ClassVar[str]
    SUBTYPE_PRIORITY: ClassVar[str]
    SUBTYPE_RANGE: ClassVar[str]
    SUBTYPE_SOURCE: ClassVar[str]
    SUBTYPE_TOGGLE: ClassVar[str]
    SUBTYPE_VALUE: ClassVar[str]
    def __init__(self, arg0: Parcel) -> None: ...
    def getSpec(self) -> SliceSpec: ...
    def getUri(self) -> Uri: ...
    def getItems(self) -> list: ...
    def getHints(self) -> list: ...
    def writeToParcel(self, arg0: Parcel, arg1: int) -> None: ...
    def describeContents(self) -> int: ...
    def isCallerNeeded(self) -> bool: ...
    def toString(self) -> str: ...

    class Builder:
        @overload
        def __init__(self, arg0: Uri, arg1: SliceSpec) -> None: ...
        @overload
        def __init__(self, arg0: "Builder") -> None: ...
        def setCallerNeeded(self, arg0: bool) -> "Builder": ...
        def addHints(self, arg0: list) -> "Builder": ...
        def addSubSlice(self, arg0: "Slice", arg1: str) -> "Builder": ...
        def addAction(self, arg0: PendingIntent, arg1: "Slice", arg2: str) -> "Builder": ...
        def addText(self, arg0: str, arg1: str, arg2: list) -> "Builder": ...
        def addIcon(self, arg0: Icon, arg1: str, arg2: list) -> "Builder": ...
        def addRemoteInput(self, arg0: RemoteInput, arg1: str, arg2: list) -> "Builder": ...
        def addInt(self, arg0: int, arg1: str, arg2: list) -> "Builder": ...
        def addLong(self, arg0: int, arg1: str, arg2: list) -> "Builder": ...
        def addBundle(self, arg0: Bundle, arg1: str, arg2: list) -> "Builder": ...
        def build(self) -> "Slice": ...
