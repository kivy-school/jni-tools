from typing import Any, ClassVar, overload
from java.security.spec.AlgorithmParameterSpec import AlgorithmParameterSpec
from java.security.spec.ECParameterSpec import ECParameterSpec
from java.security.spec.ECPoint import ECPoint

class ECPublicKey:
    serialVersionUID: ClassVar[int]
    serialVersionUID: ClassVar[int]
    serialVersionUID: ClassVar[int]
    def getW(self) -> ECPoint: ...
    @overload
    def getParams(self) -> ECParameterSpec: ...
    @overload
    def getParams(self) -> AlgorithmParameterSpec: ...
