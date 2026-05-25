from typing import Any, ClassVar, overload
from java.util.function.BiConsumer import BiConsumer
from java.util.function.BinaryOperator import BinaryOperator
from java.util.function.Function import Function
from java.util.function.Supplier import Supplier

class Collector:
    def supplier(self) -> Supplier: ...
    def accumulator(self) -> BiConsumer: ...
    def finisher(self) -> Function: ...
    @overload
    @staticmethod
    def of(p0: Supplier, p1: BiConsumer, p2: BinaryOperator, p3: Function, p4: Any) -> "Collector": ...
    @overload
    @staticmethod
    def of(p0: Supplier, p1: BiConsumer, p2: BinaryOperator, p3: Any) -> "Collector": ...
    def characteristics(self) -> set: ...
    def combiner(self) -> BinaryOperator: ...

    class Characteristics:
        CONCURRENT: ClassVar["Characteristics"]
        UNORDERED: ClassVar["Characteristics"]
        IDENTITY_FINISH: ClassVar["Characteristics"]
        CONCURRENT: ClassVar[Any]
        UNORDERED: ClassVar[Any]
        IDENTITY_FINISH: ClassVar[Any]
        @staticmethod
        def values() -> Any: ...
        @staticmethod
        def valueOf(p0: str) -> Any: ...
