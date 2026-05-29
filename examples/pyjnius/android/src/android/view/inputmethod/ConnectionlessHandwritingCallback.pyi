from typing import Any, ClassVar, overload

class ConnectionlessHandwritingCallback:
    CONNECTIONLESS_HANDWRITING_ERROR_NO_TEXT_RECOGNIZED: ClassVar[int]
    CONNECTIONLESS_HANDWRITING_ERROR_OTHER: ClassVar[int]
    CONNECTIONLESS_HANDWRITING_ERROR_UNSUPPORTED: ClassVar[int]
    def onError(self, p0: int) -> None: ...
    def onResult(self, p0: str) -> None: ...
