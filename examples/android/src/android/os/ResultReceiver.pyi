from typing import Any, ClassVar, overload
from android.os.Bundle import Bundle
from android.os.Handler import Handler
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

class ResultReceiver:
    CREATOR: ClassVar[Creator]
    def __init__(self, arg0: Handler) -> None: ...
    def send(self, arg0: int, arg1: Bundle) -> None: ...
    def onReceiveResult(self, arg0: int, arg1: Bundle) -> None: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, arg0: Parcel, arg1: int) -> None: ...
