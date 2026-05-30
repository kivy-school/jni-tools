from typing import Any, ClassVar, overload
from java.math.BigInteger import BigInteger

class RSAPrivateCrtKey:
    serialVersionUID: ClassVar[int]
    serialVersionUID: ClassVar[int]
    serialVersionUID: ClassVar[int]
    serialVersionUID: ClassVar[int]
    def getPublicExponent(self) -> BigInteger: ...
    def getPrimeP(self) -> BigInteger: ...
    def getPrimeQ(self) -> BigInteger: ...
    def getPrimeExponentP(self) -> BigInteger: ...
    def getPrimeExponentQ(self) -> BigInteger: ...
    def getCrtCoefficient(self) -> BigInteger: ...

from typing import Any, ClassVar, overload
from java.security.spec.ECParameterSpec import ECParameterSpec

class ECKey:
    def getParams(self) -> ECParameterSpec: ...

from typing import Any, ClassVar, overload
from java.math.BigInteger import BigInteger

class DSAPublicKey:
    serialVersionUID: ClassVar[int]
    serialVersionUID: ClassVar[int]
    serialVersionUID: ClassVar[int]
    def getY(self) -> BigInteger: ...

from typing import Any, ClassVar, overload
from java.security.spec.ECPoint import ECPoint

class ECPublicKey:
    serialVersionUID: ClassVar[int]
    serialVersionUID: ClassVar[int]
    serialVersionUID: ClassVar[int]
    def getW(self) -> ECPoint: ...

from typing import Any, ClassVar, overload
from java.security.spec.AlgorithmParameterSpec import AlgorithmParameterSpec

class XECKey:
    def getParams(self) -> AlgorithmParameterSpec: ...

from typing import Any, ClassVar, overload
from java.security.spec.EdECPoint import EdECPoint

class EdECPublicKey:
    serialVersionUID: ClassVar[int]
    serialVersionUID: ClassVar[int]
    def getPoint(self) -> EdECPoint: ...

from typing import Any, ClassVar, overload
from java.math.BigInteger import BigInteger

class XECPublicKey:
    serialVersionUID: ClassVar[int]
    serialVersionUID: ClassVar[int]
    def getU(self) -> BigInteger: ...

from typing import Any, ClassVar, overload
from java.math.BigInteger import BigInteger

class DSAPrivateKey:
    serialVersionUID: ClassVar[int]
    serialVersionUID: ClassVar[int]
    serialVersionUID: ClassVar[int]
    def getX(self) -> BigInteger: ...

from typing import Any, ClassVar, overload
from java.math.BigInteger import BigInteger

class DSAParams:
    def getP(self) -> BigInteger: ...
    def getQ(self) -> BigInteger: ...
    def getG(self) -> BigInteger: ...

from typing import Any, ClassVar, overload
from java.util.Optional import Optional

class XECPrivateKey:
    serialVersionUID: ClassVar[int]
    serialVersionUID: ClassVar[int]
    def getScalar(self) -> Optional: ...

from typing import Any, ClassVar, overload
from java.math.BigInteger import BigInteger

class RSAPublicKey:
    serialVersionUID: ClassVar[int]
    serialVersionUID: ClassVar[int]
    serialVersionUID: ClassVar[int]
    def getPublicExponent(self) -> BigInteger: ...

from typing import Any, ClassVar, overload
from java.math.BigInteger import BigInteger

class RSAMultiPrimePrivateCrtKey:
    serialVersionUID: ClassVar[int]
    serialVersionUID: ClassVar[int]
    serialVersionUID: ClassVar[int]
    serialVersionUID: ClassVar[int]
    def getPublicExponent(self) -> BigInteger: ...
    def getPrimeP(self) -> BigInteger: ...
    def getPrimeQ(self) -> BigInteger: ...
    def getPrimeExponentP(self) -> BigInteger: ...
    def getPrimeExponentQ(self) -> BigInteger: ...
    def getCrtCoefficient(self) -> BigInteger: ...
    def getOtherPrimeInfo(self) -> Any: ...

from typing import Any, ClassVar, overload
from java.security.SecureRandom import SecureRandom
from java.security.interfaces.DSAParams import DSAParams

class DSAKeyPairGenerator:
    @overload
    def initialize(self, p0: DSAParams, p1: SecureRandom) -> None: ...
    @overload
    def initialize(self, p0: int, p1: bool, p2: SecureRandom) -> None: ...

from typing import Any, ClassVar, overload
from java.security.interfaces.DSAParams import DSAParams

class DSAKey:
    def getParams(self) -> DSAParams: ...

from typing import Any, ClassVar, overload
from java.security.spec.NamedParameterSpec import NamedParameterSpec

class EdECKey:
    def getParams(self) -> NamedParameterSpec: ...

from typing import Any, ClassVar, overload
from java.math.BigInteger import BigInteger

class RSAPrivateKey:
    serialVersionUID: ClassVar[int]
    serialVersionUID: ClassVar[int]
    serialVersionUID: ClassVar[int]
    def getPrivateExponent(self) -> BigInteger: ...

from typing import Any, ClassVar, overload
from java.math.BigInteger import BigInteger
from java.security.spec.AlgorithmParameterSpec import AlgorithmParameterSpec

class RSAKey:
    def getParams(self) -> AlgorithmParameterSpec: ...
    def getModulus(self) -> BigInteger: ...

from typing import Any, ClassVar, overload
from java.util.Optional import Optional

class EdECPrivateKey:
    serialVersionUID: ClassVar[int]
    serialVersionUID: ClassVar[int]
    def getBytes(self) -> Optional: ...

from typing import Any, ClassVar, overload
from java.math.BigInteger import BigInteger

class ECPrivateKey:
    serialVersionUID: ClassVar[int]
    serialVersionUID: ClassVar[int]
    serialVersionUID: ClassVar[int]
    def getS(self) -> BigInteger: ...

