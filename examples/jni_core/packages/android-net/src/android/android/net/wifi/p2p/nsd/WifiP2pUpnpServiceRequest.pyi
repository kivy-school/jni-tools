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
