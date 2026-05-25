from typing import Any, ClassVar, overload

class WifiP2pDnsSdServiceRequest:
    @overload
    @staticmethod
    def newInstance() -> "WifiP2pDnsSdServiceRequest": ...
    @overload
    @staticmethod
    def newInstance(arg0: str) -> "WifiP2pDnsSdServiceRequest": ...
    @overload
    @staticmethod
    def newInstance(arg0: str, arg1: str) -> "WifiP2pDnsSdServiceRequest": ...
