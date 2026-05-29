from typing import Any, ClassVar, overload
from java.math.BigInteger import BigInteger

class RSAPublicKey:
    serialVersionUID: ClassVar[int]
    def getPublicExponent(self) -> BigInteger: ...
