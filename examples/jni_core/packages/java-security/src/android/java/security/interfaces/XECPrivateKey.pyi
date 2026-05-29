from typing import Any, ClassVar, overload
from java.security.spec.AlgorithmParameterSpec import AlgorithmParameterSpec
from java.util.Optional import Optional

class XECPrivateKey:
    serialVersionUID: ClassVar[int]
    serialVersionUID: ClassVar[int]
    def getParams(self) -> AlgorithmParameterSpec: ...
    def getScalar(self) -> Optional: ...
