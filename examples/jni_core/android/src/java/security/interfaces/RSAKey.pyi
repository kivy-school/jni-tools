from typing import Any, ClassVar, overload
from java.math.BigInteger import BigInteger
from java.security.spec.AlgorithmParameterSpec import AlgorithmParameterSpec

class RSAKey:
    def getParams(self) -> AlgorithmParameterSpec: ...
    def getModulus(self) -> BigInteger: ...
