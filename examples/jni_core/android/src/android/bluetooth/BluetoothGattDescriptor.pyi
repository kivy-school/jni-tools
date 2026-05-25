from typing import Any, ClassVar, overload
from android.bluetooth.BluetoothGattCharacteristic import BluetoothGattCharacteristic
from android.os.Parcel import Parcel
from java.util.UUID import UUID

class BluetoothGattDescriptor:
    CREATOR: ClassVar[Any]
    DISABLE_NOTIFICATION_VALUE: ClassVar[Any]
    ENABLE_INDICATION_VALUE: ClassVar[Any]
    ENABLE_NOTIFICATION_VALUE: ClassVar[Any]
    PERMISSION_READ: ClassVar[int]
    PERMISSION_READ_ENCRYPTED: ClassVar[int]
    PERMISSION_READ_ENCRYPTED_MITM: ClassVar[int]
    PERMISSION_WRITE: ClassVar[int]
    PERMISSION_WRITE_ENCRYPTED: ClassVar[int]
    PERMISSION_WRITE_ENCRYPTED_MITM: ClassVar[int]
    PERMISSION_WRITE_SIGNED: ClassVar[int]
    PERMISSION_WRITE_SIGNED_MITM: ClassVar[int]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    def __init__(self, p0: UUID, p1: int) -> None: ...
    def getCharacteristic(self) -> BluetoothGattCharacteristic: ...
    def getUuid(self) -> UUID: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...
    def getValue(self) -> Any: ...
    def getPermissions(self) -> int: ...
    def setValue(self, p0: Any) -> bool: ...
