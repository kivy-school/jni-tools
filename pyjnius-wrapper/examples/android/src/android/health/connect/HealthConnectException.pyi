from typing import Any, ClassVar, overload

class HealthConnectException:
    ERROR_DATA_SYNC_IN_PROGRESS: ClassVar[int]
    ERROR_INTERNAL: ClassVar[int]
    ERROR_INVALID_ARGUMENT: ClassVar[int]
    ERROR_IO: ClassVar[int]
    ERROR_RATE_LIMIT_EXCEEDED: ClassVar[int]
    ERROR_REMOTE: ClassVar[int]
    ERROR_SECURITY: ClassVar[int]
    ERROR_UNKNOWN: ClassVar[int]
    ERROR_UNSUPPORTED_OPERATION: ClassVar[int]
    def getErrorCode(self) -> int: ...
