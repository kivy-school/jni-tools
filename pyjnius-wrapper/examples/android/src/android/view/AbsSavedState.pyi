from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel
from android.os.Parcelable import Parcelable
from java.lang.ClassLoader import ClassLoader

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

class AbsSavedState:
    CREATOR: ClassVar[Creator]
    EMPTY_STATE: ClassVar["AbsSavedState"]
    @overload
    def __init__(self, arg0: Parcelable) -> None: ...
    @overload
    def __init__(self, arg0: Parcel) -> None: ...
    @overload
    def __init__(self, arg0: Parcel, arg1: ClassLoader) -> None: ...
    def getSuperState(self) -> Parcelable: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, arg0: Parcel, arg1: int) -> None: ...
