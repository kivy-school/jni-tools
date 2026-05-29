from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel

class DhcpInfo:
    CREATOR: ClassVar[Any]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    dns1: int
    dns2: int
    gateway: int
    ipAddress: int
    leaseDuration: int
    netmask: int
    serverAddress: int
    def __init__(self) -> None: ...
    def toString(self) -> str: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...
