from typing import Any, ClassVar, overload
from java.security.SecureRandom import SecureRandom
from java.security.interfaces.DSAParams import DSAParams

class DSAKeyPairGenerator:
    @overload
    def initialize(self, p0: DSAParams, p1: SecureRandom) -> None: ...
    @overload
    def initialize(self, p0: int, p1: bool, p2: SecureRandom) -> None: ...
