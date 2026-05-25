from typing import Any, ClassVar, overload
from java.security.spec.EdECPoint import EdECPoint

class EdECPublicKey:
    def getPoint(self) -> EdECPoint: ...
