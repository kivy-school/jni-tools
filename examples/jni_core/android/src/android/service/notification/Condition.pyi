from typing import Any, ClassVar, overload
from android.content.Context import Context
from android.net.Uri import Uri
from android.os.Parcel import Parcel

class Condition:
    CREATOR: ClassVar[Any]
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
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    flags: int
    icon: int
    id: Uri
    line1: str
    line2: str
    source: int
    state: int
    summary: str
    @overload
    def __init__(self, p0: Uri, p1: str, p2: int) -> None: ...
    @overload
    def __init__(self, p0: Uri, p1: str, p2: str, p3: str, p4: int, p5: int, p6: int) -> None: ...
    @overload
    def __init__(self, p0: Uri, p1: str, p2: int, p3: int) -> None: ...
    @overload
    def __init__(self, p0: Parcel) -> None: ...
    @overload
    def __init__(self, p0: Uri, p1: str, p2: str, p3: str, p4: int, p5: int, p6: int, p7: int) -> None: ...
    @staticmethod
    def newId(p0: Context) -> Any: ...
    @staticmethod
    def stateToString(p0: int) -> str: ...
    @staticmethod
    def relevanceToString(p0: int) -> str: ...
    @staticmethod
    def isValidId(p0: Uri, p1: str) -> bool: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...
    def equals(self, p0: Any) -> bool: ...
    def toString(self) -> str: ...
    def hashCode(self) -> int: ...
    def copy(self) -> "Condition": ...
