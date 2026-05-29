from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel

class GnssNavigationMessage:
    CREATOR: ClassVar[Any]
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
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    def getStatus(self) -> int: ...
    def getMessageId(self) -> int: ...
    def getSubmessageId(self) -> int: ...
    def getSvid(self) -> int: ...
    def toString(self) -> str: ...
    def getType(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...
    def describeContents(self) -> int: ...
    def getData(self) -> Any: ...

    class Callback:
        STATUS_LOCATION_DISABLED: ClassVar[int]
        STATUS_NOT_SUPPORTED: ClassVar[int]
        STATUS_READY: ClassVar[int]
        def __init__(self) -> None: ...
        def onGnssNavigationMessageReceived(self, p0: "GnssNavigationMessage") -> None: ...
        def onStatusChanged(self, p0: int) -> None: ...
