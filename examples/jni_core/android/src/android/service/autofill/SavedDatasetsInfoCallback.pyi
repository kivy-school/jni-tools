from typing import Any, ClassVar, overload

class SavedDatasetsInfoCallback:
    ERROR_NEEDS_USER_ACTION: ClassVar[int]
    ERROR_OTHER: ClassVar[int]
    ERROR_UNSUPPORTED: ClassVar[int]
    def onSuccess(self, p0: set) -> None: ...
    def onError(self, p0: int) -> None: ...
