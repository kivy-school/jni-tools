from typing import Any, ClassVar, overload
from java.net.InetAddress import InetAddress

class InetAddresses:
    @staticmethod
    def isNumericAddress(p0: str) -> bool: ...
    @staticmethod
    def parseNumericAddress(p0: str) -> InetAddress: ...
