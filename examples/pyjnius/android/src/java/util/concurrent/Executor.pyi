from typing import Any, ClassVar, overload
from java.lang.Runnable import Runnable

class Executor:
    def execute(self, arg0: Runnable) -> None: ...
