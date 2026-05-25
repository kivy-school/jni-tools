from typing import Any, ClassVar, overload
from java.util.Comparator import Comparator

class BinaryOperator:
    @staticmethod
    def minBy(arg0: Comparator) -> "BinaryOperator": ...
    @staticmethod
    def maxBy(arg0: Comparator) -> "BinaryOperator": ...
