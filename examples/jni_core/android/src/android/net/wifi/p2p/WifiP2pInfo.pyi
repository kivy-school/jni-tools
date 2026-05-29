from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel
from java.net.InetAddress import InetAddress

class WifiP2pInfo:
    CREATOR: ClassVar[Any]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    groupFormed: bool
    groupOwnerAddress: InetAddress
    isGroupOwner: bool
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, p0: "WifiP2pInfo") -> None: ...
    def toString(self) -> str: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...
    def describeContents(self) -> int: ...
