from typing import Any, ClassVar, overload
from android.app.appsearch.BatchResultCallback import BatchResultCallback
from android.app.appsearch.GetByDocumentIdRequest import GetByDocumentIdRequest
from android.app.appsearch.SearchResults import SearchResults
from android.app.appsearch.SearchSpec import SearchSpec
from java.util.concurrent.Executor import Executor
from java.util.function.Consumer import Consumer

class EnterpriseGlobalSearchSession:
    def search(self, arg0: str, arg1: SearchSpec) -> SearchResults: ...
    def getByDocumentId(self, arg0: str, arg1: str, arg2: GetByDocumentIdRequest, arg3: Executor, arg4: BatchResultCallback) -> None: ...
    def getSchema(self, arg0: str, arg1: str, arg2: Executor, arg3: Consumer) -> None: ...
