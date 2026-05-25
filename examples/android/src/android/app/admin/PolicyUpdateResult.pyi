from typing import Any, ClassVar, overload

class PolicyUpdateResult:
    RESULT_FAILURE_CONFLICTING_ADMIN_POLICY: ClassVar[int]
    RESULT_FAILURE_HARDWARE_LIMITATION: ClassVar[int]
    RESULT_FAILURE_STORAGE_LIMIT_REACHED: ClassVar[int]
    RESULT_FAILURE_UNKNOWN: ClassVar[int]
    RESULT_POLICY_CLEARED: ClassVar[int]
    RESULT_POLICY_SET: ClassVar[int]
    def __init__(self, arg0: int) -> None: ...
    def getResultCode(self) -> int: ...
