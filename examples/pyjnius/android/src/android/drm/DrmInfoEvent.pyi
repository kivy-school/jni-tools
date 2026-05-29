from typing import Any, ClassVar, overload

class DrmInfoEvent:
    TYPE_ACCOUNT_ALREADY_REGISTERED: ClassVar[int]
    TYPE_ALREADY_REGISTERED_BY_ANOTHER_ACCOUNT: ClassVar[int]
    TYPE_REMOVE_RIGHTS: ClassVar[int]
    TYPE_RIGHTS_INSTALLED: ClassVar[int]
    TYPE_RIGHTS_REMOVED: ClassVar[int]
    TYPE_WAIT_FOR_RIGHTS: ClassVar[int]
    DRM_INFO_OBJECT: ClassVar[str]
    DRM_INFO_STATUS_OBJECT: ClassVar[str]
    TYPE_ALL_RIGHTS_REMOVED: ClassVar[int]
    TYPE_DRM_INFO_PROCESSED: ClassVar[int]
    @overload
    def __init__(self, p0: int, p1: int, p2: str) -> None: ...
    @overload
    def __init__(self, p0: int, p1: int, p2: str, p3: dict) -> None: ...
