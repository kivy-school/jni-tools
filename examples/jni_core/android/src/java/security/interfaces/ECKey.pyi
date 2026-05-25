from typing import Any, ClassVar, overload
from java.security.spec.ECParameterSpec import ECParameterSpec

class ECKey:
    def getParams(self) -> ECParameterSpec: ...
