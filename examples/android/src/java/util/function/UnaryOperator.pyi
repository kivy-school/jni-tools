from typing import Any, ClassVar, overload

class UnaryOperator:
    @staticmethod
    def identity() -> "UnaryOperator": ...
