from typing import Any, ClassVar, overload
from android.database.Cursor import Cursor

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Closeable:
    """Forward declaration for ``java.io.Closeable``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('java.io.Closeable')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://docs.oracle.com/javase/8/docs/api/java/io/Closeable.html
    """
    ...

class CloseHelper:
    def __init__(self) -> None: ...
    @staticmethod
    def close(arg0: Cursor) -> None: ...
    @staticmethod
    def closeQuietly(arg0: Closeable) -> None: ...
