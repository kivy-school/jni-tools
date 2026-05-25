from typing import Any, ClassVar, overload
from java.net.InetAddress import InetAddress

class InetAddresses:
    @staticmethod
    def isNumericAddress(arg0: str) -> bool: ...
    @staticmethod
    def parseNumericAddress(arg0: str) -> InetAddress: ...
