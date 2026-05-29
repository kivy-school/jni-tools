from typing import Any, ClassVar, overload
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

class CommandResponse:
    CREATOR: ClassVar[Creator]
    RESPONSE_TYPE_JSON: ClassVar[str]
    RESPONSE_TYPE_XML: ClassVar[str]
    def __init__(self, arg0: int, arg1: int, arg2: int, arg3: str, arg4: str) -> None: ...
    def getResponse(self) -> str: ...
    def getResponseType(self) -> str: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, arg0: Parcel, arg1: int) -> None: ...
