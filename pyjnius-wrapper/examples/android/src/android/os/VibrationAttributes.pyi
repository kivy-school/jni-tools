from typing import Any, ClassVar, overload
from android.media.AudioAttributes import AudioAttributes
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

class VibrationAttributes:
    CREATOR: ClassVar[Creator]
    FLAG_BYPASS_INTERRUPTION_POLICY: ClassVar[int]
    USAGE_ACCESSIBILITY: ClassVar[int]
    USAGE_ALARM: ClassVar[int]
    USAGE_CLASS_ALARM: ClassVar[int]
    USAGE_CLASS_FEEDBACK: ClassVar[int]
    USAGE_CLASS_MASK: ClassVar[int]
    USAGE_CLASS_MEDIA: ClassVar[int]
    USAGE_CLASS_UNKNOWN: ClassVar[int]
    USAGE_COMMUNICATION_REQUEST: ClassVar[int]
    USAGE_HARDWARE_FEEDBACK: ClassVar[int]
    USAGE_MEDIA: ClassVar[int]
    USAGE_NOTIFICATION: ClassVar[int]
    USAGE_PHYSICAL_EMULATION: ClassVar[int]
    USAGE_RINGTONE: ClassVar[int]
    USAGE_TOUCH: ClassVar[int]
    USAGE_UNKNOWN: ClassVar[int]
    @staticmethod
    def createForUsage(arg0: int) -> "VibrationAttributes": ...
    def getUsageClass(self) -> int: ...
    def getUsage(self) -> int: ...
    def getFlags(self) -> int: ...
    def isFlagSet(self, arg0: int) -> bool: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, arg0: Parcel, arg1: int) -> None: ...
    def equals(self, arg0: Any) -> bool: ...
    def hashCode(self) -> int: ...
    def toString(self) -> str: ...

    class Builder:
        @overload
        def __init__(self) -> None: ...
        @overload
        def __init__(self, arg0: "VibrationAttributes") -> None: ...
        @overload
        def __init__(self, arg0: AudioAttributes) -> None: ...
        def build(self) -> "VibrationAttributes": ...
        def setUsage(self, arg0: int) -> "Builder": ...
        def setFlags(self, arg0: int, arg1: int) -> "Builder": ...
