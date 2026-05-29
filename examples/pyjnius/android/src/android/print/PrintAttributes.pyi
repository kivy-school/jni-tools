from typing import Any, ClassVar, overload
from android.content.pm.PackageManager import PackageManager
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

class PrintAttributes:
    COLOR_MODE_COLOR: ClassVar[int]
    COLOR_MODE_MONOCHROME: ClassVar[int]
    CREATOR: ClassVar[Creator]
    DUPLEX_MODE_LONG_EDGE: ClassVar[int]
    DUPLEX_MODE_NONE: ClassVar[int]
    DUPLEX_MODE_SHORT_EDGE: ClassVar[int]
    def getMediaSize(self) -> "MediaSize": ...
    def getResolution(self) -> "Resolution": ...
    def getMinMargins(self) -> "Margins": ...
    def getColorMode(self) -> int: ...
    def getDuplexMode(self) -> int: ...
    def writeToParcel(self, arg0: Parcel, arg1: int) -> None: ...
    def describeContents(self) -> int: ...
    def hashCode(self) -> int: ...
    def equals(self, arg0: Any) -> bool: ...
    def toString(self) -> str: ...

    class Builder:
        def __init__(self) -> None: ...
        def setMediaSize(self, arg0: "MediaSize") -> "Builder": ...
        def setResolution(self, arg0: "Resolution") -> "Builder": ...
        def setMinMargins(self, arg0: "Margins") -> "Builder": ...
        def setColorMode(self, arg0: int) -> "Builder": ...
        def setDuplexMode(self, arg0: int) -> "Builder": ...
        def build(self) -> "PrintAttributes": ...

    class Margins:
        NO_MARGINS: ClassVar["Margins"]
        def __init__(self, arg0: int, arg1: int, arg2: int, arg3: int) -> None: ...
        def getLeftMils(self) -> int: ...
        def getTopMils(self) -> int: ...
        def getRightMils(self) -> int: ...
        def getBottomMils(self) -> int: ...
        def hashCode(self) -> int: ...
        def equals(self, arg0: Any) -> bool: ...
        def toString(self) -> str: ...

    class MediaSize:
        ANSI_C: ClassVar["MediaSize"]
        ANSI_D: ClassVar["MediaSize"]
        ANSI_E: ClassVar["MediaSize"]
        ANSI_F: ClassVar["MediaSize"]
        ISO_A0: ClassVar["MediaSize"]
        ISO_A1: ClassVar["MediaSize"]
        ISO_A10: ClassVar["MediaSize"]
        ISO_A2: ClassVar["MediaSize"]
        ISO_A3: ClassVar["MediaSize"]
        ISO_A4: ClassVar["MediaSize"]
        ISO_A5: ClassVar["MediaSize"]
        ISO_A6: ClassVar["MediaSize"]
        ISO_A7: ClassVar["MediaSize"]
        ISO_A8: ClassVar["MediaSize"]
        ISO_A9: ClassVar["MediaSize"]
        ISO_B0: ClassVar["MediaSize"]
        ISO_B1: ClassVar["MediaSize"]
        ISO_B10: ClassVar["MediaSize"]
        ISO_B2: ClassVar["MediaSize"]
        ISO_B3: ClassVar["MediaSize"]
        ISO_B4: ClassVar["MediaSize"]
        ISO_B5: ClassVar["MediaSize"]
        ISO_B6: ClassVar["MediaSize"]
        ISO_B7: ClassVar["MediaSize"]
        ISO_B8: ClassVar["MediaSize"]
        ISO_B9: ClassVar["MediaSize"]
        ISO_C0: ClassVar["MediaSize"]
        ISO_C1: ClassVar["MediaSize"]
        ISO_C10: ClassVar["MediaSize"]
        ISO_C2: ClassVar["MediaSize"]
        ISO_C3: ClassVar["MediaSize"]
        ISO_C4: ClassVar["MediaSize"]
        ISO_C5: ClassVar["MediaSize"]
        ISO_C6: ClassVar["MediaSize"]
        ISO_C7: ClassVar["MediaSize"]
        ISO_C8: ClassVar["MediaSize"]
        ISO_C9: ClassVar["MediaSize"]
        JIS_B0: ClassVar["MediaSize"]
        JIS_B1: ClassVar["MediaSize"]
        JIS_B10: ClassVar["MediaSize"]
        JIS_B2: ClassVar["MediaSize"]
        JIS_B3: ClassVar["MediaSize"]
        JIS_B4: ClassVar["MediaSize"]
        JIS_B5: ClassVar["MediaSize"]
        JIS_B6: ClassVar["MediaSize"]
        JIS_B7: ClassVar["MediaSize"]
        JIS_B8: ClassVar["MediaSize"]
        JIS_B9: ClassVar["MediaSize"]
        JIS_EXEC: ClassVar["MediaSize"]
        JPN_CHOU2: ClassVar["MediaSize"]
        JPN_CHOU3: ClassVar["MediaSize"]
        JPN_CHOU4: ClassVar["MediaSize"]
        JPN_HAGAKI: ClassVar["MediaSize"]
        JPN_KAHU: ClassVar["MediaSize"]
        JPN_KAKU2: ClassVar["MediaSize"]
        JPN_OE_PHOTO_L: ClassVar["MediaSize"]
        JPN_OUFUKU: ClassVar["MediaSize"]
        JPN_YOU4: ClassVar["MediaSize"]
        NA_ARCH_A: ClassVar["MediaSize"]
        NA_ARCH_B: ClassVar["MediaSize"]
        NA_ARCH_C: ClassVar["MediaSize"]
        NA_ARCH_D: ClassVar["MediaSize"]
        NA_ARCH_E: ClassVar["MediaSize"]
        NA_ARCH_E1: ClassVar["MediaSize"]
        NA_FOOLSCAP: ClassVar["MediaSize"]
        NA_GOVT_LETTER: ClassVar["MediaSize"]
        NA_INDEX_3X5: ClassVar["MediaSize"]
        NA_INDEX_4X6: ClassVar["MediaSize"]
        NA_INDEX_5X8: ClassVar["MediaSize"]
        NA_JUNIOR_LEGAL: ClassVar["MediaSize"]
        NA_LEDGER: ClassVar["MediaSize"]
        NA_LEGAL: ClassVar["MediaSize"]
        NA_LETTER: ClassVar["MediaSize"]
        NA_MONARCH: ClassVar["MediaSize"]
        NA_QUARTO: ClassVar["MediaSize"]
        NA_SUPER_B: ClassVar["MediaSize"]
        NA_TABLOID: ClassVar["MediaSize"]
        OM_DAI_PA_KAI: ClassVar["MediaSize"]
        OM_JUURO_KU_KAI: ClassVar["MediaSize"]
        OM_PA_KAI: ClassVar["MediaSize"]
        PRC_1: ClassVar["MediaSize"]
        PRC_10: ClassVar["MediaSize"]
        PRC_16K: ClassVar["MediaSize"]
        PRC_2: ClassVar["MediaSize"]
        PRC_3: ClassVar["MediaSize"]
        PRC_4: ClassVar["MediaSize"]
        PRC_5: ClassVar["MediaSize"]
        PRC_6: ClassVar["MediaSize"]
        PRC_7: ClassVar["MediaSize"]
        PRC_8: ClassVar["MediaSize"]
        PRC_9: ClassVar["MediaSize"]
        ROC_16K: ClassVar["MediaSize"]
        ROC_8K: ClassVar["MediaSize"]
        UNKNOWN_LANDSCAPE: ClassVar["MediaSize"]
        UNKNOWN_PORTRAIT: ClassVar["MediaSize"]
        def __init__(self, arg0: str, arg1: str, arg2: int, arg3: int) -> None: ...
        def getId(self) -> str: ...
        def getLabel(self, arg0: PackageManager) -> str: ...
        def getWidthMils(self) -> int: ...
        def getHeightMils(self) -> int: ...
        def isPortrait(self) -> bool: ...
        def asPortrait(self) -> "MediaSize": ...
        def asLandscape(self) -> "MediaSize": ...
        def hashCode(self) -> int: ...
        def equals(self, arg0: Any) -> bool: ...
        def toString(self) -> str: ...

    class Resolution:
        def __init__(self, arg0: str, arg1: str, arg2: int, arg3: int) -> None: ...
        def getId(self) -> str: ...
        def getLabel(self) -> str: ...
        def getHorizontalDpi(self) -> int: ...
        def getVerticalDpi(self) -> int: ...
        def hashCode(self) -> int: ...
        def equals(self, arg0: Any) -> bool: ...
        def toString(self) -> str: ...
