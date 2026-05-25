from typing import Any, ClassVar, overload
from android.view.View import View

class AutoText:
    @staticmethod
    def getSize(p0: View) -> int: ...
    @staticmethod
    def get(p0: str, p1: int, p2: int, p3: View) -> str: ...
