from typing import Any, ClassVar, overload
from android.content.pm.PackageManager import PackageManager
from android.os.Parcel import Parcel

class PrintAttributes:
    COLOR_MODE_COLOR: ClassVar[int]
    COLOR_MODE_MONOCHROME: ClassVar[int]
    CREATOR: ClassVar[Any]
    DUPLEX_MODE_LONG_EDGE: ClassVar[int]
    DUPLEX_MODE_NONE: ClassVar[int]
    DUPLEX_MODE_SHORT_EDGE: ClassVar[int]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    def getColorMode(self) -> int: ...
    def getDuplexMode(self) -> int: ...
    def getMinMargins(self) -> Any: ...
    def equals(self, p0: Any) -> bool: ...
    def toString(self) -> str: ...
    def hashCode(self) -> int: ...
    def getMediaSize(self) -> Any: ...
    def getResolution(self) -> Any: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...
    def describeContents(self) -> int: ...

    class Resolution:
        def __init__(self, p0: str, p1: str, p2: int, p3: int) -> None: ...
        def getHorizontalDpi(self) -> int: ...
        def getVerticalDpi(self) -> int: ...
        def equals(self, p0: Any) -> bool: ...
        def toString(self) -> str: ...
        def hashCode(self) -> int: ...
        def getId(self) -> str: ...
        def getLabel(self) -> str: ...

    class MediaSize:
        ANSI_C: ClassVar[Any]
        ANSI_D: ClassVar[Any]
        ANSI_E: ClassVar[Any]
        ANSI_F: ClassVar[Any]
        ISO_A0: ClassVar[Any]
        ISO_A1: ClassVar[Any]
        ISO_A10: ClassVar[Any]
        ISO_A2: ClassVar[Any]
        ISO_A3: ClassVar[Any]
        ISO_A4: ClassVar[Any]
        ISO_A5: ClassVar[Any]
        ISO_A6: ClassVar[Any]
        ISO_A7: ClassVar[Any]
        ISO_A8: ClassVar[Any]
        ISO_A9: ClassVar[Any]
        ISO_B0: ClassVar[Any]
        ISO_B1: ClassVar[Any]
        ISO_B10: ClassVar[Any]
        ISO_B2: ClassVar[Any]
        ISO_B3: ClassVar[Any]
        ISO_B4: ClassVar[Any]
        ISO_B5: ClassVar[Any]
        ISO_B6: ClassVar[Any]
        ISO_B7: ClassVar[Any]
        ISO_B8: ClassVar[Any]
        ISO_B9: ClassVar[Any]
        ISO_C0: ClassVar[Any]
        ISO_C1: ClassVar[Any]
        ISO_C10: ClassVar[Any]
        ISO_C2: ClassVar[Any]
        ISO_C3: ClassVar[Any]
        ISO_C4: ClassVar[Any]
        ISO_C5: ClassVar[Any]
        ISO_C6: ClassVar[Any]
        ISO_C7: ClassVar[Any]
        ISO_C8: ClassVar[Any]
        ISO_C9: ClassVar[Any]
        JIS_B0: ClassVar[Any]
        JIS_B1: ClassVar[Any]
        JIS_B10: ClassVar[Any]
        JIS_B2: ClassVar[Any]
        JIS_B3: ClassVar[Any]
        JIS_B4: ClassVar[Any]
        JIS_B5: ClassVar[Any]
        JIS_B6: ClassVar[Any]
        JIS_B7: ClassVar[Any]
        JIS_B8: ClassVar[Any]
        JIS_B9: ClassVar[Any]
        JIS_EXEC: ClassVar[Any]
        JPN_CHOU2: ClassVar[Any]
        JPN_CHOU3: ClassVar[Any]
        JPN_CHOU4: ClassVar[Any]
        JPN_HAGAKI: ClassVar[Any]
        JPN_KAHU: ClassVar[Any]
        JPN_KAKU2: ClassVar[Any]
        JPN_OE_PHOTO_L: ClassVar[Any]
        JPN_OUFUKU: ClassVar[Any]
        JPN_YOU4: ClassVar[Any]
        NA_ARCH_A: ClassVar[Any]
        NA_ARCH_B: ClassVar[Any]
        NA_ARCH_C: ClassVar[Any]
        NA_ARCH_D: ClassVar[Any]
        NA_ARCH_E: ClassVar[Any]
        NA_ARCH_E1: ClassVar[Any]
        NA_FOOLSCAP: ClassVar[Any]
        NA_GOVT_LETTER: ClassVar[Any]
        NA_INDEX_3X5: ClassVar[Any]
        NA_INDEX_4X6: ClassVar[Any]
        NA_INDEX_5X8: ClassVar[Any]
        NA_JUNIOR_LEGAL: ClassVar[Any]
        NA_LEDGER: ClassVar[Any]
        NA_LEGAL: ClassVar[Any]
        NA_LETTER: ClassVar[Any]
        NA_MONARCH: ClassVar[Any]
        NA_QUARTO: ClassVar[Any]
        NA_SUPER_B: ClassVar[Any]
        NA_TABLOID: ClassVar[Any]
        OM_DAI_PA_KAI: ClassVar[Any]
        OM_JUURO_KU_KAI: ClassVar[Any]
        OM_PA_KAI: ClassVar[Any]
        PRC_1: ClassVar[Any]
        PRC_10: ClassVar[Any]
        PRC_16K: ClassVar[Any]
        PRC_2: ClassVar[Any]
        PRC_3: ClassVar[Any]
        PRC_4: ClassVar[Any]
        PRC_5: ClassVar[Any]
        PRC_6: ClassVar[Any]
        PRC_7: ClassVar[Any]
        PRC_8: ClassVar[Any]
        PRC_9: ClassVar[Any]
        ROC_16K: ClassVar[Any]
        ROC_8K: ClassVar[Any]
        UNKNOWN_LANDSCAPE: ClassVar[Any]
        UNKNOWN_PORTRAIT: ClassVar[Any]
        def __init__(self, p0: str, p1: str, p2: int, p3: int) -> None: ...
        def asLandscape(self) -> Any: ...
        def asPortrait(self) -> Any: ...
        def getHeightMils(self) -> int: ...
        def getWidthMils(self) -> int: ...
        def isPortrait(self) -> bool: ...
        def equals(self, p0: Any) -> bool: ...
        def toString(self) -> str: ...
        def hashCode(self) -> int: ...
        def getId(self) -> str: ...
        def getLabel(self, p0: PackageManager) -> str: ...

    class Margins:
        NO_MARGINS: ClassVar[Any]
        def __init__(self, p0: int, p1: int, p2: int, p3: int) -> None: ...
        def getBottomMils(self) -> int: ...
        def getLeftMils(self) -> int: ...
        def getRightMils(self) -> int: ...
        def getTopMils(self) -> int: ...
        def equals(self, p0: Any) -> bool: ...
        def toString(self) -> str: ...
        def hashCode(self) -> int: ...

    class Builder:
        def __init__(self) -> None: ...
        def setColorMode(self, p0: int) -> Any: ...
        def setDuplexMode(self, p0: int) -> Any: ...
        def setMediaSize(self, p0: Any) -> Any: ...
        def setMinMargins(self, p0: Any) -> Any: ...
        def setResolution(self, p0: Any) -> Any: ...
        def build(self) -> "PrintAttributes": ...
