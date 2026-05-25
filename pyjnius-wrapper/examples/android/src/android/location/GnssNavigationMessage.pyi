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

class GnssNavigationMessage:
    CREATOR: ClassVar[Creator]
    STATUS_PARITY_PASSED: ClassVar[int]
    STATUS_PARITY_REBUILT: ClassVar[int]
    STATUS_UNKNOWN: ClassVar[int]
    TYPE_BDS_CNAV1: ClassVar[int]
    TYPE_BDS_CNAV2: ClassVar[int]
    TYPE_BDS_D1: ClassVar[int]
    TYPE_BDS_D2: ClassVar[int]
    TYPE_GAL_F: ClassVar[int]
    TYPE_GAL_I: ClassVar[int]
    TYPE_GLO_L1CA: ClassVar[int]
    TYPE_GPS_CNAV2: ClassVar[int]
    TYPE_GPS_L1CA: ClassVar[int]
    TYPE_GPS_L2CNAV: ClassVar[int]
    TYPE_GPS_L5CNAV: ClassVar[int]
    TYPE_IRN_L1: ClassVar[int]
    TYPE_IRN_L5: ClassVar[int]
    TYPE_IRN_L5CA: ClassVar[int]
    TYPE_QZS_L1CA: ClassVar[int]
    TYPE_SBS: ClassVar[int]
    TYPE_UNKNOWN: ClassVar[int]
    def getType(self) -> int: ...
    def getSvid(self) -> int: ...
    def getMessageId(self) -> int: ...
    def getSubmessageId(self) -> int: ...
    def getData(self) -> list[int]: ...
    def getStatus(self) -> int: ...
    def writeToParcel(self, arg0: Parcel, arg1: int) -> None: ...
    def describeContents(self) -> int: ...
    def toString(self) -> str: ...

    class Callback:
        STATUS_LOCATION_DISABLED: ClassVar[int]
        STATUS_NOT_SUPPORTED: ClassVar[int]
        STATUS_READY: ClassVar[int]
        def __init__(self) -> None: ...
        def onGnssNavigationMessageReceived(self, arg0: "GnssNavigationMessage") -> None: ...
        def onStatusChanged(self, arg0: int) -> None: ...
