from typing import Any, ClassVar, overload
from android.view.displayhash.DisplayHash import DisplayHash

class DisplayHashResultCallback:
    DISPLAY_HASH_ERROR_INVALID_BOUNDS: ClassVar[int]
    DISPLAY_HASH_ERROR_INVALID_HASH_ALGORITHM: ClassVar[int]
    DISPLAY_HASH_ERROR_MISSING_WINDOW: ClassVar[int]
    DISPLAY_HASH_ERROR_NOT_VISIBLE_ON_SCREEN: ClassVar[int]
    DISPLAY_HASH_ERROR_TOO_MANY_REQUESTS: ClassVar[int]
    DISPLAY_HASH_ERROR_UNKNOWN: ClassVar[int]
    def onDisplayHashResult(self, arg0: DisplayHash) -> None: ...
    def onDisplayHashError(self, arg0: int) -> None: ...
