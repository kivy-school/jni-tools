from typing import Any, ClassVar, overload
from java.lang.reflect.TypeVariable import TypeVariable

class GenericDeclaration:
    def getTypeParameters(self) -> list[TypeVariable]: ...
