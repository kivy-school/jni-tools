from typing import Any, ClassVar, overload
from java.util.Comparator import Comparator

class BinaryOperator:
    @staticmethod
    def minBy(p0: Comparator) -> "BinaryOperator": ...
    @staticmethod
    def maxBy(p0: Comparator) -> "BinaryOperator": ...
