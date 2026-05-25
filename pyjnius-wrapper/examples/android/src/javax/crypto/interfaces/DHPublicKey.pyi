from typing import Any, ClassVar, overload
from java.math.BigInteger import BigInteger

class DHPublicKey:
    serialVersionUID: ClassVar[int]
    def getY(self) -> BigInteger: ...
