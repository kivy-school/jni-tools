from typing import Any, ClassVar, overload

class LSException:
    PARSE_ERR: ClassVar[int]
    SERIALIZE_ERR: ClassVar[int]
    code: int
    def __init__(self, arg0: int, arg1: str) -> None: ...
