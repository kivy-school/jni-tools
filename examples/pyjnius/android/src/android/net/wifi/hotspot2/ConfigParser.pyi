from typing import Any, ClassVar, overload
from android.net.wifi.hotspot2.PasspointConfiguration import PasspointConfiguration

class ConfigParser:
    @staticmethod
    def parsePasspointConfig(p0: str, p1: Any) -> PasspointConfiguration: ...
