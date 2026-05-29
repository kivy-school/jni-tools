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
    DRM_INFO_OBJECT: ClassVar[str]
    DRM_INFO_STATUS_OBJECT: ClassVar[str]
    TYPE_ALL_RIGHTS_REMOVED: ClassVar[int]
    TYPE_DRM_INFO_PROCESSED: ClassVar[int]
    @overload
    def __init__(self, p0: int, p1: int, p2: str) -> None: ...
    @overload
    def __init__(self, p0: int, p1: int, p2: str, p3: dict) -> None: ...
