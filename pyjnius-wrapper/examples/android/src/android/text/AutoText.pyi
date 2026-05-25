from typing import Any, ClassVar, overload
from android.view.View import View

class AutoText:
    @staticmethod
    def get(arg0: str, arg1: int, arg2: int, arg3: View) -> str: ...
    @staticmethod
    def getSize(arg0: View) -> int: ...
