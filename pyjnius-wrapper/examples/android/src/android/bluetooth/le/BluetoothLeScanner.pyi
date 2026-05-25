from typing import Any, ClassVar, overload
from android.app.PendingIntent import PendingIntent
from android.bluetooth.le.ScanCallback import ScanCallback
from android.bluetooth.le.ScanSettings import ScanSettings

class BluetoothLeScanner:
    EXTRA_CALLBACK_TYPE: ClassVar[str]
    EXTRA_ERROR_CODE: ClassVar[str]
    EXTRA_LIST_SCAN_RESULT: ClassVar[str]
    @overload
    def startScan(self, arg0: ScanCallback) -> None: ...
    @overload
    def startScan(self, arg0: list, arg1: ScanSettings, arg2: ScanCallback) -> None: ...
    @overload
    def startScan(self, arg0: list, arg1: ScanSettings, arg2: PendingIntent) -> int: ...
    @overload
    def stopScan(self, arg0: ScanCallback) -> None: ...
    @overload
    def stopScan(self, arg0: PendingIntent) -> None: ...
    def flushPendingScanResults(self, arg0: ScanCallback) -> None: ...
