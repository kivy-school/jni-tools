from typing import Any, ClassVar, overload
from android.health.connect.datatypes.Metadata import Metadata
from java.time.Instant import Instant
from java.time.ZoneOffset import ZoneOffset

class CervicalMucusRecord:
    def getSensation(self) -> int: ...
    def getAppearance(self) -> int: ...
    def equals(self, arg0: Any) -> bool: ...
    def hashCode(self) -> int: ...

    class Builder:
        def __init__(self, arg0: Metadata, arg1: Instant, arg2: int, arg3: int) -> None: ...
        def setZoneOffset(self, arg0: ZoneOffset) -> "Builder": ...
        def clearZoneOffset(self) -> "Builder": ...
        def build(self) -> "CervicalMucusRecord": ...

    class CervicalMucusAppearance:
        APPEARANCE_CREAMY: ClassVar[int]
        APPEARANCE_DRY: ClassVar[int]
        APPEARANCE_EGG_WHITE: ClassVar[int]
        APPEARANCE_STICKY: ClassVar[int]
        APPEARANCE_UNKNOWN: ClassVar[int]
        APPEARANCE_UNUSUAL: ClassVar[int]
        APPEARANCE_WATERY: ClassVar[int]

    class CervicalMucusSensation:
        SENSATION_HEAVY: ClassVar[int]
        SENSATION_LIGHT: ClassVar[int]
        SENSATION_MEDIUM: ClassVar[int]
        SENSATION_UNKNOWN: ClassVar[int]
