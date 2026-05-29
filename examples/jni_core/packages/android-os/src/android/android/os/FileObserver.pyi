from typing import Any, ClassVar, overload
from java.io.File import File

class FileObserver:
    ACCESS: ClassVar[int]
    ALL_EVENTS: ClassVar[int]
    ATTRIB: ClassVar[int]
    CLOSE_NOWRITE: ClassVar[int]
    CLOSE_WRITE: ClassVar[int]
    CREATE: ClassVar[int]
    DELETE: ClassVar[int]
    DELETE_SELF: ClassVar[int]
    MODIFY: ClassVar[int]
    MOVED_FROM: ClassVar[int]
    MOVED_TO: ClassVar[int]
    MOVE_SELF: ClassVar[int]
    OPEN: ClassVar[int]
    @overload
    def __init__(self, p0: File, p1: int) -> None: ...
    @overload
    def __init__(self, p0: list, p1: int) -> None: ...
    @overload
    def __init__(self, p0: str) -> None: ...
    @overload
    def __init__(self, p0: File) -> None: ...
    @overload
    def __init__(self, p0: str, p1: int) -> None: ...
    @overload
    def __init__(self, p0: list) -> None: ...
    def startWatching(self) -> None: ...
    def stopWatching(self) -> None: ...
    def onEvent(self, p0: int, p1: str) -> None: ...
