from typing import Any, ClassVar, overload
from android.content.Context import Context
from android.os.Parcel import Parcel
from android.util.Size import Size
from android.view.inputmethod.InlineSuggestionInfo import InlineSuggestionInfo
from java.util.concurrent.Executor import Executor
from java.util.function.Consumer import Consumer

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

class InlineSuggestion:
    CREATOR: ClassVar[Creator]
    def inflate(self, arg0: Context, arg1: Size, arg2: Executor, arg3: Consumer) -> None: ...
    def getInfo(self) -> InlineSuggestionInfo: ...
    def toString(self) -> str: ...
    def equals(self, arg0: Any) -> bool: ...
    def hashCode(self) -> int: ...
    def writeToParcel(self, arg0: Parcel, arg1: int) -> None: ...
    def describeContents(self) -> int: ...
