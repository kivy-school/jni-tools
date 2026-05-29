from typing import Any, ClassVar, overload

class BluetoothStatusCodes:
    ERROR_BLUETOOTH_NOT_ALLOWED: ClassVar[int]
    ERROR_BLUETOOTH_NOT_ENABLED: ClassVar[int]
    ERROR_DEVICE_NOT_BONDED: ClassVar[int]
    ERROR_GATT_WRITE_NOT_ALLOWED: ClassVar[int]
    ERROR_GATT_WRITE_REQUEST_BUSY: ClassVar[int]
    ERROR_MISSING_BLUETOOTH_CONNECT_PERMISSION: ClassVar[int]
    ERROR_PROFILE_SERVICE_NOT_BOUND: ClassVar[int]
    ERROR_UNKNOWN: ClassVar[int]
    FEATURE_NOT_CONFIGURED: ClassVar[int]
    FEATURE_NOT_SUPPORTED: ClassVar[int]
    FEATURE_SUPPORTED: ClassVar[int]
    SUCCESS: ClassVar[int]
