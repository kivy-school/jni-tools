from typing import Any, ClassVar, overload
from java.lang.ClassLoader import ClassLoader
from java.util.Iterator import Iterator
from java.util.Optional import Optional
from java.util.stream.Stream import Stream

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class ModuleLayer:
    """Forward declaration for ``java.lang.ModuleLayer``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('java.lang.ModuleLayer')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://docs.oracle.com/javase/8/docs/api/java/lang/ModuleLayer.html
    """
    ...

class ServiceLoader:
    def reload(self) -> None: ...
    def findFirst(self) -> Optional: ...
    @staticmethod
    def loadInstalled(p0: type) -> "ServiceLoader": ...
    def toString(self) -> str: ...
    @overload
    @staticmethod
    def load(p0: type) -> "ServiceLoader": ...
    @overload
    @staticmethod
    def load(p0: ModuleLayer, p1: type) -> "ServiceLoader": ...
    @overload
    @staticmethod
    def load(p0: type, p1: ClassLoader) -> "ServiceLoader": ...
    def iterator(self) -> Iterator: ...
    def stream(self) -> Stream: ...

    class Provider:
        def get(self) -> Any: ...
        def type(self) -> type: ...
