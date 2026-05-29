from typing import Any, ClassVar, overload
from android.content.Context import Context

class Browser:
    EXTRA_APPLICATION_ID: ClassVar[str]
    EXTRA_CREATE_NEW_TAB: ClassVar[str]
    EXTRA_HEADERS: ClassVar[str]
    INITIAL_ZOOM_LEVEL: ClassVar[str]
    def __init__(self) -> None: ...
    @staticmethod
    def sendString(p0: Context, p1: str) -> None: ...
