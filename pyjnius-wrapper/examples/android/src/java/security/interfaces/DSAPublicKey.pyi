from typing import Any, ClassVar, overload
from java.math.BigInteger import BigInteger

class DSAPublicKey:
    serialVersionUID: ClassVar[int]
    def getY(self) -> BigInteger: ...
