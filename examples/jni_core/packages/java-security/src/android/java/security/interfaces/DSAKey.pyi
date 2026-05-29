from typing import Any, ClassVar, overload
from java.security.interfaces.DSAParams import DSAParams

class DSAKey:
    def getParams(self) -> DSAParams: ...
