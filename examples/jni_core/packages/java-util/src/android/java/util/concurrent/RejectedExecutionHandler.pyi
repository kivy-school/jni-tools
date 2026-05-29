from typing import Any, ClassVar, overload
from java.lang.Runnable import Runnable
from java.util.concurrent.ThreadPoolExecutor import ThreadPoolExecutor

class RejectedExecutionHandler:
    def rejectedExecution(self, p0: Runnable, p1: ThreadPoolExecutor) -> None: ...
