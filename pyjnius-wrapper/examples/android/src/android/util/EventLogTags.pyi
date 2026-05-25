from typing import Any, ClassVar, overload
from java.io.BufferedReader import BufferedReader

class EventLogTags:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, arg0: BufferedReader) -> None: ...
    @overload
    def get(self, arg0: str) -> "Description": ...
    @overload
    def get(self, arg0: int) -> "Description": ...

    class Description:
        mName: str
        mTag: int
