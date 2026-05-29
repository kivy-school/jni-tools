from typing import Any, ClassVar, overload
from java.lang.Throwable import Throwable

class ServiceStartNotAllowedException:
    def getCause(self) -> Throwable: ...
