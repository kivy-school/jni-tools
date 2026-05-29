from typing import Any, ClassVar, overload
from java.lang.Runnable import Runnable
from java.lang.Thread import Thread

class ThreadFactory:
    def newThread(self, p0: Runnable) -> Thread: ...
