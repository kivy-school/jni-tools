from typing import Any, ClassVar, overload

class ConnectionlessHandwritingCallback:
    CONNECTIONLESS_HANDWRITING_ERROR_NO_TEXT_RECOGNIZED: ClassVar[int]
    CONNECTIONLESS_HANDWRITING_ERROR_OTHER: ClassVar[int]
    CONNECTIONLESS_HANDWRITING_ERROR_UNSUPPORTED: ClassVar[int]
    def onResult(self, arg0: str) -> None: ...
    def onError(self, arg0: int) -> None: ...
