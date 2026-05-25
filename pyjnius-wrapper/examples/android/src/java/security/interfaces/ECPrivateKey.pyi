from typing import Any, ClassVar, overload
from java.math.BigInteger import BigInteger

class ECPrivateKey:
    serialVersionUID: ClassVar[int]
    def getS(self) -> BigInteger: ...
