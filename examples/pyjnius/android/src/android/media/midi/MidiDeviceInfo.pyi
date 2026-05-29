from typing import Any, ClassVar, overload
from android.os.Bundle import Bundle
from android.os.Parcel import Parcel

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

class MidiDeviceInfo:
    CREATOR: ClassVar[Creator]
    PROPERTY_BLUETOOTH_DEVICE: ClassVar[str]
    PROPERTY_MANUFACTURER: ClassVar[str]
    PROPERTY_NAME: ClassVar[str]
    PROPERTY_PRODUCT: ClassVar[str]
    PROPERTY_SERIAL_NUMBER: ClassVar[str]
    PROPERTY_USB_DEVICE: ClassVar[str]
    PROPERTY_VERSION: ClassVar[str]
    PROTOCOL_UMP_MIDI_1_0_UP_TO_128_BITS: ClassVar[int]
    PROTOCOL_UMP_MIDI_1_0_UP_TO_128_BITS_AND_JRTS: ClassVar[int]
    PROTOCOL_UMP_MIDI_1_0_UP_TO_64_BITS: ClassVar[int]
    PROTOCOL_UMP_MIDI_1_0_UP_TO_64_BITS_AND_JRTS: ClassVar[int]
    PROTOCOL_UMP_MIDI_2_0: ClassVar[int]
    PROTOCOL_UMP_MIDI_2_0_AND_JRTS: ClassVar[int]
    PROTOCOL_UMP_USE_MIDI_CI: ClassVar[int]
    PROTOCOL_UNKNOWN: ClassVar[int]
    TYPE_BLUETOOTH: ClassVar[int]
    TYPE_USB: ClassVar[int]
    TYPE_VIRTUAL: ClassVar[int]
    def getType(self) -> int: ...
    def getId(self) -> int: ...
    def getInputPortCount(self) -> int: ...
    def getOutputPortCount(self) -> int: ...
    def getPorts(self) -> list["PortInfo"]: ...
    def getProperties(self) -> Bundle: ...
    def isPrivate(self) -> bool: ...
    def getDefaultProtocol(self) -> int: ...
    def equals(self, arg0: Any) -> bool: ...
    def hashCode(self) -> int: ...
    def toString(self) -> str: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, arg0: Parcel, arg1: int) -> None: ...

    class PortInfo:
        TYPE_INPUT: ClassVar[int]
        TYPE_OUTPUT: ClassVar[int]
        def getType(self) -> int: ...
        def getPortNumber(self) -> int: ...
        def getName(self) -> str: ...
