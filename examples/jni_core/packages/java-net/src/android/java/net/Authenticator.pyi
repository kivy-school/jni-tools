from typing import Any, ClassVar, overload
from java.net.InetAddress import InetAddress
from java.net.PasswordAuthentication import PasswordAuthentication
from java.net.URL import URL

class Authenticator:
    def __init__(self) -> None: ...
    @staticmethod
    def getDefault() -> "Authenticator": ...
    @overload
    @staticmethod
    def requestPasswordAuthentication(p0: "Authenticator", p1: str, p2: InetAddress, p3: int, p4: str, p5: str, p6: str, p7: URL, p8: Any) -> PasswordAuthentication: ...
    @overload
    @staticmethod
    def requestPasswordAuthentication(p0: str, p1: InetAddress, p2: int, p3: str, p4: str, p5: str, p6: URL, p7: Any) -> PasswordAuthentication: ...
    @overload
    @staticmethod
    def requestPasswordAuthentication(p0: str, p1: InetAddress, p2: int, p3: str, p4: str, p5: str) -> PasswordAuthentication: ...
    @overload
    @staticmethod
    def requestPasswordAuthentication(p0: InetAddress, p1: int, p2: str, p3: str, p4: str) -> PasswordAuthentication: ...
    def requestPasswordAuthenticationInstance(self, p0: str, p1: InetAddress, p2: int, p3: str, p4: str, p5: str, p6: URL, p7: Any) -> PasswordAuthentication: ...
    @staticmethod
    def setDefault(p0: "Authenticator") -> None: ...

    class RequestorType:
        PROXY: ClassVar["RequestorType"]
        SERVER: ClassVar["RequestorType"]
        PROXY: ClassVar[Any]
        SERVER: ClassVar[Any]
        @staticmethod
        def values() -> Any: ...
        @staticmethod
        def valueOf(p0: str) -> Any: ...
