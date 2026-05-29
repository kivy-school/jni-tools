from typing import Any, ClassVar, overload
from android.net.wifi.hotspot2.PasspointConfiguration import PasspointConfiguration

class ConfigParser:
    @staticmethod
    def parsePasspointConfig(arg0: str, arg1: list[int]) -> PasspointConfiguration: ...
