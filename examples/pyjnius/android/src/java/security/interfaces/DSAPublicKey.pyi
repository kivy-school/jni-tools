from typing import Any, ClassVar, overload
from java.math.BigInteger import BigInteger
from java.security.interfaces.DSAParams import DSAParams
from java.security.spec.AlgorithmParameterSpec import AlgorithmParameterSpec

class DSAPublicKey:
    serialVersionUID: ClassVar[int]
    serialVersionUID: ClassVar[int]
    serialVersionUID: ClassVar[int]
    def getY(self) -> BigInteger: ...
    @overload
    def getParams(self) -> DSAParams: ...
    @overload
    def getParams(self) -> AlgorithmParameterSpec: ...
