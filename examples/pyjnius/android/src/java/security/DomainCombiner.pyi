from typing import Any, ClassVar, overload
from java.security.ProtectionDomain import ProtectionDomain

class DomainCombiner:
    def combine(self, arg0: list[ProtectionDomain], arg1: list[ProtectionDomain]) -> list[ProtectionDomain]: ...
