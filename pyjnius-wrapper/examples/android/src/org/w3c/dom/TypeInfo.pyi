from typing import Any, ClassVar, overload

class TypeInfo:
    DERIVATION_EXTENSION: ClassVar[int]
    DERIVATION_LIST: ClassVar[int]
    DERIVATION_RESTRICTION: ClassVar[int]
    DERIVATION_UNION: ClassVar[int]
    def getTypeName(self) -> str: ...
    def getTypeNamespace(self) -> str: ...
    def isDerivedFrom(self, arg0: str, arg1: str, arg2: int) -> bool: ...
