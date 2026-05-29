from typing import Any, ClassVar, overload
from java.math.BigInteger import BigInteger
from java.security.spec.AlgorithmParameterSpec import AlgorithmParameterSpec
from javax.crypto.spec.DHParameterSpec import DHParameterSpec

class DHPrivateKey:
    serialVersionUID: ClassVar[int]
    serialVersionUID: ClassVar[int]
    serialVersionUID: ClassVar[int]
    @overload
    def getParams(self) -> DHParameterSpec: ...
    @overload
    def getParams(self) -> AlgorithmParameterSpec: ...
    def getX(self) -> BigInteger: ...
