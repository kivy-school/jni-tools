from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel
from android.os.Parcelable.Creator import Creator

class VersionInfoParcel:
    CREATOR: ClassVar[Creator]
    afmaVersion: str
    buddyApkVersion: int
    clientJarVersion: int
    isClientJar: bool
    isLiteSdk: bool
    @overload
    def __init__(self, arg0: int, arg1: int, arg2: bool) -> None: ...
    @overload
    def __init__(self, arg0: int, arg1: int, arg2: bool, arg3: bool) -> None: ...
    @overload
    def __init__(self, arg0: int, arg1: int, arg2: bool, arg3: bool, arg4: bool) -> None: ...
    @staticmethod
    def forPackage() -> "VersionInfoParcel": ...
    def writeToParcel(self, arg0: Parcel, arg1: int) -> None: ...
