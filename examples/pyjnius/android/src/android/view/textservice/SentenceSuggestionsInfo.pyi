from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel
from android.view.textservice.SuggestionsInfo import SuggestionsInfo

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

class SentenceSuggestionsInfo:
    CREATOR: ClassVar[Creator]
    @overload
    def __init__(self, arg0: list[SuggestionsInfo], arg1: list[int], arg2: list[int]) -> None: ...
    @overload
    def __init__(self, arg0: Parcel) -> None: ...
    def writeToParcel(self, arg0: Parcel, arg1: int) -> None: ...
    def describeContents(self) -> int: ...
    def getSuggestionsCount(self) -> int: ...
    def getSuggestionsInfoAt(self, arg0: int) -> SuggestionsInfo: ...
    def getOffsetAt(self, arg0: int) -> int: ...
    def getLengthAt(self, arg0: int) -> int: ...
