from typing import Any, ClassVar, overload
from android.app.PendingIntent import PendingIntent
from android.graphics.drawable.Icon import Icon
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

class ChooserAction:
    CREATOR: ClassVar[Creator]
    def getLabel(self) -> str: ...
    def getIcon(self) -> Icon: ...
    def getAction(self) -> PendingIntent: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, arg0: Parcel, arg1: int) -> None: ...
    def toString(self) -> str: ...

    class Builder:
        def __init__(self, arg0: Icon, arg1: str, arg2: PendingIntent) -> None: ...
        def build(self) -> "ChooserAction": ...
