from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Creator:
    """Forward declaration for ``android.os.Parcelable.Creator``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.os.Parcelable.Creator')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/os/Parcelable/Creator
    """
    ...

class TableRequest:
    CREATOR: ClassVar[Creator]
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
    def __init__(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> None: ...
    def getTableId(self) -> int: ...
    def getTableName(self) -> int: ...
    def getVersion(self) -> int: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, arg0: Parcel, arg1: int) -> None: ...
