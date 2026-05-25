from typing import Any, ClassVar, overload
from java.security.spec.AlgorithmParameterSpec import AlgorithmParameterSpec

class XECKey:
    def getParams(self) -> AlgorithmParameterSpec: ...
