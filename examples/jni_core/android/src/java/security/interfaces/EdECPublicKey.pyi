from typing import Any, ClassVar, overload
from java.security.spec.AlgorithmParameterSpec import AlgorithmParameterSpec
from java.security.spec.EdECPoint import EdECPoint
from java.security.spec.NamedParameterSpec import NamedParameterSpec

class EdECPublicKey:
    serialVersionUID: ClassVar[int]
    serialVersionUID: ClassVar[int]
    @overload
    def getParams(self) -> NamedParameterSpec: ...
    @overload
    def getParams(self) -> AlgorithmParameterSpec: ...
    def getPoint(self) -> EdECPoint: ...
