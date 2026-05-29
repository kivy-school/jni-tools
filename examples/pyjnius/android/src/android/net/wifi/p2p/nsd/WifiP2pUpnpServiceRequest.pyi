from typing import Any, ClassVar, overload

class WifiP2pUpnpServiceRequest:
    @overload
    @staticmethod
    def newInstance() -> "WifiP2pUpnpServiceRequest": ...
    @overload
    @staticmethod
    def newInstance(arg0: str) -> "WifiP2pUpnpServiceRequest": ...
