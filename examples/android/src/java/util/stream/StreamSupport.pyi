from typing import Any, ClassVar, overload
from java.util.Spliterator import Spliterator
from java.util.function.Supplier import Supplier
from java.util.stream.DoubleStream import DoubleStream
from java.util.stream.IntStream import IntStream
from java.util.stream.LongStream import LongStream
from java.util.stream.Stream import Stream

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class OfInt:
    """Forward declaration for ``java.util.Spliterator.OfInt``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('java.util.Spliterator.OfInt')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://docs.oracle.com/javase/8/docs/api/java/util/Spliterator/OfInt.html
    """
    ...
class OfLong:
    """Forward declaration for ``java.util.Spliterator.OfLong``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('java.util.Spliterator.OfLong')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://docs.oracle.com/javase/8/docs/api/java/util/Spliterator/OfLong.html
    """
    ...
class OfDouble:
    """Forward declaration for ``java.util.Spliterator.OfDouble``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('java.util.Spliterator.OfDouble')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://docs.oracle.com/javase/8/docs/api/java/util/Spliterator/OfDouble.html
    """
    ...

class StreamSupport:
    @overload
    @staticmethod
    def stream(arg0: Spliterator, arg1: bool) -> Stream: ...
    @overload
    @staticmethod
    def stream(arg0: Supplier, arg1: int, arg2: bool) -> Stream: ...
    @overload
    @staticmethod
    def intStream(arg0: OfInt, arg1: bool) -> IntStream: ...
    @overload
    @staticmethod
    def intStream(arg0: Supplier, arg1: int, arg2: bool) -> IntStream: ...
    @overload
    @staticmethod
    def longStream(arg0: OfLong, arg1: bool) -> LongStream: ...
    @overload
    @staticmethod
    def longStream(arg0: Supplier, arg1: int, arg2: bool) -> LongStream: ...
    @overload
    @staticmethod
    def doubleStream(arg0: OfDouble, arg1: bool) -> DoubleStream: ...
    @overload
    @staticmethod
    def doubleStream(arg0: Supplier, arg1: int, arg2: bool) -> DoubleStream: ...
