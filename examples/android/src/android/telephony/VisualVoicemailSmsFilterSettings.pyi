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

class VisualVoicemailSmsFilterSettings:
    CREATOR: ClassVar[Creator]
    DESTINATION_PORT_ANY: ClassVar[int]
    DESTINATION_PORT_DATA_SMS: ClassVar[int]
    clientPrefix: str
    destinationPort: int
    originatingNumbers: list
    def describeContents(self) -> int: ...
    def writeToParcel(self, arg0: Parcel, arg1: int) -> None: ...
    def toString(self) -> str: ...

    class Builder:
        def __init__(self) -> None: ...
        def build(self) -> "VisualVoicemailSmsFilterSettings": ...
        def setClientPrefix(self, arg0: str) -> "Builder": ...
        def setOriginatingNumbers(self, arg0: list) -> "Builder": ...
        def setDestinationPort(self, arg0: int) -> "Builder": ...
