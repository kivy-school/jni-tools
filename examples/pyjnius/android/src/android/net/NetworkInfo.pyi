from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel

class NetworkInfo:
    CREATOR: ClassVar[Any]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    def __init__(self, p0: int, p1: int, p2: str, p3: str) -> None: ...
    def isAvailable(self) -> bool: ...
    def isConnected(self) -> bool: ...
    def getSubtypeName(self) -> str: ...
    def getSubtype(self) -> int: ...
    def getExtraInfo(self) -> str: ...
    def isFailover(self) -> bool: ...
    def setDetailedState(self, p0: Any, p1: str, p2: str) -> None: ...
    def getDetailedState(self) -> Any: ...
    def isConnectedOrConnecting(self) -> bool: ...
    def toString(self) -> str: ...
    def getTypeName(self) -> str: ...
    def getState(self) -> Any: ...
    def getType(self) -> int: ...
    def isRoaming(self) -> bool: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...
    def describeContents(self) -> int: ...
    def getReason(self) -> str: ...

    class State:
        CONNECTED: ClassVar["State"]
        CONNECTING: ClassVar["State"]
        DISCONNECTED: ClassVar["State"]
        DISCONNECTING: ClassVar["State"]
        SUSPENDED: ClassVar["State"]
        UNKNOWN: ClassVar["State"]
        CONNECTED: ClassVar[Any]
        CONNECTING: ClassVar[Any]
        DISCONNECTED: ClassVar[Any]
        DISCONNECTING: ClassVar[Any]
        SUSPENDED: ClassVar[Any]
        UNKNOWN: ClassVar[Any]
        @staticmethod
        def values() -> Any: ...
        @staticmethod
        def valueOf(p0: str) -> Any: ...

    class DetailedState:
        AUTHENTICATING: ClassVar["DetailedState"]
        BLOCKED: ClassVar["DetailedState"]
        CAPTIVE_PORTAL_CHECK: ClassVar["DetailedState"]
        CONNECTED: ClassVar["DetailedState"]
        CONNECTING: ClassVar["DetailedState"]
        DISCONNECTED: ClassVar["DetailedState"]
        DISCONNECTING: ClassVar["DetailedState"]
        FAILED: ClassVar["DetailedState"]
        IDLE: ClassVar["DetailedState"]
        OBTAINING_IPADDR: ClassVar["DetailedState"]
        SCANNING: ClassVar["DetailedState"]
        SUSPENDED: ClassVar["DetailedState"]
        VERIFYING_POOR_LINK: ClassVar["DetailedState"]
        AUTHENTICATING: ClassVar[Any]
        BLOCKED: ClassVar[Any]
        CAPTIVE_PORTAL_CHECK: ClassVar[Any]
        CONNECTED: ClassVar[Any]
        CONNECTING: ClassVar[Any]
        DISCONNECTED: ClassVar[Any]
        DISCONNECTING: ClassVar[Any]
        FAILED: ClassVar[Any]
        IDLE: ClassVar[Any]
        OBTAINING_IPADDR: ClassVar[Any]
        SCANNING: ClassVar[Any]
        SUSPENDED: ClassVar[Any]
        VERIFYING_POOR_LINK: ClassVar[Any]
        @staticmethod
        def values() -> Any: ...
        @staticmethod
        def valueOf(p0: str) -> Any: ...
