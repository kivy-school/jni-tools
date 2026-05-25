from typing import Any, ClassVar, overload

class AdInspectorError:
    ERROR_CODE_INTERNAL_ERROR: ClassVar[int]
    ERROR_CODE_FAILED_TO_LOAD: ClassVar[int]
    ERROR_CODE_NOT_IN_TEST_MODE: ClassVar[int]
    ERROR_CODE_ALREADY_OPEN: ClassVar[int]
    def __init__(self, arg0: int, arg1: str, arg2: str) -> None: ...
    def getCode(self) -> int: ...

    class AdInspectorErrorCode:
        ...
