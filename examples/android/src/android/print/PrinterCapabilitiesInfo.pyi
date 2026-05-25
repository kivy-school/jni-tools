from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel
from android.print.PrintAttributes import PrintAttributes
from android.print.PrinterId import PrinterId

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
class Margins:
    """Forward declaration for ``android.print.PrintAttributes.Margins``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.print.PrintAttributes.Margins')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/print/PrintAttributes/Margins
    """
    ...
class MediaSize:
    """Forward declaration for ``android.print.PrintAttributes.MediaSize``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.print.PrintAttributes.MediaSize')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/print/PrintAttributes/MediaSize
    """
    ...
class Resolution:
    """Forward declaration for ``android.print.PrintAttributes.Resolution``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.print.PrintAttributes.Resolution')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/print/PrintAttributes/Resolution
    """
    ...

class PrinterCapabilitiesInfo:
    CREATOR: ClassVar[Creator]
    def getMediaSizes(self) -> list: ...
    def getResolutions(self) -> list: ...
    def getMinMargins(self) -> Margins: ...
    def getColorModes(self) -> int: ...
    def getDuplexModes(self) -> int: ...
    def getDefaults(self) -> PrintAttributes: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, arg0: Parcel, arg1: int) -> None: ...
    def hashCode(self) -> int: ...
    def equals(self, arg0: Any) -> bool: ...
    def toString(self) -> str: ...

    class Builder:
        def __init__(self, arg0: PrinterId) -> None: ...
        def addMediaSize(self, arg0: MediaSize, arg1: bool) -> "Builder": ...
        def addResolution(self, arg0: Resolution, arg1: bool) -> "Builder": ...
        def setMinMargins(self, arg0: Margins) -> "Builder": ...
        def setColorModes(self, arg0: int, arg1: int) -> "Builder": ...
        def setDuplexModes(self, arg0: int, arg1: int) -> "Builder": ...
        def build(self) -> "PrinterCapabilitiesInfo": ...
