from typing import Any, ClassVar, overload
from android.bluetooth.BluetoothClass import BluetoothClass
from android.bluetooth.BluetoothGatt import BluetoothGatt
from android.bluetooth.BluetoothGattCallback import BluetoothGattCallback
from android.bluetooth.BluetoothSocket import BluetoothSocket
from android.bluetooth.BluetoothSocketSettings import BluetoothSocketSettings
from android.content.Context import Context
from android.os.Handler import Handler
from android.os.Parcel import Parcel
from java.util.UUID import UUID

class BluetoothDevice:
    ACTION_ACL_CONNECTED: ClassVar[str]
    ACTION_ACL_DISCONNECTED: ClassVar[str]
    ACTION_ACL_DISCONNECT_REQUESTED: ClassVar[str]
    ACTION_ALIAS_CHANGED: ClassVar[str]
    ACTION_BOND_STATE_CHANGED: ClassVar[str]
    ACTION_CLASS_CHANGED: ClassVar[str]
    ACTION_ENCRYPTION_CHANGE: ClassVar[str]
    ACTION_FOUND: ClassVar[str]
    ACTION_KEY_MISSING: ClassVar[str]
    ACTION_NAME_CHANGED: ClassVar[str]
    ACTION_PAIRING_REQUEST: ClassVar[str]
    ACTION_UUID: ClassVar[str]
    ADDRESS_TYPE_ANONYMOUS: ClassVar[int]
    ADDRESS_TYPE_PUBLIC: ClassVar[int]
    ADDRESS_TYPE_RANDOM: ClassVar[int]
    ADDRESS_TYPE_UNKNOWN: ClassVar[int]
    BOND_BONDED: ClassVar[int]
    BOND_BONDING: ClassVar[int]
    BOND_NONE: ClassVar[int]
    CREATOR: ClassVar[Any]
    DEVICE_TYPE_CLASSIC: ClassVar[int]
    DEVICE_TYPE_DUAL: ClassVar[int]
    DEVICE_TYPE_LE: ClassVar[int]
    DEVICE_TYPE_UNKNOWN: ClassVar[int]
    ENCRYPTION_ALGORITHM_AES: ClassVar[int]
    ENCRYPTION_ALGORITHM_E0: ClassVar[int]
    ENCRYPTION_ALGORITHM_NONE: ClassVar[int]
    ERROR: ClassVar[int]
    EXTRA_BOND_STATE: ClassVar[str]
    EXTRA_CLASS: ClassVar[str]
    EXTRA_DEVICE: ClassVar[str]
    EXTRA_ENCRYPTION_ALGORITHM: ClassVar[str]
    EXTRA_ENCRYPTION_ENABLED: ClassVar[str]
    EXTRA_ENCRYPTION_STATUS: ClassVar[str]
    EXTRA_IS_COORDINATED_SET_MEMBER: ClassVar[str]
    EXTRA_KEY_SIZE: ClassVar[str]
    EXTRA_NAME: ClassVar[str]
    EXTRA_PAIRING_KEY: ClassVar[str]
    EXTRA_PAIRING_VARIANT: ClassVar[str]
    EXTRA_PREVIOUS_BOND_STATE: ClassVar[str]
    EXTRA_RSSI: ClassVar[str]
    EXTRA_TRANSPORT: ClassVar[str]
    EXTRA_UUID: ClassVar[str]
    PAIRING_VARIANT_PASSKEY_CONFIRMATION: ClassVar[int]
    PAIRING_VARIANT_PIN: ClassVar[int]
    PHY_LE_1M: ClassVar[int]
    PHY_LE_1M_MASK: ClassVar[int]
    PHY_LE_2M: ClassVar[int]
    PHY_LE_2M_MASK: ClassVar[int]
    PHY_LE_CODED: ClassVar[int]
    PHY_LE_CODED_MASK: ClassVar[int]
    PHY_OPTION_NO_PREFERRED: ClassVar[int]
    PHY_OPTION_S2: ClassVar[int]
    PHY_OPTION_S8: ClassVar[int]
    TRANSPORT_AUTO: ClassVar[int]
    TRANSPORT_BREDR: ClassVar[int]
    TRANSPORT_LE: ClassVar[int]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    @overload
    def connectGatt(self, p0: Context, p1: bool, p2: BluetoothGattCallback, p3: int, p4: int) -> BluetoothGatt: ...
    @overload
    def connectGatt(self, p0: Context, p1: bool, p2: BluetoothGattCallback, p3: int) -> BluetoothGatt: ...
    @overload
    def connectGatt(self, p0: Context, p1: bool, p2: BluetoothGattCallback) -> BluetoothGatt: ...
    @overload
    def connectGatt(self, p0: Context, p1: bool, p2: BluetoothGattCallback, p3: int, p4: int, p5: Handler) -> BluetoothGatt: ...
    def createBond(self) -> bool: ...
    def createInsecureL2capChannel(self, p0: int) -> BluetoothSocket: ...
    def createInsecureRfcommSocketToServiceRecord(self, p0: UUID) -> BluetoothSocket: ...
    def createL2capChannel(self, p0: int) -> BluetoothSocket: ...
    def createRfcommSocketToServiceRecord(self, p0: UUID) -> BluetoothSocket: ...
    def createUsingSocketSettings(self, p0: BluetoothSocketSettings) -> BluetoothSocket: ...
    def fetchUuidsWithSdp(self) -> bool: ...
    def getAlias(self) -> str: ...
    def getBluetoothClass(self) -> BluetoothClass: ...
    def getBondState(self) -> int: ...
    def getIdentityAddressWithType(self) -> Any: ...
    def getUuids(self) -> Any: ...
    def setAlias(self, p0: str) -> int: ...
    def setPairingConfirmation(self, p0: bool) -> bool: ...
    def setPin(self, p0: Any) -> bool: ...
    def getAddressType(self) -> int: ...
    def getName(self) -> str: ...
    def equals(self, p0: Any) -> bool: ...
    def toString(self) -> str: ...
    def hashCode(self) -> int: ...
    def getType(self) -> int: ...
    def getAddress(self) -> str: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...
    def describeContents(self) -> int: ...

    class BluetoothAddress:
        CREATOR: ClassVar[Any]
        CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
        PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
        def __init__(self, p0: str, p1: int) -> None: ...
        def getAddressType(self) -> int: ...
        def getAddress(self) -> str: ...
        def writeToParcel(self, p0: Parcel, p1: int) -> None: ...
        def describeContents(self) -> int: ...
