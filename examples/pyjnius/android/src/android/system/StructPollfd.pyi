from typing import Any, ClassVar, overload
from java.io.FileDescriptor import FileDescriptor

class StructPollfd:
    events: int
    fd: FileDescriptor
    revents: int
    userData: Any
    def __init__(self) -> None: ...
    def toString(self) -> str: ...
