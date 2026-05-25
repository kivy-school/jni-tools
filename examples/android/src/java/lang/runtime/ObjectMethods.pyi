from typing import Any, ClassVar, overload
from java.lang.invoke.MethodHandle import MethodHandle
from java.lang.invoke.TypeDescriptor import TypeDescriptor

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Lookup:
    """Forward declaration for ``java.lang.invoke.MethodHandles.Lookup``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('java.lang.invoke.MethodHandles.Lookup')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://docs.oracle.com/javase/8/docs/api/java/lang/invoke/MethodHandles/Lookup.html
    """
    ...

class ObjectMethods:
    @staticmethod
    def bootstrap(arg0: Lookup, arg1: str, arg2: TypeDescriptor, arg3: type, arg4: str, *arg5: MethodHandle) -> Any: ...
