from typing import Any, ClassVar, overload

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class StringBuilder:
    """Forward declaration for ``java.lang.StringBuilder``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('java.lang.StringBuilder')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://docs.oracle.com/javase/8/docs/api/java/lang/StringBuilder.html
    """
    ...
class Iterable:
    """Forward declaration for ``java.lang.Iterable``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('java.lang.Iterable')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html
    """
    ...
class Iterator:
    """Forward declaration for ``java.util.Iterator``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('java.util.Iterator')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://docs.oracle.com/javase/8/docs/api/java/util/Iterator.html
    """
    ...

class zzgtl:
    @staticmethod
    def zzb(arg0: StringBuilder, arg1: Iterable, arg2: str) -> StringBuilder: ...
    @staticmethod
    def zzc(arg0: StringBuilder, arg1: Iterator, arg2: str) -> StringBuilder: ...
    @staticmethod
    def zzd(arg0: Iterable, arg1: str) -> str: ...
