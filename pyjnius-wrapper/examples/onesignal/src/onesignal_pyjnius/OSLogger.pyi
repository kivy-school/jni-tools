from typing import Any, ClassVar, overload

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Throwable:
    """Forward declaration for ``java.lang.Throwable``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('java.lang.Throwable')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://docs.oracle.com/javase/8/docs/api/java/lang/Throwable.html
    """
    ...

class OSLogger:
    def verbose(self, arg0: str) -> None: ...
    def debug(self, arg0: str) -> None: ...
    def info(self, arg0: str) -> None: ...
    def warning(self, arg0: str) -> None: ...
    @overload
    def error(self, arg0: str) -> None: ...
    @overload
    def error(self, arg0: str, arg1: Throwable) -> None: ...
