from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Alignment:
    """Forward declaration for ``android.text.Layout.Alignment``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.text.Layout.Alignment')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/text/Layout/Alignment
    """
    ...

class AlignmentSpan:
    def getAlignment(self) -> Alignment: ...

    class Standard:
        @overload
        def __init__(self, arg0: Alignment) -> None: ...
        @overload
        def __init__(self, arg0: Parcel) -> None: ...
        def getSpanTypeId(self) -> int: ...
        def describeContents(self) -> int: ...
        def writeToParcel(self, arg0: Parcel, arg1: int) -> None: ...
        def getAlignment(self) -> Alignment: ...
        def toString(self) -> str: ...
