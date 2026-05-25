from typing import Any, ClassVar, overload
from android.health.connect.datatypes.DataOrigin import DataOrigin
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

class ChangeLogTokenRequest:
    CREATOR: ClassVar[Creator]
    def getDataOriginFilters(self) -> set: ...
    def getRecordTypes(self) -> set: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, arg0: Parcel, arg1: int) -> None: ...

    class Builder:
        def __init__(self) -> None: ...
        def addRecordType(self, arg0: type) -> "Builder": ...
        def addDataOriginFilter(self, arg0: DataOrigin) -> "Builder": ...
        def build(self) -> "ChangeLogTokenRequest": ...
