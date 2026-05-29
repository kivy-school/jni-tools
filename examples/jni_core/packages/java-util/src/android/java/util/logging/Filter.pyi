from typing import Any, ClassVar, overload
from java.util.logging.LogRecord import LogRecord

class Filter:
    def isLoggable(self, p0: LogRecord) -> bool: ...
