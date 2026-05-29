from typing import Any, ClassVar, overload
from java.security.AlgorithmParameters import AlgorithmParameters
from java.security.Key import Key

class AlgorithmConstraints:
    @overload
    def permits(self, p0: set, p1: str, p2: AlgorithmParameters) -> bool: ...
    @overload
    def permits(self, p0: set, p1: Key) -> bool: ...
    @overload
    def permits(self, p0: set, p1: str, p2: Key, p3: AlgorithmParameters) -> bool: ...
