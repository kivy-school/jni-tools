from typing import Any, ClassVar, overload
from java.lang.invoke.MethodType import MethodType
from java.lang.reflect.Member import Member

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

class MethodHandleInfo:
    REF_getField: ClassVar[int]
    REF_getStatic: ClassVar[int]
    REF_invokeInterface: ClassVar[int]
    REF_invokeSpecial: ClassVar[int]
    REF_invokeStatic: ClassVar[int]
    REF_invokeVirtual: ClassVar[int]
    REF_newInvokeSpecial: ClassVar[int]
    REF_putField: ClassVar[int]
    REF_putStatic: ClassVar[int]
    def getReferenceKind(self) -> int: ...
    def getDeclaringClass(self) -> type: ...
    def getName(self) -> str: ...
    def getMethodType(self) -> MethodType: ...
    def reflectAs(self, arg0: type, arg1: Lookup) -> Member: ...
    def getModifiers(self) -> int: ...
    def isVarArgs(self) -> bool: ...
    @staticmethod
    def referenceKindToString(arg0: int) -> str: ...
    @staticmethod
    def toString(arg0: int, arg1: type, arg2: str, arg3: MethodType) -> str: ...
    @staticmethod
    def refKindIsValid(arg0: int) -> bool: ...
    @staticmethod
    def refKindIsField(arg0: int) -> bool: ...
    @staticmethod
    def refKindName(arg0: int) -> str: ...
