from typing import Any, ClassVar, overload
from android.health.connect.datatypes.Metadata import Metadata
from java.time.Instant import Instant
from java.time.ZoneOffset import ZoneOffset

class CervicalMucusRecord:
    def equals(self, p0: Any) -> bool: ...
    def hashCode(self) -> int: ...
    def getSensation(self) -> int: ...
    def getAppearance(self) -> int: ...

    class CervicalMucusSensation:
        SENSATION_HEAVY: ClassVar[int]
        SENSATION_LIGHT: ClassVar[int]
        SENSATION_MEDIUM: ClassVar[int]
        SENSATION_UNKNOWN: ClassVar[int]

    class CervicalMucusAppearance:
        APPEARANCE_CREAMY: ClassVar[int]
        APPEARANCE_DRY: ClassVar[int]
        APPEARANCE_EGG_WHITE: ClassVar[int]
        APPEARANCE_STICKY: ClassVar[int]
        APPEARANCE_UNKNOWN: ClassVar[int]
        APPEARANCE_UNUSUAL: ClassVar[int]
        APPEARANCE_WATERY: ClassVar[int]

    class Builder:
        def __init__(self, p0: Metadata, p1: Instant, p2: int, p3: int) -> None: ...
        def build(self) -> "CervicalMucusRecord": ...
        def clearZoneOffset(self) -> Any: ...
        def setZoneOffset(self, p0: ZoneOffset) -> Any: ...
