from typing import Any, ClassVar, overload
from android.bluetooth.BluetoothGattDescriptor import BluetoothGattDescriptor
from android.bluetooth.BluetoothGattService import BluetoothGattService
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

class BluetoothGattCharacteristic:
    CREATOR: ClassVar[Creator]
    FORMAT_FLOAT: ClassVar[int]
    FORMAT_SFLOAT: ClassVar[int]
    FORMAT_SINT16: ClassVar[int]
    FORMAT_SINT32: ClassVar[int]
    FORMAT_SINT8: ClassVar[int]
    FORMAT_UINT16: ClassVar[int]
    FORMAT_UINT32: ClassVar[int]
    FORMAT_UINT8: ClassVar[int]
    PERMISSION_READ: ClassVar[int]
    PERMISSION_READ_ENCRYPTED: ClassVar[int]
    PERMISSION_READ_ENCRYPTED_MITM: ClassVar[int]
    PERMISSION_WRITE: ClassVar[int]
    PERMISSION_WRITE_ENCRYPTED: ClassVar[int]
    PERMISSION_WRITE_ENCRYPTED_MITM: ClassVar[int]
    PERMISSION_WRITE_SIGNED: ClassVar[int]
    PERMISSION_WRITE_SIGNED_MITM: ClassVar[int]
    PROPERTY_BROADCAST: ClassVar[int]
    PROPERTY_EXTENDED_PROPS: ClassVar[int]
    PROPERTY_INDICATE: ClassVar[int]
    PROPERTY_NOTIFY: ClassVar[int]
    PROPERTY_READ: ClassVar[int]
    PROPERTY_SIGNED_WRITE: ClassVar[int]
    PROPERTY_WRITE: ClassVar[int]
    PROPERTY_WRITE_NO_RESPONSE: ClassVar[int]
    WRITE_TYPE_DEFAULT: ClassVar[int]
    WRITE_TYPE_NO_RESPONSE: ClassVar[int]
    WRITE_TYPE_SIGNED: ClassVar[int]
    mDescriptors: list
    def __init__(self, arg0: UUID, arg1: int, arg2: int) -> None: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, arg0: Parcel, arg1: int) -> None: ...
    def addDescriptor(self, arg0: BluetoothGattDescriptor) -> bool: ...
    def getService(self) -> BluetoothGattService: ...
    def getUuid(self) -> UUID: ...
    def getInstanceId(self) -> int: ...
    def getProperties(self) -> int: ...
    def getPermissions(self) -> int: ...
    def getWriteType(self) -> int: ...
    def setWriteType(self, arg0: int) -> None: ...
    def getDescriptors(self) -> list: ...
    def getDescriptor(self, arg0: UUID) -> BluetoothGattDescriptor: ...
    def getValue(self) -> list[int]: ...
    def getIntValue(self, arg0: int, arg1: int) -> int: ...
    def getFloatValue(self, arg0: int, arg1: int) -> float: ...
    def getStringValue(self, arg0: int) -> str: ...
    @overload
    def setValue(self, arg0: list[int]) -> bool: ...
    @overload
    def setValue(self, arg0: int, arg1: int, arg2: int) -> bool: ...
    @overload
    def setValue(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool: ...
    @overload
    def setValue(self, arg0: str) -> bool: ...
