from typing import Any, ClassVar, overload

class StructCmsghdr:
    cmsg_data: list[int]
    cmsg_level: int
    cmsg_type: int
    @overload
    def __init__(self, arg0: int, arg1: int, arg2: int) -> None: ...
    @overload
    def __init__(self, arg0: int, arg1: int, arg2: list[int]) -> None: ...
