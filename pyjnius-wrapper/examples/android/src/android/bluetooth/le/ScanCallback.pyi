from typing import Any, ClassVar, overload
from android.bluetooth.le.ScanResult import ScanResult

class ScanCallback:
    SCAN_FAILED_ALREADY_STARTED: ClassVar[int]
    SCAN_FAILED_APPLICATION_REGISTRATION_FAILED: ClassVar[int]
    SCAN_FAILED_FEATURE_UNSUPPORTED: ClassVar[int]
    SCAN_FAILED_INTERNAL_ERROR: ClassVar[int]
    SCAN_FAILED_OUT_OF_HARDWARE_RESOURCES: ClassVar[int]
    SCAN_FAILED_SCANNING_TOO_FREQUENTLY: ClassVar[int]
    def __init__(self) -> None: ...
    def onScanResult(self, arg0: int, arg1: ScanResult) -> None: ...
    def onBatchScanResults(self, arg0: list) -> None: ...
    def onScanFailed(self, arg0: int) -> None: ...
