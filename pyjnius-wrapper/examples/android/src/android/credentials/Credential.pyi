from typing import Any, ClassVar, overload
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

class Credential:
    CREATOR: ClassVar[Creator]
    TYPE_PASSWORD_CREDENTIAL: ClassVar[str]
    def __init__(self, arg0: str, arg1: Bundle) -> None: ...
    def getType(self) -> str: ...
    def getData(self) -> Bundle: ...
    def writeToParcel(self, arg0: Parcel, arg1: int) -> None: ...
    def describeContents(self) -> int: ...
    def toString(self) -> str: ...
