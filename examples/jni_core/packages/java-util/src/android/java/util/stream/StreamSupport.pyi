from typing import Any, ClassVar, overload
from java.util.Spliterator import Spliterator
from java.util.function.Supplier import Supplier
from java.util.stream.DoubleStream import DoubleStream
from java.util.stream.IntStream import IntStream
from java.util.stream.LongStream import LongStream
from java.util.stream.Stream import Stream

class StreamSupport:
    @overload
    @staticmethod
    def stream(p0: Supplier, p1: int, p2: bool) -> Stream: ...
    @overload
    @staticmethod
    def stream(p0: Spliterator, p1: bool) -> Stream: ...
    @overload
    @staticmethod
    def intStream(p0: Supplier, p1: int, p2: bool) -> IntStream: ...
    @overload
    @staticmethod
    def intStream(p0: Any, p1: bool) -> IntStream: ...
    @overload
    @staticmethod
    def longStream(p0: Supplier, p1: int, p2: bool) -> LongStream: ...
    @overload
    @staticmethod
    def longStream(p0: Any, p1: bool) -> LongStream: ...
    @overload
    @staticmethod
    def doubleStream(p0: Any, p1: bool) -> DoubleStream: ...
    @overload
    @staticmethod
    def doubleStream(p0: Supplier, p1: int, p2: bool) -> DoubleStream: ...
