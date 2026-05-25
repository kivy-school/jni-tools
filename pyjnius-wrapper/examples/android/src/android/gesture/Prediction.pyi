from typing import Any, ClassVar, overload

class Prediction:
    name: str
    score: float
    def toString(self) -> str: ...
