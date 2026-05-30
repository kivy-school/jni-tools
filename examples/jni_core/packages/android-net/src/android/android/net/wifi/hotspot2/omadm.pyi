from typing import Any, ClassVar, overload
from android.net.wifi.hotspot2.PasspointConfiguration import PasspointConfiguration

class PpsMoParser:
    @staticmethod
    def parseMoText(p0: str) -> PasspointConfiguration: ...

