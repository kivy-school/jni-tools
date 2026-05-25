from typing import Any, ClassVar, overload
from java.util.concurrent.Executor import Executor
from java.util.function.Consumer import Consumer

class SearchResults:
    def getNextPage(self, arg0: Executor, arg1: Consumer) -> None: ...
    def close(self) -> None: ...
