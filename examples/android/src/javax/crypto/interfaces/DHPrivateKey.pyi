from typing import Any, ClassVar, overload
from java.math.BigInteger import BigInteger

class DHPrivateKey:
    serialVersionUID: ClassVar[int]
    def getX(self) -> BigInteger: ...
