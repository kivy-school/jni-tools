from typing import Any, ClassVar, overload

class DataSpace:
    DATASPACE_ADOBE_RGB: ClassVar[int]
    DATASPACE_BT2020: ClassVar[int]
    DATASPACE_BT2020_HLG: ClassVar[int]
    DATASPACE_BT2020_PQ: ClassVar[int]
    DATASPACE_BT601_525: ClassVar[int]
    DATASPACE_BT601_625: ClassVar[int]
    DATASPACE_BT709: ClassVar[int]
    DATASPACE_DCI_P3: ClassVar[int]
    DATASPACE_DEPTH: ClassVar[int]
    DATASPACE_DISPLAY_P3: ClassVar[int]
    DATASPACE_DYNAMIC_DEPTH: ClassVar[int]
    DATASPACE_HEIF: ClassVar[int]
    DATASPACE_HEIF_ULTRAHDR: ClassVar[int]
    DATASPACE_JFIF: ClassVar[int]
    DATASPACE_JPEG_R: ClassVar[int]
    DATASPACE_SCRGB: ClassVar[int]
    DATASPACE_SCRGB_LINEAR: ClassVar[int]
    DATASPACE_SRGB: ClassVar[int]
    DATASPACE_SRGB_LINEAR: ClassVar[int]
    DATASPACE_UNKNOWN: ClassVar[int]
    RANGE_EXTENDED: ClassVar[int]
    RANGE_FULL: ClassVar[int]
    RANGE_LIMITED: ClassVar[int]
    RANGE_UNSPECIFIED: ClassVar[int]
    STANDARD_ADOBE_RGB: ClassVar[int]
    STANDARD_BT2020: ClassVar[int]
    STANDARD_BT2020_CONSTANT_LUMINANCE: ClassVar[int]
    STANDARD_BT470M: ClassVar[int]
    STANDARD_BT601_525: ClassVar[int]
    STANDARD_BT601_525_UNADJUSTED: ClassVar[int]
    STANDARD_BT601_625: ClassVar[int]
    STANDARD_BT601_625_UNADJUSTED: ClassVar[int]
    STANDARD_BT709: ClassVar[int]
    STANDARD_DCI_P3: ClassVar[int]
    STANDARD_FILM: ClassVar[int]
    STANDARD_UNSPECIFIED: ClassVar[int]
    TRANSFER_GAMMA2_2: ClassVar[int]
    TRANSFER_GAMMA2_6: ClassVar[int]
    TRANSFER_GAMMA2_8: ClassVar[int]
    TRANSFER_HLG: ClassVar[int]
    TRANSFER_LINEAR: ClassVar[int]
    TRANSFER_SMPTE_170M: ClassVar[int]
    TRANSFER_SRGB: ClassVar[int]
    TRANSFER_ST2084: ClassVar[int]
    TRANSFER_UNSPECIFIED: ClassVar[int]
    @staticmethod
    def getRange(p0: int) -> int: ...
    @staticmethod
    def getStandard(p0: int) -> int: ...
    @staticmethod
    def getTransfer(p0: int) -> int: ...
    @staticmethod
    def pack(p0: int, p1: int, p2: int) -> int: ...
