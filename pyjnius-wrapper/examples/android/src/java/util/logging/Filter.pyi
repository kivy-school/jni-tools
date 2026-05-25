from typing import Any, ClassVar, overload
from java.util.logging.LogRecord import LogRecord

class Filter:
    def isLoggable(self, arg0: LogRecord) -> bool: ...
