from typing import Any, ClassVar, overload
from java.security.spec.NamedParameterSpec import NamedParameterSpec

class EdECKey:
    def getParams(self) -> NamedParameterSpec: ...
