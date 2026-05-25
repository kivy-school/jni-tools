from typing import Any, ClassVar, overload
from android.content.ComponentName import ComponentName
from android.content.Context import Context
from android.content.pm.ServiceInfo import ServiceInfo
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

class TvInteractiveAppServiceInfo:
    CREATOR: ClassVar[Creator]
    INTERACTIVE_APP_TYPE_ATSC: ClassVar[int]
    INTERACTIVE_APP_TYPE_GINGA: ClassVar[int]
    INTERACTIVE_APP_TYPE_HBBTV: ClassVar[int]
    INTERACTIVE_APP_TYPE_OTHER: ClassVar[int]
    INTERACTIVE_APP_TYPE_TARGETED_AD: ClassVar[int]
    def __init__(self, arg0: Context, arg1: ComponentName) -> None: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, arg0: Parcel, arg1: int) -> None: ...
    def getId(self) -> str: ...
    def getServiceInfo(self) -> ServiceInfo: ...
    def getSupportedTypes(self) -> int: ...
    def getCustomSupportedTypes(self) -> list: ...
