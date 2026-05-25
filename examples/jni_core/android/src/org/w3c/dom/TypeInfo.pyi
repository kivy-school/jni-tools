from typing import Any, ClassVar, overload

class TypeInfo:
    DERIVATION_RESTRICTION: ClassVar[int]
    DERIVATION_EXTENSION: ClassVar[int]
    DERIVATION_UNION: ClassVar[int]
    DERIVATION_LIST: ClassVar[int]
    def getTypeNamespace(self) -> str: ...
    def isDerivedFrom(self, p0: str, p1: str, p2: int) -> bool: ...
    def getTypeName(self) -> str: ...
