from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel

class Checksum:
    CREATOR: ClassVar[Any]
    TYPE_PARTIAL_MERKLE_ROOT_1M_SHA256: ClassVar[int]
    TYPE_PARTIAL_MERKLE_ROOT_1M_SHA512: ClassVar[int]
    TYPE_WHOLE_MD5: ClassVar[int]
    TYPE_WHOLE_MERKLE_ROOT_4K_SHA256: ClassVar[int]
    TYPE_WHOLE_SHA1: ClassVar[int]
    TYPE_WHOLE_SHA256: ClassVar[int]
    TYPE_WHOLE_SHA512: ClassVar[int]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    def __init__(self, p0: int, p1: Any) -> None: ...
    def getValue(self) -> Any: ...
    def getType(self) -> int: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...
