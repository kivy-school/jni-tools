from typing import Any, ClassVar, overload

class AbstractSelectionKey:
    OP_READ: ClassVar[int]
    OP_WRITE: ClassVar[int]
    OP_CONNECT: ClassVar[int]
    OP_ACCEPT: ClassVar[int]
    def cancel(self) -> None: ...
    def isValid(self) -> bool: ...
