from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel

class ConfigurationInfo:
    CREATOR: ClassVar[Any]
    GL_ES_VERSION_UNDEFINED: ClassVar[int]
    INPUT_FEATURE_FIVE_WAY_NAV: ClassVar[int]
    INPUT_FEATURE_HARD_KEYBOARD: ClassVar[int]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    reqGlEsVersion: int
    reqInputFeatures: int
    reqKeyboardType: int
    reqNavigation: int
    reqTouchScreen: int
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, p0: "ConfigurationInfo") -> None: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...
    def getGlEsVersion(self) -> str: ...
    def toString(self) -> str: ...
