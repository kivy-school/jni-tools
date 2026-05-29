from typing import Any, ClassVar, overload
from android.net.wifi.aware.PeerHandle import PeerHandle
from android.os.Parcel import Parcel

class ParcelablePeerHandle:
    CREATOR: ClassVar[Any]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    def __init__(self, p0: PeerHandle) -> None: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...
    def describeContents(self) -> int: ...
