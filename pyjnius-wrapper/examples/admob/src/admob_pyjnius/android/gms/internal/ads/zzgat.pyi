from typing import Any, ClassVar, overload

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class ExecutorService:
    """Forward declaration for ``java.util.concurrent.ExecutorService``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('java.util.concurrent.ExecutorService')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/ExecutorService.html
    """
    ...
class ThreadFactory:
    """Forward declaration for ``java.util.concurrent.ThreadFactory``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('java.util.concurrent.ThreadFactory')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/ThreadFactory.html
    """
    ...

class zzgat:
    def zza(self, arg0: int) -> ExecutorService: ...
    def zzb(self, arg0: int, arg1: ThreadFactory, arg2: int) -> ExecutorService: ...
    def zzc(self, arg0: int) -> ExecutorService: ...
    def zzd(self, arg0: ThreadFactory, arg1: int) -> ExecutorService: ...
