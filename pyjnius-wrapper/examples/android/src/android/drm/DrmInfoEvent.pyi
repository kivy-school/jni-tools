from typing import Any, ClassVar, overload

class DrmInfoEvent:
    TYPE_ACCOUNT_ALREADY_REGISTERED: ClassVar[int]
    TYPE_ALREADY_REGISTERED_BY_ANOTHER_ACCOUNT: ClassVar[int]
    TYPE_REMOVE_RIGHTS: ClassVar[int]
    TYPE_RIGHTS_INSTALLED: ClassVar[int]
    TYPE_RIGHTS_REMOVED: ClassVar[int]
    TYPE_WAIT_FOR_RIGHTS: ClassVar[int]
    @overload
    def __init__(self, arg0: int, arg1: int, arg2: str) -> None: ...
    @overload
    def __init__(self, arg0: int, arg1: int, arg2: str, arg3: dict) -> None: ...
