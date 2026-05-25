from typing import Any, ClassVar, overload

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class ThreadPoolExecutor:
    """Forward declaration for ``java.util.concurrent.ThreadPoolExecutor``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('java.util.concurrent.ThreadPoolExecutor')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/ThreadPoolExecutor.html
    """
    ...
class ExecutorService:
    """Forward declaration for ``java.util.concurrent.ExecutorService``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('java.util.concurrent.ExecutorService')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/ExecutorService.html
    """
    ...

class zzb:
    zza: ClassVar[ThreadPoolExecutor]
    zzb: ClassVar[ExecutorService]
