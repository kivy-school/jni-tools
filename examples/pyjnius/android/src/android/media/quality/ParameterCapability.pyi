from typing import Any, ClassVar, overload
from android.os.Bundle import Bundle
from android.os.Parcel import Parcel

class ParameterCapability:
    CAPABILITY_DEFAULT: ClassVar[str]
    CAPABILITY_ENUM: ClassVar[str]
    CAPABILITY_MAX: ClassVar[str]
    CAPABILITY_MIN: ClassVar[str]
    CREATOR: ClassVar[Any]
    TYPE_DOUBLE: ClassVar[int]
    TYPE_INT: ClassVar[int]
    TYPE_LONG: ClassVar[int]
    TYPE_NONE: ClassVar[int]
    TYPE_STRING: ClassVar[int]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    def getParameterName(self) -> str: ...
    def getParameterType(self) -> int: ...
    def isSupported(self) -> bool: ...
    def getCapabilities(self) -> Bundle: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...
    def describeContents(self) -> int: ...
