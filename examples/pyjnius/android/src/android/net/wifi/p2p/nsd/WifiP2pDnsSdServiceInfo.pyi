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
