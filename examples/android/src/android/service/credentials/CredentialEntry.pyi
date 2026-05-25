from typing import Any, ClassVar, overload
from android.app.slice.Slice import Slice
from android.os.Parcel import Parcel
from android.service.credentials.BeginGetCredentialOption import BeginGetCredentialOption

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

class CredentialEntry:
    CREATOR: ClassVar[Creator]
    @overload
    def __init__(self, arg0: str, arg1: str, arg2: Slice) -> None: ...
    @overload
    def __init__(self, arg0: BeginGetCredentialOption, arg1: Slice) -> None: ...
    @overload
    def __init__(self, arg0: str, arg1: Slice) -> None: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, arg0: Parcel, arg1: int) -> None: ...
    def getBeginGetCredentialOptionId(self) -> str: ...
    def getType(self) -> str: ...
    def getSlice(self) -> Slice: ...
