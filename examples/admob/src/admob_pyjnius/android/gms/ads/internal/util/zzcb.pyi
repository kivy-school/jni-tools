from typing import Any, ClassVar, overload
from android.content.Context import Context

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Callable:
    """Forward declaration for ``java.util.concurrent.Callable``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('java.util.concurrent.Callable')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Callable.html
    """
    ...

class zzcb:
    @staticmethod
    def zza(arg0: Context, arg1: Callable) -> Any: ...
