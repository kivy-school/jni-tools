from typing import Any, ClassVar, overload
from java.security.SecureRandom import SecureRandom
from java.security.interfaces.DSAParams import DSAParams

class DSAKeyPairGenerator:
    @overload
    def initialize(self, arg0: DSAParams, arg1: SecureRandom) -> None: ...
    @overload
    def initialize(self, arg0: int, arg1: bool, arg2: SecureRandom) -> None: ...
