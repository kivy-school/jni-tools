from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel
from android.os.Parcelable import Parcelable

class AbsSavedState:
    CREATOR: ClassVar[Any]
    EMPTY_STATE: ClassVar["AbsSavedState"]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...
    def getSuperState(self) -> Parcelable: ...
