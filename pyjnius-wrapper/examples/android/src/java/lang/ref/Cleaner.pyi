from typing import Any, ClassVar, overload
from java.lang.Runnable import Runnable
from java.util.concurrent.ThreadFactory import ThreadFactory

class Cleaner:
    @overload
    @staticmethod
    def create() -> "Cleaner": ...
    @overload
    @staticmethod
    def create(arg0: ThreadFactory) -> "Cleaner": ...
    def register(self, arg0: Any, arg1: Runnable) -> "Cleanable": ...

    class Cleanable:
        def clean(self) -> None: ...
