from typing import Any, ClassVar, overload
from org.apache.commons.csv.CSVFormat import CSVFormat

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Reader:
    """Forward declaration for ``java.io.Reader``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('java.io.Reader')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://docs.oracle.com/javase/8/docs/api/java/io/Reader.html
    """
    ...
class Iterator:
    """Forward declaration for ``java.util.Iterator``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('java.util.Iterator')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://docs.oracle.com/javase/8/docs/api/java/util/Iterator.html
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
class File:
    """Forward declaration for ``java.io.File``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('java.io.File')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://docs.oracle.com/javase/8/docs/api/java/io/File.html
    """
    ...
class Charset:
    """Forward declaration for ``java.nio.charset.Charset``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('java.nio.charset.Charset')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://docs.oracle.com/javase/8/docs/api/java/nio/charset/Charset.html
    """
    ...
class Path:
    """Forward declaration for ``java.nio.file.Path``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('java.nio.file.Path')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://docs.oracle.com/javase/8/docs/api/java/nio/file/Path.html
    """
    ...
class InputStream:
    """Forward declaration for ``java.io.InputStream``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('java.io.InputStream')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://docs.oracle.com/javase/8/docs/api/java/io/InputStream.html
    """
    ...
class URL:
    """Forward declaration for ``java.net.URL``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('java.net.URL')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://docs.oracle.com/javase/8/docs/api/java/net/URL.html
    """
    ...

class CSVParser:
    @overload
    def __init__(self, p0: Reader, p1: CSVFormat, p2: int, p3: int) -> None: ...
    @overload
    def __init__(self, p0: Reader, p1: CSVFormat) -> None: ...
    def iterator(self) -> Iterator: ...
    def stream(self) -> Stream: ...
    def close(self) -> None: ...
    @overload
    @staticmethod
    def parse(p0: File, p1: Charset, p2: CSVFormat) -> "CSVParser": ...
    @overload
    @staticmethod
    def parse(p0: Path, p1: Charset, p2: CSVFormat) -> "CSVParser": ...
    @overload
    @staticmethod
    def parse(p0: Reader, p1: CSVFormat) -> "CSVParser": ...
    @overload
    @staticmethod
    def parse(p0: InputStream, p1: Charset, p2: CSVFormat) -> "CSVParser": ...
    @overload
    @staticmethod
    def parse(p0: str, p1: CSVFormat) -> "CSVParser": ...
    @overload
    @staticmethod
    def parse(p0: URL, p1: Charset, p2: CSVFormat) -> "CSVParser": ...
    def getCurrentLineNumber(self) -> int: ...
    def isClosed(self) -> bool: ...
    def getFirstEndOfLine(self) -> str: ...
    def getHeaderComment(self) -> str: ...
    def getHeaderMap(self) -> dict: ...
    def getHeaderNames(self) -> list: ...
    def getRecordNumber(self) -> int: ...
    def getRecords(self) -> list: ...
    def getTrailerComment(self) -> str: ...
    def hasHeaderComment(self) -> bool: ...
    def hasTrailerComment(self) -> bool: ...
