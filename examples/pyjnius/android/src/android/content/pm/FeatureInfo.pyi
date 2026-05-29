from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel

class FeatureInfo:
    CREATOR: ClassVar[Any]
    FLAG_REQUIRED: ClassVar[int]
    GL_ES_VERSION_UNDEFINED: ClassVar[int]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    flags: int
    name: str
    reqGlEsVersion: int
    version: int
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, p0: "FeatureInfo") -> None: ...
    def toString(self) -> str: ...
    def getGlEsVersion(self) -> str: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...
    def describeContents(self) -> int: ...
