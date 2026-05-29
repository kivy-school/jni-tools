from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel

class UwbComplexChannel:
    CREATOR: ClassVar[Any]
    UWB_CHANNEL_10: ClassVar[int]
    UWB_CHANNEL_12: ClassVar[int]
    UWB_CHANNEL_13: ClassVar[int]
    UWB_CHANNEL_14: ClassVar[int]
    UWB_CHANNEL_5: ClassVar[int]
    UWB_CHANNEL_6: ClassVar[int]
    UWB_CHANNEL_8: ClassVar[int]
    UWB_CHANNEL_9: ClassVar[int]
    UWB_PREAMBLE_CODE_INDEX_10: ClassVar[int]
    UWB_PREAMBLE_CODE_INDEX_11: ClassVar[int]
    UWB_PREAMBLE_CODE_INDEX_12: ClassVar[int]
    UWB_PREAMBLE_CODE_INDEX_25: ClassVar[int]
    UWB_PREAMBLE_CODE_INDEX_26: ClassVar[int]
    UWB_PREAMBLE_CODE_INDEX_27: ClassVar[int]
    UWB_PREAMBLE_CODE_INDEX_28: ClassVar[int]
    UWB_PREAMBLE_CODE_INDEX_29: ClassVar[int]
    UWB_PREAMBLE_CODE_INDEX_30: ClassVar[int]
    UWB_PREAMBLE_CODE_INDEX_31: ClassVar[int]
    UWB_PREAMBLE_CODE_INDEX_32: ClassVar[int]
    UWB_PREAMBLE_CODE_INDEX_9: ClassVar[int]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    def equals(self, p0: Any) -> bool: ...
    def toString(self) -> str: ...
    def hashCode(self) -> int: ...
    def getPreambleIndex(self) -> int: ...
    def getChannel(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...
    def describeContents(self) -> int: ...

    class Builder:
        def __init__(self) -> None: ...
        def setChannel(self, p0: int) -> Any: ...
        def setPreambleIndex(self, p0: int) -> Any: ...
        def build(self) -> "UwbComplexChannel": ...
