from typing import Any, ClassVar, overload

class PBEKey:
    serialVersionUID: ClassVar[int]
    serialVersionUID: ClassVar[int]
    serialVersionUID: ClassVar[int]
    def getIterationCount(self) -> int: ...
    def getSalt(self) -> Any: ...
    def getPassword(self) -> Any: ...

from typing import Any, ClassVar, overload
from java.math.BigInteger import BigInteger

class DHPrivateKey:
    serialVersionUID: ClassVar[int]
    serialVersionUID: ClassVar[int]
    serialVersionUID: ClassVar[int]
    def getX(self) -> BigInteger: ...

from typing import Any, ClassVar, overload
from java.math.BigInteger import BigInteger

class DHPublicKey:
    serialVersionUID: ClassVar[int]
    serialVersionUID: ClassVar[int]
    serialVersionUID: ClassVar[int]
    def getY(self) -> BigInteger: ...

from typing import Any, ClassVar, overload
from javax.crypto.spec.DHParameterSpec import DHParameterSpec

class DHKey:
    def getParams(self) -> DHParameterSpec: ...

