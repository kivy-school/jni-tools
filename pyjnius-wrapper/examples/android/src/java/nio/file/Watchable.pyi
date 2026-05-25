from typing import Any, ClassVar, overload
from java.nio.file.WatchKey import WatchKey
from java.nio.file.WatchService import WatchService

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Kind:
    """Forward declaration for ``java.nio.file.WatchEvent.Kind``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('java.nio.file.WatchEvent.Kind')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://docs.oracle.com/javase/8/docs/api/java/nio/file/WatchEvent/Kind.html
    """
    ...
class Modifier:
    """Forward declaration for ``java.nio.file.WatchEvent.Modifier``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('java.nio.file.WatchEvent.Modifier')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://docs.oracle.com/javase/8/docs/api/java/nio/file/WatchEvent/Modifier.html
    """
    ...

class Watchable:
    @overload
    def register(self, arg0: WatchService, arg1: list[Kind], *arg2: Modifier) -> WatchKey: ...
    @overload
    def register(self, arg0: WatchService, *arg1: Kind) -> WatchKey: ...
