from typing import Any, ClassVar, overload

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Runnable:
    """Forward declaration for ``java.lang.Runnable``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('java.lang.Runnable')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://docs.oracle.com/javase/8/docs/api/java/lang/Runnable.html
    """
    ...

class OSBackgroundManager:
    def __init__(self) -> None: ...
    def runRunnableOnThread(self, arg0: Runnable, arg1: str) -> None: ...
