from typing import Any, ClassVar, overload
from android.app.appsearch.AppSearchBatchResult import AppSearchBatchResult
from java.lang.Throwable import Throwable

class BatchResultCallback:
    def onResult(self, arg0: AppSearchBatchResult) -> None: ...
    def onSystemError(self, arg0: Throwable) -> None: ...
