from typing import Any, ClassVar, overload
from android.app.appsearch.BatchResultCallback import BatchResultCallback
from android.app.appsearch.GetByDocumentIdRequest import GetByDocumentIdRequest
from android.app.appsearch.SearchResults import SearchResults
from android.app.appsearch.SearchSpec import SearchSpec
from java.util.concurrent.Executor import Executor
from java.util.function.Consumer import Consumer

class EnterpriseGlobalSearchSession:
    def getByDocumentId(self, p0: str, p1: str, p2: GetByDocumentIdRequest, p3: Executor, p4: BatchResultCallback) -> None: ...
    def getSchema(self, p0: str, p1: str, p2: Executor, p3: Consumer) -> None: ...
    def search(self, p0: str, p1: SearchSpec) -> SearchResults: ...
