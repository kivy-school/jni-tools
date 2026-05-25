from typing import Any, ClassVar, overload
from java.math.BigInteger import BigInteger

class RSAPrivateKey:
    serialVersionUID: ClassVar[int]
    def getPrivateExponent(self) -> BigInteger: ...
