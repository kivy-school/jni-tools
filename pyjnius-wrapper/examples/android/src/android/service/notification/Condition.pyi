from typing import Any, ClassVar, overload
from android.content.Context import Context
from android.net.Uri import Uri
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
class Builder:
    """Forward declaration for ``android.net.Uri.Builder``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.net.Uri.Builder')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/net/Uri/Builder
    """
    ...

class Condition:
    CREATOR: ClassVar[Creator]
    FLAG_RELEVANT_ALWAYS: ClassVar[int]
    FLAG_RELEVANT_NOW: ClassVar[int]
    SCHEME: ClassVar[str]
    SOURCE_CONTEXT: ClassVar[int]
    SOURCE_SCHEDULE: ClassVar[int]
    SOURCE_UNKNOWN: ClassVar[int]
    SOURCE_USER_ACTION: ClassVar[int]
    STATE_ERROR: ClassVar[int]
    STATE_FALSE: ClassVar[int]
    STATE_TRUE: ClassVar[int]
    STATE_UNKNOWN: ClassVar[int]
    flags: int
    icon: int
    id: Uri
    line1: str
    line2: str
    source: int
    state: int
    summary: str
    @overload
    def __init__(self, arg0: Uri, arg1: str, arg2: int) -> None: ...
    @overload
    def __init__(self, arg0: Uri, arg1: str, arg2: int, arg3: int) -> None: ...
    @overload
    def __init__(self, arg0: Uri, arg1: str, arg2: str, arg3: str, arg4: int, arg5: int, arg6: int) -> None: ...
    @overload
    def __init__(self, arg0: Uri, arg1: str, arg2: str, arg3: str, arg4: int, arg5: int, arg6: int, arg7: int) -> None: ...
    @overload
    def __init__(self, arg0: Parcel) -> None: ...
    def writeToParcel(self, arg0: Parcel, arg1: int) -> None: ...
    def toString(self) -> str: ...
    @staticmethod
    def stateToString(arg0: int) -> str: ...
    @staticmethod
    def relevanceToString(arg0: int) -> str: ...
    def equals(self, arg0: Any) -> bool: ...
    def hashCode(self) -> int: ...
    def describeContents(self) -> int: ...
    def copy(self) -> "Condition": ...
    @staticmethod
    def newId(arg0: Context) -> Builder: ...
    @staticmethod
    def isValidId(arg0: Uri, arg1: str) -> bool: ...
