from typing import Any, ClassVar, overload

class DrmConvertedStatus:
    STATUS_ERROR: ClassVar[int]
    STATUS_INPUTDATA_ERROR: ClassVar[int]
    STATUS_OK: ClassVar[int]
    convertedData: list[int]
    offset: int
    statusCode: int
    def __init__(self, arg0: int, arg1: list[int], arg2: int) -> None: ...
