from typing import Any, ClassVar, overload
from java.util.concurrent.TimeUnit import TimeUnit

class Delayed:
    def getDelay(self, p0: TimeUnit) -> int: ...
