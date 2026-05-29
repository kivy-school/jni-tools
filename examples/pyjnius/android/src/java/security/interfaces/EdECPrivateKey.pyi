from typing import Any, ClassVar, overload
from java.security.spec.AlgorithmParameterSpec import AlgorithmParameterSpec
from java.security.spec.NamedParameterSpec import NamedParameterSpec
from java.util.Optional import Optional

class EdECPrivateKey:
    serialVersionUID: ClassVar[int]
    serialVersionUID: ClassVar[int]
    def getBytes(self) -> Optional: ...
    @overload
    def getParams(self) -> NamedParameterSpec: ...
    @overload
    def getParams(self) -> AlgorithmParameterSpec: ...
