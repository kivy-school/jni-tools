from typing import Any, ClassVar, overload
from java.math.BigInteger import BigInteger
from java.security.spec.AlgorithmParameterSpec import AlgorithmParameterSpec

class XECPublicKey:
    serialVersionUID: ClassVar[int]
    serialVersionUID: ClassVar[int]
    def getParams(self) -> AlgorithmParameterSpec: ...
    def getU(self) -> BigInteger: ...
