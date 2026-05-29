from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel
from android.service.autofill.BatchUpdates import BatchUpdates
from android.service.autofill.OnClickAction import OnClickAction
from android.service.autofill.Transformation import Transformation
from android.service.autofill.Validator import Validator
from android.widget.RemoteViews import RemoteViews

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

class CustomDescription:
    CREATOR: ClassVar[Creator]
    def toString(self) -> str: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, arg0: Parcel, arg1: int) -> None: ...

    class Builder:
        def __init__(self, arg0: RemoteViews) -> None: ...
        def addChild(self, arg0: int, arg1: Transformation) -> "Builder": ...
        def batchUpdate(self, arg0: Validator, arg1: BatchUpdates) -> "Builder": ...
        def addOnClickAction(self, arg0: int, arg1: OnClickAction) -> "Builder": ...
        def build(self) -> "CustomDescription": ...
