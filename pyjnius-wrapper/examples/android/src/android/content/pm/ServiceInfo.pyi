from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel
from android.util.Printer import Printer

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

class ServiceInfo:
    CREATOR: ClassVar[Creator]
    FLAG_ALLOW_SHARED_ISOLATED_PROCESS: ClassVar[int]
    FLAG_EXTERNAL_SERVICE: ClassVar[int]
    FLAG_ISOLATED_PROCESS: ClassVar[int]
    FLAG_SINGLE_USER: ClassVar[int]
    FLAG_STOP_WITH_TASK: ClassVar[int]
    FLAG_USE_APP_ZYGOTE: ClassVar[int]
    FOREGROUND_SERVICE_TYPE_CAMERA: ClassVar[int]
    FOREGROUND_SERVICE_TYPE_CONNECTED_DEVICE: ClassVar[int]
    FOREGROUND_SERVICE_TYPE_DATA_SYNC: ClassVar[int]
    FOREGROUND_SERVICE_TYPE_HEALTH: ClassVar[int]
    FOREGROUND_SERVICE_TYPE_LOCATION: ClassVar[int]
    FOREGROUND_SERVICE_TYPE_MANIFEST: ClassVar[int]
    FOREGROUND_SERVICE_TYPE_MEDIA_PLAYBACK: ClassVar[int]
    FOREGROUND_SERVICE_TYPE_MEDIA_PROCESSING: ClassVar[int]
    FOREGROUND_SERVICE_TYPE_MEDIA_PROJECTION: ClassVar[int]
    FOREGROUND_SERVICE_TYPE_MICROPHONE: ClassVar[int]
    FOREGROUND_SERVICE_TYPE_NONE: ClassVar[int]
    FOREGROUND_SERVICE_TYPE_PHONE_CALL: ClassVar[int]
    FOREGROUND_SERVICE_TYPE_REMOTE_MESSAGING: ClassVar[int]
    FOREGROUND_SERVICE_TYPE_SHORT_SERVICE: ClassVar[int]
    FOREGROUND_SERVICE_TYPE_SPECIAL_USE: ClassVar[int]
    FOREGROUND_SERVICE_TYPE_SYSTEM_EXEMPTED: ClassVar[int]
    flags: int
    permission: str
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, arg0: "ServiceInfo") -> None: ...
    def getForegroundServiceType(self) -> int: ...
    def dump(self, arg0: Printer, arg1: str) -> None: ...
    def toString(self) -> str: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, arg0: Parcel, arg1: int) -> None: ...
