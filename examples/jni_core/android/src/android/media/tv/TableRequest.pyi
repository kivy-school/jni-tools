from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel

class TableRequest:
    CREATOR: ClassVar[Any]
    TABLE_NAME_BAT: ClassVar[int]
    TABLE_NAME_CAT: ClassVar[int]
    TABLE_NAME_EIT: ClassVar[int]
    TABLE_NAME_NIT: ClassVar[int]
    TABLE_NAME_PAT: ClassVar[int]
    TABLE_NAME_PMT: ClassVar[int]
    TABLE_NAME_SDT: ClassVar[int]
    TABLE_NAME_SIT: ClassVar[int]
    TABLE_NAME_TDT: ClassVar[int]
    TABLE_NAME_TOT: ClassVar[int]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    CREATOR: ClassVar[Any]
    REQUEST_OPTION_AUTO_UPDATE: ClassVar[int]
    REQUEST_OPTION_ONESHOT: ClassVar[int]
    REQUEST_OPTION_ONEWAY: ClassVar[int]
    REQUEST_OPTION_REPEAT: ClassVar[int]
    def __init__(self, p0: int, p1: int, p2: int, p3: int, p4: int) -> None: ...
    def getVersion(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...
    def describeContents(self) -> int: ...
    def getTableId(self) -> int: ...
    def getTableName(self) -> int: ...
