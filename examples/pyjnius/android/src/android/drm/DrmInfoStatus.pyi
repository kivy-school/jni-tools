from typing import Any, ClassVar, overload
from android.drm.ProcessedData import ProcessedData

class DrmInfoStatus:
    STATUS_ERROR: ClassVar[int]
    STATUS_OK: ClassVar[int]
    data: ProcessedData
    infoType: int
    mimeType: str
    statusCode: int
    def __init__(self, p0: int, p1: int, p2: ProcessedData, p3: str) -> None: ...
