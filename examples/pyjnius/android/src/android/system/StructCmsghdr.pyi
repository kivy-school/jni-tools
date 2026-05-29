from typing import Any, ClassVar, overload

class StructCmsghdr:
    cmsg_data: Any
    cmsg_level: int
    cmsg_type: int
    @overload
    def __init__(self, p0: int, p1: int, p2: Any) -> None: ...
    @overload
    def __init__(self, p0: int, p1: int, p2: int) -> None: ...
