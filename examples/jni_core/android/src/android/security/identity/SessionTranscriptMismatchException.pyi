from typing import Any, ClassVar, overload
from java.lang.Throwable import Throwable

class SessionTranscriptMismatchException:
    @overload
    def __init__(self, p0: str) -> None: ...
    @overload
    def __init__(self, p0: str, p1: Throwable) -> None: ...
