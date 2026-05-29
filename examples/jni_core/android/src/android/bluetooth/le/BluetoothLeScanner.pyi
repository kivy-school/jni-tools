from typing import Any, ClassVar, overload
from android.app.PendingIntent import PendingIntent
from android.bluetooth.le.ScanCallback import ScanCallback
from android.bluetooth.le.ScanSettings import ScanSettings

class BluetoothLeScanner:
    EXTRA_CALLBACK_TYPE: ClassVar[str]
    EXTRA_ERROR_CODE: ClassVar[str]
    EXTRA_LIST_SCAN_RESULT: ClassVar[str]
    def flushPendingScanResults(self, p0: ScanCallback) -> None: ...
    @overload
    def startScan(self, p0: list, p1: ScanSettings, p2: ScanCallback) -> None: ...
    @overload
    def startScan(self, p0: ScanCallback) -> None: ...
    @overload
    def startScan(self, p0: list, p1: ScanSettings, p2: PendingIntent) -> int: ...
    @overload
    def stopScan(self, p0: PendingIntent) -> None: ...
    @overload
    def stopScan(self, p0: ScanCallback) -> None: ...
