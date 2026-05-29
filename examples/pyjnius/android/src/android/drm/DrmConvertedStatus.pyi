from typing import Any, ClassVar, overload

class DrmConvertedStatus:
    STATUS_ERROR: ClassVar[int]
    STATUS_INPUTDATA_ERROR: ClassVar[int]
    STATUS_OK: ClassVar[int]
    convertedData: Any
    offset: int
    statusCode: int
    def __init__(self, p0: int, p1: Any, p2: int) -> None: ...
