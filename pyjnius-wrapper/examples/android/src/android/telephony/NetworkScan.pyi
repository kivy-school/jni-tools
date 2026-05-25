from typing import Any, ClassVar, overload

class NetworkScan:
    ERROR_INTERRUPTED: ClassVar[int]
    ERROR_INVALID_SCAN: ClassVar[int]
    ERROR_INVALID_SCANID: ClassVar[int]
    ERROR_MODEM_ERROR: ClassVar[int]
    ERROR_MODEM_UNAVAILABLE: ClassVar[int]
    ERROR_RADIO_INTERFACE_ERROR: ClassVar[int]
    ERROR_UNSUPPORTED: ClassVar[int]
    SUCCESS: ClassVar[int]
    def stopScan(self) -> None: ...
