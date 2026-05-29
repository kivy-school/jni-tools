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

class Checksum:
    CREATOR: ClassVar[Creator]
    TYPE_PARTIAL_MERKLE_ROOT_1M_SHA256: ClassVar[int]
    TYPE_PARTIAL_MERKLE_ROOT_1M_SHA512: ClassVar[int]
    TYPE_WHOLE_MD5: ClassVar[int]
    TYPE_WHOLE_MERKLE_ROOT_4K_SHA256: ClassVar[int]
    TYPE_WHOLE_SHA1: ClassVar[int]
    TYPE_WHOLE_SHA256: ClassVar[int]
    TYPE_WHOLE_SHA512: ClassVar[int]
    def __init__(self, arg0: int, arg1: list[int]) -> None: ...
    def getType(self) -> int: ...
    def getValue(self) -> list[int]: ...
    def writeToParcel(self, arg0: Parcel, arg1: int) -> None: ...
    def describeContents(self) -> int: ...
