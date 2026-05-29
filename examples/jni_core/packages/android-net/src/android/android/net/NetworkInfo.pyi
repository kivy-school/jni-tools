from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel

class NetworkInfo:
    CREATOR: ClassVar[Any]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    def __init__(self, p0: int, p1: int, p2: str, p3: str) -> None: ...
    def isRoaming(self) -> bool: ...
    def getSubtype(self) -> int: ...
    def getSubtypeName(self) -> str: ...
    def isConnectedOrConnecting(self) -> bool: ...
    def isFailover(self) -> bool: ...
    def getDetailedState(self) -> Any: ...
    def setDetailedState(self, p0: Any, p1: str, p2: str) -> None: ...
    def getExtraInfo(self) -> str: ...
    def isConnected(self) -> bool: ...
    def isAvailable(self) -> bool: ...
    def toString(self) -> str: ...
    def getTypeName(self) -> str: ...
    def getState(self) -> Any: ...
    def getType(self) -> int: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...
    def getReason(self) -> str: ...

    class State:
        CONNECTING: ClassVar["State"]
        CONNECTED: ClassVar["State"]
        SUSPENDED: ClassVar["State"]
        DISCONNECTING: ClassVar["State"]
        DISCONNECTED: ClassVar["State"]
        UNKNOWN: ClassVar["State"]
        CONNECTING: ClassVar[Any]
        CONNECTED: ClassVar[Any]
        SUSPENDED: ClassVar[Any]
        DISCONNECTING: ClassVar[Any]
        DISCONNECTED: ClassVar[Any]
        UNKNOWN: ClassVar[Any]
        @staticmethod
        def values() -> Any: ...
        @staticmethod
        def valueOf(p0: str) -> Any: ...

    class DetailedState:
        IDLE: ClassVar["DetailedState"]
        SCANNING: ClassVar["DetailedState"]
        CONNECTING: ClassVar["DetailedState"]
        AUTHENTICATING: ClassVar["DetailedState"]
        OBTAINING_IPADDR: ClassVar["DetailedState"]
        CONNECTED: ClassVar["DetailedState"]
        SUSPENDED: ClassVar["DetailedState"]
        DISCONNECTING: ClassVar["DetailedState"]
        DISCONNECTED: ClassVar["DetailedState"]
        FAILED: ClassVar["DetailedState"]
        BLOCKED: ClassVar["DetailedState"]
        VERIFYING_POOR_LINK: ClassVar["DetailedState"]
        CAPTIVE_PORTAL_CHECK: ClassVar["DetailedState"]
        IDLE: ClassVar[Any]
        SCANNING: ClassVar[Any]
        CONNECTING: ClassVar[Any]
        AUTHENTICATING: ClassVar[Any]
        OBTAINING_IPADDR: ClassVar[Any]
        CONNECTED: ClassVar[Any]
        SUSPENDED: ClassVar[Any]
        DISCONNECTING: ClassVar[Any]
        DISCONNECTED: ClassVar[Any]
        FAILED: ClassVar[Any]
        BLOCKED: ClassVar[Any]
        VERIFYING_POOR_LINK: ClassVar[Any]
        CAPTIVE_PORTAL_CHECK: ClassVar[Any]
        @staticmethod
        def values() -> Any: ...
        @staticmethod
        def valueOf(p0: str) -> Any: ...
