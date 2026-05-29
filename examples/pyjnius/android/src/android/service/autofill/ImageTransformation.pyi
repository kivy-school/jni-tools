from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel
from android.view.autofill.AutofillId import AutofillId
from java.util.regex.Pattern import Pattern

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

class ImageTransformation:
    CREATOR: ClassVar[Creator]
    def toString(self) -> str: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, arg0: Parcel, arg1: int) -> None: ...

    class Builder:
        @overload
        def __init__(self, arg0: AutofillId, arg1: Pattern, arg2: int) -> None: ...
        @overload
        def __init__(self, arg0: AutofillId, arg1: Pattern, arg2: int, arg3: str) -> None: ...
        @overload
        def addOption(self, arg0: Pattern, arg1: int) -> "Builder": ...
        @overload
        def addOption(self, arg0: Pattern, arg1: int, arg2: str) -> "Builder": ...
        def build(self) -> "ImageTransformation": ...
