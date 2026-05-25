from typing import Any, ClassVar, overload
from android.bluetooth.BluetoothGattCharacteristic import BluetoothGattCharacteristic
from android.os.Parcel import Parcel
from java.util.UUID import UUID

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Creator:
    """Forward declaration for ``android.os.Parcelable.Creator``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.os.Parcelable.Creator')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/os/Parcelable/Creator
    """
    ...

class BluetoothGattDescriptor:
    CREATOR: ClassVar[Creator]
    DISABLE_NOTIFICATION_VALUE: ClassVar[list[int]]
    ENABLE_INDICATION_VALUE: ClassVar[list[int]]
    ENABLE_NOTIFICATION_VALUE: ClassVar[list[int]]
    PERMISSION_READ: ClassVar[int]
    PERMISSION_READ_ENCRYPTED: ClassVar[int]
    PERMISSION_READ_ENCRYPTED_MITM: ClassVar[int]
    PERMISSION_WRITE: ClassVar[int]
    PERMISSION_WRITE_ENCRYPTED: ClassVar[int]
    PERMISSION_WRITE_ENCRYPTED_MITM: ClassVar[int]
    PERMISSION_WRITE_SIGNED: ClassVar[int]
    PERMISSION_WRITE_SIGNED_MITM: ClassVar[int]
    def __init__(self, arg0: UUID, arg1: int) -> None: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, arg0: Parcel, arg1: int) -> None: ...
    def getCharacteristic(self) -> BluetoothGattCharacteristic: ...
    def getUuid(self) -> UUID: ...
    def getPermissions(self) -> int: ...
    def getValue(self) -> list[int]: ...
    def setValue(self, arg0: list[int]) -> bool: ...
