from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel
from android.os.ParcelFileDescriptor import ParcelFileDescriptor

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

class DsmccResponse:
    BIOP_MESSAGE_TYPE_DIRECTORY: ClassVar[str]
    BIOP_MESSAGE_TYPE_FILE: ClassVar[str]
    BIOP_MESSAGE_TYPE_SERVICE_GATEWAY: ClassVar[str]
    BIOP_MESSAGE_TYPE_STREAM: ClassVar[str]
    CREATOR: ClassVar[Creator]
    @overload
    def __init__(self, arg0: int, arg1: int, arg2: int, arg3: ParcelFileDescriptor) -> None: ...
    @overload
    def __init__(self, arg0: int, arg1: int, arg2: int, arg3: bool, arg4: list) -> None: ...
    @overload
    def __init__(self, arg0: int, arg1: int, arg2: int, arg3: list[int], arg4: list[str]) -> None: ...
    def getBiopMessageType(self) -> str: ...
    def getFile(self) -> ParcelFileDescriptor: ...
    def getChildList(self) -> list: ...
    def getStreamEventIds(self) -> list[int]: ...
    def getStreamEventNames(self) -> list[str]: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, arg0: Parcel, arg1: int) -> None: ...
