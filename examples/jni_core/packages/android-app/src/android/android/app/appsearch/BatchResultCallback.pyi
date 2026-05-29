from typing import Any, ClassVar, overload
from android.app.appsearch.AppSearchBatchResult import AppSearchBatchResult
from java.lang.Throwable import Throwable

class BatchResultCallback:
    def onSystemError(self, p0: Throwable) -> None: ...
    def onResult(self, p0: AppSearchBatchResult) -> None: ...
