from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel

class FeatureGroupInfo:
    CREATOR: ClassVar[Any]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    features: Any
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, p0: "FeatureGroupInfo") -> None: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...
    def describeContents(self) -> int: ...
