from typing import Any, ClassVar, overload
from java.math.BigInteger import BigInteger
from java.security.spec.AlgorithmParameterSpec import AlgorithmParameterSpec
from java.security.spec.ECParameterSpec import ECParameterSpec

class ECPrivateKey:
    serialVersionUID: ClassVar[int]
    serialVersionUID: ClassVar[int]
    serialVersionUID: ClassVar[int]
    def getS(self) -> BigInteger: ...
    @overload
    def getParams(self) -> ECParameterSpec: ...
    @overload
    def getParams(self) -> AlgorithmParameterSpec: ...
