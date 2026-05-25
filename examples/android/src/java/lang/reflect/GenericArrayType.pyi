from typing import Any, ClassVar, overload
from java.lang.reflect.Type import Type

class GenericArrayType:
    def getGenericComponentType(self) -> Type: ...
