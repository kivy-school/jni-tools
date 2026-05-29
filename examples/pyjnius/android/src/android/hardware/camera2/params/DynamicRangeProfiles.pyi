from typing import Any, ClassVar, overload

class DynamicRangeProfiles:
    DOLBY_VISION_10B_HDR_OEM: ClassVar[int]
    DOLBY_VISION_10B_HDR_OEM_PO: ClassVar[int]
    DOLBY_VISION_10B_HDR_REF: ClassVar[int]
    DOLBY_VISION_10B_HDR_REF_PO: ClassVar[int]
    DOLBY_VISION_8B_HDR_OEM: ClassVar[int]
    DOLBY_VISION_8B_HDR_OEM_PO: ClassVar[int]
    DOLBY_VISION_8B_HDR_REF: ClassVar[int]
    DOLBY_VISION_8B_HDR_REF_PO: ClassVar[int]
    HDR10: ClassVar[int]
    HDR10_PLUS: ClassVar[int]
    HLG10: ClassVar[int]
    PUBLIC_MAX: ClassVar[int]
    STANDARD: ClassVar[int]
    def __init__(self, arg0: list[int]) -> None: ...
    def getSupportedProfiles(self) -> set: ...
    def getProfileCaptureRequestConstraints(self, arg0: int) -> set: ...
    def isExtraLatencyPresent(self, arg0: int) -> bool: ...
