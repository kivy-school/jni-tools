from typing import Any, ClassVar, overload
from java.util.concurrent.Executor import Executor
from java.util.function.Consumer import Consumer

class SearchResults:
    def close(self) -> None: ...
    def getNextPage(self, p0: Executor, p1: Consumer) -> None: ...
