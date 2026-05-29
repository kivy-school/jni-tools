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
