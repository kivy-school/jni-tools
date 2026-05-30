from typing import Any, ClassVar, overload

class WifiP2pUpnpServiceRequest:
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    @overload
    @staticmethod
    def newInstance() -> "WifiP2pUpnpServiceRequest": ...
    @overload
    @staticmethod
    def newInstance(p0: str) -> "WifiP2pUpnpServiceRequest": ...

from typing import Any, ClassVar, overload
from android.net.wifi.p2p.nsd.WifiP2pUsdBasedServiceConfig import WifiP2pUsdBasedServiceConfig
from android.os.Parcel import Parcel

class WifiP2pServiceRequest:
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    def __init__(self, p0: WifiP2pUsdBasedServiceConfig) -> None: ...
    def equals(self, p0: Any) -> bool: ...
    def hashCode(self) -> int: ...
    @overload
    @staticmethod
    def newInstance(p0: int) -> "WifiP2pServiceRequest": ...
    @overload
    @staticmethod
    def newInstance(p0: int, p1: str) -> "WifiP2pServiceRequest": ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...
    def getWifiP2pUsdBasedServiceConfig(self) -> WifiP2pUsdBasedServiceConfig: ...

from typing import Any, ClassVar, overload

class WifiP2pDnsSdServiceRequest:
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    @overload
    @staticmethod
    def newInstance(p0: str, p1: str) -> "WifiP2pDnsSdServiceRequest": ...
    @overload
    @staticmethod
    def newInstance(p0: str) -> "WifiP2pDnsSdServiceRequest": ...
    @overload
    @staticmethod
    def newInstance() -> "WifiP2pDnsSdServiceRequest": ...

from typing import Any, ClassVar, overload

class WifiP2pUpnpServiceInfo:
    SERVICE_TYPE_ALL: ClassVar[int]
    SERVICE_TYPE_BONJOUR: ClassVar[int]
    SERVICE_TYPE_UPNP: ClassVar[int]
    SERVICE_TYPE_VENDOR_SPECIFIC: ClassVar[int]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    @staticmethod
    def newInstance(p0: str, p1: str, p2: list) -> "WifiP2pUpnpServiceInfo": ...

from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel

class WifiP2pUsdBasedServiceConfig:
    CREATOR: ClassVar[Any]
    SERVICE_PROTOCOL_TYPE_BONJOUR: ClassVar[int]
    SERVICE_PROTOCOL_TYPE_GENERIC: ClassVar[int]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    def __init__(self) -> None: ...
    def getServiceProtocolType(self) -> int: ...
    def getServiceSpecificInfo(self) -> Any: ...
    @staticmethod
    def getMaxAllowedServiceSpecificInfoLength() -> int: ...
    def toString(self) -> str: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...
    def getServiceName(self) -> str: ...

    class Builder:
        def __init__(self, p0: str) -> None: ...
        def setServiceSpecificInfo(self, p0: Any) -> Any: ...
        def setServiceProtocolType(self, p0: int) -> Any: ...
        def build(self) -> "WifiP2pUsdBasedServiceConfig": ...

from typing import Any, ClassVar, overload
from android.net.wifi.p2p.nsd.WifiP2pUsdBasedServiceConfig import WifiP2pUsdBasedServiceConfig
from android.os.Parcel import Parcel

class WifiP2pServiceInfo:
    SERVICE_TYPE_ALL: ClassVar[int]
    SERVICE_TYPE_BONJOUR: ClassVar[int]
    SERVICE_TYPE_UPNP: ClassVar[int]
    SERVICE_TYPE_VENDOR_SPECIFIC: ClassVar[int]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    def __init__(self, p0: WifiP2pUsdBasedServiceConfig) -> None: ...
    def equals(self, p0: Any) -> bool: ...
    def hashCode(self) -> int: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...
    def getWifiP2pUsdBasedServiceConfig(self) -> WifiP2pUsdBasedServiceConfig: ...

from typing import Any, ClassVar, overload

class WifiP2pDnsSdServiceInfo:
    SERVICE_TYPE_ALL: ClassVar[int]
    SERVICE_TYPE_BONJOUR: ClassVar[int]
    SERVICE_TYPE_UPNP: ClassVar[int]
    SERVICE_TYPE_VENDOR_SPECIFIC: ClassVar[int]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    @staticmethod
    def newInstance(p0: str, p1: str, p2: dict) -> "WifiP2pDnsSdServiceInfo": ...

from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel

class WifiP2pUsdBasedServiceResponse:
    CREATOR: ClassVar[Any]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    def getServiceProtocolType(self) -> int: ...
    def getServiceSpecificInfo(self) -> Any: ...
    def toString(self) -> str: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...

