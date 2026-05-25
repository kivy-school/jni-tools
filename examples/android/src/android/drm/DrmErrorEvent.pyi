from typing import Any, ClassVar, overload

class DrmErrorEvent:
    TYPE_ACQUIRE_DRM_INFO_FAILED: ClassVar[int]
    TYPE_NOT_SUPPORTED: ClassVar[int]
    TYPE_NO_INTERNET_CONNECTION: ClassVar[int]
    TYPE_OUT_OF_MEMORY: ClassVar[int]
    TYPE_PROCESS_DRM_INFO_FAILED: ClassVar[int]
    TYPE_REMOVE_ALL_RIGHTS_FAILED: ClassVar[int]
    TYPE_RIGHTS_NOT_INSTALLED: ClassVar[int]
    TYPE_RIGHTS_RENEWAL_NOT_ALLOWED: ClassVar[int]
    @overload
    def __init__(self, arg0: int, arg1: int, arg2: str) -> None: ...
    @overload
    def __init__(self, arg0: int, arg1: int, arg2: str, arg3: dict) -> None: ...
