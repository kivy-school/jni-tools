from typing import Any, ClassVar, overload

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class ByteBuffer:
    """Forward declaration for ``java.nio.ByteBuffer``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('java.nio.ByteBuffer')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://docs.oracle.com/javase/8/docs/api/java/nio/ByteBuffer.html
    """
    ...

class zzifc:
    zza: ClassVar[list[int]]
    zzb: ClassVar[ByteBuffer]
    @staticmethod
    def zza() -> int: ...
    @staticmethod
    def zzb(arg0: bool) -> int: ...
