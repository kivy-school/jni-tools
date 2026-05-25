from typing import Any, ClassVar, overload
from java.io.BufferedReader import BufferedReader

class EventLogTags:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, p0: BufferedReader) -> None: ...
    @overload
    def get(self, p0: int) -> Any: ...
    @overload
    def get(self, p0: str) -> Any: ...

    class Description:
        mName: str
        mTag: int
