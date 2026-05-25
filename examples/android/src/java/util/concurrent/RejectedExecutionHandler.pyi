from typing import Any, ClassVar, overload
from java.lang.Runnable import Runnable
from java.util.concurrent.ThreadPoolExecutor import ThreadPoolExecutor

class RejectedExecutionHandler:
    def rejectedExecution(self, arg0: Runnable, arg1: ThreadPoolExecutor) -> None: ...
