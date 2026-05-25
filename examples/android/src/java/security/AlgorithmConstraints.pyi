from typing import Any, ClassVar, overload
from java.security.AlgorithmParameters import AlgorithmParameters
from java.security.Key import Key

class AlgorithmConstraints:
    @overload
    def permits(self, arg0: set, arg1: str, arg2: AlgorithmParameters) -> bool: ...
    @overload
    def permits(self, arg0: set, arg1: Key) -> bool: ...
    @overload
    def permits(self, arg0: set, arg1: str, arg2: Key, arg3: AlgorithmParameters) -> bool: ...
