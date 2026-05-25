from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel

class PathPermission:
    CREATOR: ClassVar[Any]
    CREATOR: ClassVar[Any]
    PATTERN_ADVANCED_GLOB: ClassVar[int]
    PATTERN_LITERAL: ClassVar[int]
    PATTERN_PREFIX: ClassVar[int]
    PATTERN_SIMPLE_GLOB: ClassVar[int]
    PATTERN_SUFFIX: ClassVar[int]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    @overload
    def __init__(self, p0: str, p1: int, p2: str, p3: str) -> None: ...
    @overload
    def __init__(self, p0: Parcel) -> None: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...
    def getReadPermission(self) -> str: ...
    def getWritePermission(self) -> str: ...
