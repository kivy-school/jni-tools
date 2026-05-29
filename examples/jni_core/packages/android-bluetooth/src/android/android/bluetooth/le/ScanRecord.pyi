from typing import Any, ClassVar, overload
from android.os.ParcelUuid import ParcelUuid
from android.util.SparseArray import SparseArray

class ScanRecord:
    DATA_TYPE_3D_INFORMATION_DATA: ClassVar[int]
    DATA_TYPE_ADVERTISING_INTERVAL: ClassVar[int]
    DATA_TYPE_ADVERTISING_INTERVAL_LONG: ClassVar[int]
    DATA_TYPE_APPEARANCE: ClassVar[int]
    DATA_TYPE_BIG_INFO: ClassVar[int]
    DATA_TYPE_BROADCAST_CODE: ClassVar[int]
    DATA_TYPE_CHANNEL_MAP_UPDATE_INDICATION: ClassVar[int]
    DATA_TYPE_CLASS_OF_DEVICE: ClassVar[int]
    DATA_TYPE_DEVICE_ID: ClassVar[int]
    DATA_TYPE_FLAGS: ClassVar[int]
    DATA_TYPE_INDOOR_POSITIONING: ClassVar[int]
    DATA_TYPE_LE_BLUETOOTH_DEVICE_ADDRESS: ClassVar[int]
    DATA_TYPE_LE_ROLE: ClassVar[int]
    DATA_TYPE_LE_SECURE_CONNECTIONS_CONFIRMATION_VALUE: ClassVar[int]
    DATA_TYPE_LE_SECURE_CONNECTIONS_RANDOM_VALUE: ClassVar[int]
    DATA_TYPE_LE_SUPPORTED_FEATURES: ClassVar[int]
    DATA_TYPE_LOCAL_NAME_COMPLETE: ClassVar[int]
    DATA_TYPE_LOCAL_NAME_SHORT: ClassVar[int]
    DATA_TYPE_MANUFACTURER_SPECIFIC_DATA: ClassVar[int]
    DATA_TYPE_MESH_BEACON: ClassVar[int]
    DATA_TYPE_MESH_MESSAGE: ClassVar[int]
    DATA_TYPE_NONE: ClassVar[int]
    DATA_TYPE_PB_ADV: ClassVar[int]
    DATA_TYPE_PUBLIC_TARGET_ADDRESS: ClassVar[int]
    DATA_TYPE_RANDOM_TARGET_ADDRESS: ClassVar[int]
    DATA_TYPE_RESOLVABLE_SET_IDENTIFIER: ClassVar[int]
    DATA_TYPE_SECURITY_MANAGER_OUT_OF_BAND_FLAGS: ClassVar[int]
    DATA_TYPE_SERVICE_DATA_128_BIT: ClassVar[int]
    DATA_TYPE_SERVICE_DATA_16_BIT: ClassVar[int]
    DATA_TYPE_SERVICE_DATA_32_BIT: ClassVar[int]
    DATA_TYPE_SERVICE_SOLICITATION_UUIDS_128_BIT: ClassVar[int]
    DATA_TYPE_SERVICE_SOLICITATION_UUIDS_16_BIT: ClassVar[int]
    DATA_TYPE_SERVICE_SOLICITATION_UUIDS_32_BIT: ClassVar[int]
    DATA_TYPE_SERVICE_UUIDS_128_BIT_COMPLETE: ClassVar[int]
    DATA_TYPE_SERVICE_UUIDS_128_BIT_PARTIAL: ClassVar[int]
    DATA_TYPE_SERVICE_UUIDS_16_BIT_COMPLETE: ClassVar[int]
    DATA_TYPE_SERVICE_UUIDS_16_BIT_PARTIAL: ClassVar[int]
    DATA_TYPE_SERVICE_UUIDS_32_BIT_COMPLETE: ClassVar[int]
    DATA_TYPE_SERVICE_UUIDS_32_BIT_PARTIAL: ClassVar[int]
    DATA_TYPE_SIMPLE_PAIRING_HASH_C: ClassVar[int]
    DATA_TYPE_SIMPLE_PAIRING_HASH_C_256: ClassVar[int]
    DATA_TYPE_SIMPLE_PAIRING_RANDOMIZER_R: ClassVar[int]
    DATA_TYPE_SIMPLE_PAIRING_RANDOMIZER_R_256: ClassVar[int]
    DATA_TYPE_SLAVE_CONNECTION_INTERVAL_RANGE: ClassVar[int]
    DATA_TYPE_TRANSPORT_DISCOVERY_DATA: ClassVar[int]
    DATA_TYPE_TX_POWER_LEVEL: ClassVar[int]
    DATA_TYPE_URI: ClassVar[int]
    def getServiceUuids(self) -> list: ...
    def getServiceSolicitationUuids(self) -> list: ...
    @overload
    def getManufacturerSpecificData(self) -> SparseArray: ...
    @overload
    def getManufacturerSpecificData(self, p0: int) -> Any: ...
    def getTxPowerLevel(self) -> int: ...
    def getAdvertiseFlags(self) -> int: ...
    def getAdvertisingDataMap(self) -> dict: ...
    def getDeviceName(self) -> str: ...
    @overload
    def getServiceData(self, p0: ParcelUuid) -> Any: ...
    @overload
    def getServiceData(self) -> dict: ...
    def toString(self) -> str: ...
    def getBytes(self) -> Any: ...
