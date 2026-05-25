from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel

class WifiP2pServiceInfo:
    SERVICE_TYPE_ALL: ClassVar[int]
    SERVICE_TYPE_BONJOUR: ClassVar[int]
    SERVICE_TYPE_UPNP: ClassVar[int]
    SERVICE_TYPE_VENDOR_SPECIFIC: ClassVar[int]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...
    def equals(self, p0: Any) -> bool: ...
    def hashCode(self) -> int: ...
