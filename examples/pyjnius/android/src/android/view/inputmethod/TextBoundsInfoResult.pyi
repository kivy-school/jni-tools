from typing import Any, ClassVar, overload
from android.view.inputmethod.TextBoundsInfo import TextBoundsInfo

class TextBoundsInfoResult:
    CODE_CANCELLED: ClassVar[int]
    CODE_FAILED: ClassVar[int]
    CODE_SUCCESS: ClassVar[int]
    CODE_UNSUPPORTED: ClassVar[int]
    @overload
    def __init__(self, arg0: int) -> None: ...
    @overload
    def __init__(self, arg0: int, arg1: TextBoundsInfo) -> None: ...
    def getResultCode(self) -> int: ...
    def getTextBoundsInfo(self) -> TextBoundsInfo: ...
