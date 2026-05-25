from typing import Any, ClassVar, overload
from android.os.Bundle import Bundle
from android.os.Parcel import Parcel

class InstrumentationInfo:
    CREATOR: ClassVar[Any]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    dataDir: str
    functionalTest: bool
    handleProfiling: bool
    publicSourceDir: str
    sourceDir: str
    splitNames: Any
    splitPublicSourceDirs: Any
    splitSourceDirs: Any
    targetPackage: str
    targetProcesses: str
    banner: int
    icon: int
    isArchived: bool
    labelRes: int
    logo: int
    metaData: Bundle
    name: str
    nonLocalizedLabel: str
    packageName: str
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, p0: "InstrumentationInfo") -> None: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...
    def toString(self) -> str: ...
