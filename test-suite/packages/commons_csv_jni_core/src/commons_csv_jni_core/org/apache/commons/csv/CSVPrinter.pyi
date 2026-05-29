from typing import Any, ClassVar, overload
from org.apache.commons.csv.CSVFormat import CSVFormat

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Appendable:
    """Forward declaration for ``java.lang.Appendable``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('java.lang.Appendable')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://docs.oracle.com/javase/8/docs/api/java/lang/Appendable.html
    """
    ...
class Iterable:
    """Forward declaration for ``java.lang.Iterable``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('java.lang.Iterable')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html
    """
    ...
class ResultSet:
    """Forward declaration for ``java.sql.ResultSet``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('java.sql.ResultSet')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://docs.oracle.com/javase/8/docs/api/java/sql/ResultSet.html
    """
    ...
class Stream:
    """Forward declaration for ``java.util.stream.Stream``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('java.util.stream.Stream')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://docs.oracle.com/javase/8/docs/api/java/util/stream/Stream.html
    """
    ...

class CSVPrinter:
    def __init__(self, p0: Appendable, p1: CSVFormat) -> None: ...
    def println(self) -> None: ...
    def flush(self) -> None: ...
    def print(self, p0: Any) -> None: ...
    @overload
    def close(self) -> None: ...
    @overload
    def close(self, p0: bool) -> None: ...
    def printComment(self, p0: str) -> None: ...
    @overload
    def printRecords(self, p0: Any) -> None: ...
    @overload
    def printRecords(self, p0: Iterable) -> None: ...
    @overload
    def printRecords(self, p0: ResultSet) -> None: ...
    @overload
    def printRecords(self, p0: ResultSet, p1: bool) -> None: ...
    @overload
    def printRecords(self, p0: Stream) -> None: ...
    def printHeaders(self, p0: ResultSet) -> None: ...
    def getOut(self) -> Appendable: ...
    @overload
    def printRecord(self, p0: Iterable) -> None: ...
    @overload
    def printRecord(self, p0: Stream) -> None: ...
    @overload
    def printRecord(self, p0: Any) -> None: ...
